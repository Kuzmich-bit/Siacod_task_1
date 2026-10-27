from abc import ABC, abstractmethod

class IPaymentProvider(ABC):

    @abstractmethod
    def pay(self, amount_rubles: float, account_id: str) -> bool:
        ...