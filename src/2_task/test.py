from providers import LegacyProvider, AsyncProvider, PollingProvider
from adapters import ProviderOneAdapter, ProviderTwoAdapter, ProviderThreeAdapter

class StuckProvider:
    def transaction(self, account_id, amount):
        return 999

    def check_status(self, operation_id):
        return "PROCESSING"

def func_test_one():
    bank = LegacyProvider()
    adapter = ProviderOneAdapter(bank)

    if not adapter.pay(150.34, "artur_pirozhkov"):
        return print('1_ошибка в тесте: 1')
    if adapter.pay(0, "artur_pirozhkov"):
        return print('1_ошибка в тесте: 2')
    if adapter.pay(-15, "artur_pirozhkov"):
        return print('1_ошибка в тесте: 3')
    if adapter.pay(1500000, "artur_pirozhkov"):
        return print('1_ошибка в тесте: 4')
    if not adapter.pay(10000, "artur_pirozhkov"):
        return print('1_ошибка в тесте: 5')

    return print('1_ошибок нет')

def func_test_two():
    bank = AsyncProvider()
    adapter = ProviderTwoAdapter(bank)

    if not adapter.pay(200, "artur_pirozhkov"):
        return print('2_ошибка в тесте: 1')
    if adapter.pay(0, "artur_pirozhkov"):
        return print('2_ошибка в тесте: 2')
    if adapter.pay(-50, "artur_pirozhkov"):
        return print('2_ошибка в тесте: 3')
    if not adapter.pay(99.99, "artur_pirozhkov"):
        return print('2_ошибка в тесте: 4')

    return print('2_ошибок нет')

def func_test_three():
    bank = PollingProvider()
    adapter = ProviderThreeAdapter(bank, max_attemps=5)

    if not adapter.pay(500.0, "artur_pirozhkov"):
        return print('3_ошибка в тесте: 1')

    stuck_bank = StuckProvider()
    stuck_adapter = ProviderThreeAdapter(stuck_bank, max_attemps=3)

    try:
        stuck_adapter.pay(100.0, "artur_pirozhkov")
        return print('3_ошибка в тесте: На время TimeoutError')
    except TimeoutError:
        pass

    print('3_ошибок нет')

func_test_one()
func_test_two()
func_test_three()