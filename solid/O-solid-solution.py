# Here your solution
from abc import ABC, abstractmethod

class PaymentMethodInterface(ABC):
    @abstractmethod
    def calculator_fee(self):
        pass

class CreditCard(PaymentMethodInterface):
    def __init__(self, amount):
        self.amount = amount

    def calculator_fee(self):
        return self.amount * 0.03


class PayPal(PaymentMethodInterface):
    def __init__(self, amount):
        self.amount = amount

    def calculator_fee(self):
        return self.amount * 0.05

class BankTransfer(PaymentMethodInterface):
    def __init__(self, amount):
        self.amount = amount

    def calculator_fee(self):
        return self.amount * 2.5

class FeeCalculator:
    @staticmethod
    def calculator_fee(payment_method: PaymentMethodInterface):
        return payment_method.calculator_fee()