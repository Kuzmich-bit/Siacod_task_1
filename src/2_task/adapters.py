from providers import LegacyProvider, AsyncProvider, PollingProvider
from interface import IPaymentProvider

class ProviderOneAdapter(IPaymentProvider):

    def __init__(self, api: LegacyProvider) -> None:
        self.api = api

class ProviderTwoAdapter(IPaymentProvider):

    def __init__(self, api: AsyncProvider) -> None:
        self.api = api

class ProviderThreeAdapter(IPaymentProvider):

    def __init__(self, api: PollingProvider, max_attemps: int = 5) -> None:
        self.api = api
        self.max_attemps = max_attemps
