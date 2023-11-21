from lib.Dishes import *
from lib.OrderMeal import *
from lib.Receipt import *


 
test_dish1 = Dishes('Taco',2.25)
test_dish2 = Dishes('Nacho',1.25)
test_dish3 = Dishes('Enchilada',2.75)
test_dish4 = Dishes('Burrito',4.5)
test_dish5 = Dishes('Chips',1.80)
test_dish6 = Dishes('Soft Drink',1.25)


def test_list_dishes():
    test_receipt = Receipt()
    
    test_meal = OrderMeal(test_receipt,test_dish1)
    assert test_meal.list_dishes() == f'1.{test_dish1.name}: £{test_dish1.price}'
def test_listing_multiple_dishes():
    test_receipt = Receipt()
    test_meal = OrderMeal(test_receipt,test_dish1,test_dish2,test_dish3,test_dish4,test_dish5,test_dish6)
    assert test_meal.list_dishes() == f'1.{test_dish1.format()}\n2.{test_dish2.format()}\n3.{test_dish3.format()}\n4.{test_dish4.format()}\n5.{test_dish5.format()}\n6.{test_dish6.format()}'
def test_add_single_dish():
    test_receipt = Receipt()
    test_meal = OrderMeal(test_receipt,test_dish1)
    test_meal.add_dishes(1)
    assert test_meal.receipt.dishes == [test_dish1]
def test_add_multiple_dishes():
    test_receipt = Receipt()
    test_meal = OrderMeal(test_receipt,test_dish1,test_dish2,test_dish3,test_dish4,test_dish5,test_dish6)
    test_meal.add_dishes(1,3,5)
    assert test_meal.receipt.dishes == [test_dish1,test_dish3,test_dish5]
def test_get_total_single_dish():
    test_receipt = Receipt()
    test_meal = OrderMeal(test_receipt,test_dish1)
    test_meal.add_dishes(1)
    assert test_meal.get_total() == f'{test_dish1.format()}\n\n\n    Total: £2.25'
def test_get_total_multiple_dishes():
    test_receipt = Receipt()
    test_meal = OrderMeal(test_receipt,test_dish1,test_dish2,test_dish3,test_dish4,test_dish5,test_dish6)
    test_meal.add_dishes(1,3,5)
    assert test_meal.get_total()== f'{test_dish1.format()}\n{test_dish3.format()}\n{test_dish5.format()}\n\n\n    Total: £6.80'


   
