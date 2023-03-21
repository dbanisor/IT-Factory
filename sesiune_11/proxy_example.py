from abc import ABC, abstractmethod


class Money(ABC):
    @abstractmethod
    def pay(self, s):
        pass


class Cash(Money):
    def __init__(self, amount, limit=10000):
        self.amount = amount
        self.limit = limit

    def pay(self, s):
        self.amount -= s


class Card(Money):  # aceasta este clasa Proxy
    def __init__(self, cash):
        self.cash = cash

    def pay(self, s):
        if self.amount_ok(s) and self.limit_ok(s):
            self.cash.pay(s)

    def amount_ok(self, s):
        return self.cash.amount > s

    def limit_ok(self, s):
        return self.cash.limit > s


cash = Cash(10000, 2000)
cash.pay(2500)
print(cash.amount)

print("*" * 50)

cash = Cash(10000, 2000)
card = Card(cash)
card.pay(2500)
print(cash.amount)