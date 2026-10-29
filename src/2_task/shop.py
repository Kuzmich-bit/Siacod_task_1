from providers import LegacyProvider, AsyncProvider, PollingProvider
from adapters import ProviderOneAdapter, ProviderTwoAdapter, ProviderThreeAdapter
from interface import IPaymentProvider

class Shop:
    def __init__(self, provider: IPaymentProvider):
        self.provider = provider

    def buy(self, price: float, account_id: str):
        print(f'К оплате: {price}')
        if self.provider.pay(price, account_id):
            print('Оплачено')
        else:
            print('Отказано')
def main():
    shop1 = Shop(ProviderOneAdapter(LegacyProvider()))
    shop2 = Shop(ProviderTwoAdapter(AsyncProvider()))
    shop3 = Shop(ProviderThreeAdapter(PollingProvider()))

    shop1.buy(150.50, "baskov")
    shop2.buy(1200.0, 'kuzmich')
    shop3.buy(500.0, "polanski")

    shop1.buy(0, "baskov")

if __name__ == "__main__":
    main()