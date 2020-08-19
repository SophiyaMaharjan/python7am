class Mobile:
    def __init__(self, name):
        self.name = name
        pass
    def mobilename(self):
        return f'I am {self.name}'

class Nokia(Mobile):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price
        pass
    def price(self):
        return f'the price is {str(self.price)}'
    
obj = Nokia('abc', 2000)
print(obj.mobilename())
print(obj.price())