from unittest.mock import Mock
from lib.Receipt import *
from lib.Dishes import *
test_dish1 = Mock()
test_dish2 = Mock()
test_dish3 = Mock()

test_dish1.name = 'Taco'
test_dish1.price = 2.25
test_dish1.format.return_value = 'Taco: £2.25'
test_dish1.get_price.return_value = 2.25
test_dish2.name = 'Nacho'
test_dish2.price = 1.25
test_dish2.get_price.return_value = 1.25
test_dish2.format.return_value = 'Nacho: £1.25'
test_dish3.name = 'Enchilada'
test_dish3.price = 2.75
test_dish3.format.return_value = 'Enchilada: £2.75'
test_dish3.get_price.return_value = 2.75

test_dish4 = Dishes('Burrito',4.5)
test_dish5 = Dishes('Chips',1.80)
test_dish6 = Dishes('Soft Drink',1.25)

'''
Mock Tests
'''
def test_init_of_receipt():
    test_receipt = Receipt()
    assert test_receipt.dishes == []

def test_add_dish_updates_dish_list():
    test_receipt = Receipt()
    test_receipt.add_dish(test_dish1)
    assert test_receipt.dishes == [test_dish1]

def test_add_multiple_dishes():
    test_receipt = Receipt()
    test_receipt.add_dish(test_dish1)
    test_receipt.add_dish(test_dish3)
    test_receipt.add_dish(test_dish2)
    test_receipt.add_dish(test_dish1)
    assert test_receipt.dishes == [test_dish1,test_dish3,test_dish2,test_dish1]

def test_total_single_dish():
    test_receipt = Receipt()
    test_receipt.add_dish(test_dish1)
    assert test_receipt.total() == f'{test_dish1.format()}\n\n\n    Total: £2.25'

def test_total_multi_dish():
    test_receipt = Receipt()
    test_receipt.add_dish(test_dish1)
    test_receipt.add_dish(test_dish2)
    test_receipt.add_dish(test_dish3)
    test_receipt.add_dish(test_dish1)
    assert test_receipt.total() == f'{test_dish1.format()}\n{test_dish2.format()}\n{test_dish3.format()}\n{test_dish1.format()}\n\n\n    Total: £8.50'

'''
Tests with Dishes Class.
'''

def test_add_dishes_with_dishes_class():
    test_receipt = Receipt()
    test_receipt.add_dish(test_dish6)
    test_receipt.add_dish(test_dish5)
    test_receipt.add_dish(test_dish4)
    assert test_receipt.dishes == [test_dish6,test_dish5,test_dish4]

def test_total_returns_with_multiple_dish_classes():
    test_receipt = Receipt()
    test_receipt.add_dish(test_dish4)
    test_receipt.add_dish(test_dish5)
    test_receipt.add_dish(test_dish6)
    test_receipt.add_dish(test_dish4)
    assert test_receipt.total() == f'{test_dish4.format()}\n{test_dish5.format()}\n{test_dish6.format()}\n{test_dish4.format()}\n\n\n    Total: £12.05'
