from abc import ABCMeta,abstractmethod

class PaymentStrategy(metaclass=ABCMeta):
    """Abstract method for the available payment strategies"""
    @abstractmethod
    def paymentStrategy(self):
        pass

class CreditCard(PaymentStrategy):
    def __init__(self,account):
        self.account = account 
    def paymentStrategy(self):
        return self.account - self.account*0.1      # 10% discount for card payments

class BankTransfer(PaymentStrategy):
    def __init__(self,account):
        self.account = account 
    def paymentStrategy(self):
        return self.account + 1.0                   # 1euro additional cost due to bank comission

class CashPaying(PaymentStrategy):
    def __init__(self,account):
        self.account = account 
    def paymentStrategy(self):
        return self.account + 2.0                   # 2euros additional cost for pay-on-delivery method

