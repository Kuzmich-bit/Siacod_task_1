from providers import LegacyProvider, AsyncProvider, PollingProvider
from adapters import ProviderOneAdapter, ProviderTwoAdapter, ProviderThreeAdapter

bank = PollingProvider()
adapter = ProviderThreeAdapter(bank)
print(adapter.pay(150.34, "artur_pirozhkov"))
print(adapter.pay(0, "artur_pirozhkov"))
print(adapter.pay(-15, "artur_pirozhkov"))
print(adapter.pay(15000000, "artur_pirozhkov"))
print(adapter.pay(10000, "artur_pirozhkov"))