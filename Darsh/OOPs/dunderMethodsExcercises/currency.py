# we will make a class for money
# in this class there will two values, 1) value, 2) currency
from typing import Union

exchange_rates = {  # USD -> currency
    "INR": 75.00,
    "EUR": 0.91,
    "GBP": 0.79,
    "JPY": 113.50,
    "AUD": 1.39,
    "CAD": 1.28,
    "CHF": 0.93,
    "CNY": 6.37,
    "NZD": 1.47,
    "SGD": 1.36,
    "HKD": 7.80,
    "MXN": 20.50,
    "BRL": 5.40,
    "ZAR": 15.20,
    "RUB": 74.50,
    "USD": 1.00
}

class Money:
    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

    def __add__(self, other: Union["Money", int, float]):
        if isinstance(other, Money):
            if self.currency != other.currency:
                if self.currency in exchange_rates.keys() and other.currency in exchange_rates.keys():
                    return Money(self.value + other.value * exchange_rates[self.currency] / exchange_rates[other.currency], self.currency)
                return None
            else:
                return Money(self.value + other.value, self. currency)
        else:
            if isinstance(other, (int, float)):
                return Money(self.value + other, self.currency)
            else:
                raise TypeError("Both objects must be of type Money | int | float")

    def __str__(self):
        return f"{self.value} {self.currency}"


inr = Money(100, "INR")
inr2 = Money(240, "INR")
eur = Money(100, "EUR")
usd = Money(100, "USD")


totalMoneyInUSD = (eur + usd + inr + inr2) +  10.91 + Money(140, "INR")

print(usd)
print(inr)
print(inr2)
print(eur)

print(totalMoneyInUSD)
