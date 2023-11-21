class Receipt:
    def __init__(self):
        self.dishes = []
    def add_dish(self,dish):
        self.dishes.append(dish)
    def total(self):
        totaltxt = ''
        total_price = 0
        for dish in self.dishes:
            total_price += dish.get_price()
            if len(totaltxt) == 0:
                totaltxt = dish.format()
            else:
                totaltxt = totaltxt + f'\n{dish.format()}'

        totaltxt = totaltxt + f'\n\n\n    Total: £{total_price:.2f}'
        print(totaltxt)
        return totaltxt