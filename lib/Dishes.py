class Dishes:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def format(self):
        return f'{self.name}: £{self.price:.2f}'
    def get_price(self):
        return self.price
