





class OrderMeal:
    def __init__(self,receipt,*dishes):
        self.dishes = []
        self.receipt = receipt
        for dish in dishes:
            self.dishes.append(dish)
    def list_dishes(self):
        outputtxt = ''
        dish_number = 1
        for dish in self.dishes:
            if len(outputtxt) == 0:
                outputtxt = f'{dish_number}.{dish.format()}'
                dish_number +=1
            else:
                outputtxt = outputtxt + f'\n{dish_number}.{dish.format()}'
                dish_number +=1
        return outputtxt
    def add_dishes(self,*dish_number):
        for number in dish_number:
            self.receipt.add_dish(self.dishes[number-1])
        
    def get_total(self):
        return self.receipt.total()
    def place_order(self,client,test_phone_no,twil_phone_no):
        message = client.messages.create(
            to= test_phone_no,
            from_= twil_phone_no,
            body = f'Your order of:\n\n{self.get_total()}\n\n Will be ready in 35 minutes.'

        )
        return message.sid
