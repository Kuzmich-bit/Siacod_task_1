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

class ProviderThreeAdapter(IPaymentProvider):

    def __init__(self, api: PollingProvider, max_attemps: int = 5) -> None:
        self.api = api
        self.max_attemps = max_attemps
