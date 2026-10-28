from typing import Dict, Any

from providers import LegacyProvider, AsyncProvider, PollingProvider
from interface import IPaymentProvider

class ProviderOneAdapter(IPaymentProvider):

    def __init__(self, api: LegacyProvider) -> None:
        self.api = api

    def pay(self, amount_rubles: float, account_id: str) -> bool:
        amount_kopecks = int(round(amount_rubles * 100))
        error_code = self.api.pay_legacy(account_id, amount_kopecks)
        return error_code == 0

class ProviderTwoAdapter(IPaymentProvider):

    def __init__(self, api: AsyncProvider) -> None:
        self.api = api

    def pay(self, amount_rubles: float, account_id: str) -> bool:
        result: Dict[str, Any] = {"status": None}

        def callback_handler(response: str) -> None:
            result["status"] = (response == "SUCCESS")

        self.api.pay_async(account_id, amount_rubles, callback_handler)

        return result["status"] is True

class ProviderThreeAdapter(IPaymentProvider):

    def __init__(self, api: PollingProvider, max_attemps: int = 5) -> None:
        self.api = api
        self.max_attemps = max_attemps

    def pay(self, amount_rubles: float, account_id: str) -> bool:
        operation_id = self.api.transaction(account_id, amount_rubles)

        for _ in range(self.max_attemps):
            status = self.api.check_status(operation_id)

            if status == "COMPLETED":
                return True
            elif status in ("DECLINED", "UNKNOWN"):
                return False

        raise TimeoutError(
            f"Провайдер не ответил за {self.max_attemps} попыток"
        )