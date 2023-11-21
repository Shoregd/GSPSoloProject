As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

--- Class identification ---

    *OrderMeal - Will allow the user to see a list of dishes and their corresponding prices. They will be able to add a dish(Possibly multiple) to a pending order. They will be able to view their total order. They will be able to complete their order and receive a message for estimated delivery time.
    *Dishes - Will contain the dish name and the corresponding price. It will be able to return just the price. It will be able to format the dish information to:
     "<Dish Name> : <Dish Price>"
    *Receipt - Will hold the list of ordered dishes. Will be able to format the reciept to list the dishes, their corresponding prices and the grand total.
    


--- Class Breakdowns ---

    *OrderMeal
        *__init__:
            *Dishes - List of dishes
            *Reciept - Single instance of receipt
        *list_dishes():
        *add_dishes():
        *get_total():
        *place_order():

    *Dishes
        *__init__:
            * Dish Name
            * Dish Price
        *format():
        *get_price():
    *Receipt
        *__init__:
            *Dishes
        *add_dish():
        *total():




