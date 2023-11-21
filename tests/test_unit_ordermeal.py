from lib.OrderMeal import *
from unittest.mock import Mock
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()
account_sid = 'TestSID'
auth_token = 'TESTAUTHTOKEN'
twil_phone_no = 'TESTPHONENUMBER'
test_phone_no = 'TESTPHONENUMBER'
client = Mock()

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
test_receipt1 = Mock()
test_receipt1.dishes = []
test_receipt1.add_dish(test_dish1).return_value = test_receipt1.dishes.append(test_dish1)
test_receipt1.total.return_value = f'{test_dish1.format()}\n\n\n    Total: £2.25'
test_receipt2 = Mock()
test_receipt2.dishes = [test_dish1,test_dish2,test_dish3]
test_receipt2.total.return_value = f'{test_dish1.format()}\n{test_dish2.format()}\n{test_dish3.format()}\n\n\n    Total: £6.25'

'''
Test OrderMeal using mocks
'''

def test_init_with_single_dish():
    test_mealorder = OrderMeal(test_receipt1,test_dish1)
    assert test_mealorder.dishes == [test_dish1] 

def test_init_with_multidish():
    test_mealorder = OrderMeal(test_receipt2,test_dish1,test_dish2,test_dish3)
    assert test_mealorder.dishes == [test_dish1,test_dish2,test_dish3]

def test_list_dishes_single_dish():
    test_mealorder = OrderMeal(test_receipt1,test_dish1)
    assert test_mealorder.list_dishes() == f'1.{test_dish1.format()}'

def test_multiple_dishes_multiline_dishes():
    test_mealorder = OrderMeal(test_receipt2,test_dish1,test_dish2,test_dish3)
    assert test_mealorder.list_dishes() == f'1.{test_dish1.format()}\n2.{test_dish2.format()}\n3.{test_dish3.format()}'

def test_add_single_dish():
    test_mealorder = OrderMeal(test_receipt1,test_dish1)
    test_mealorder.add_dishes(1)
    assert test_mealorder.receipt.dishes == [test_dish1]

def test_add_multiple_dishes():
    test_mealorder = OrderMeal(test_receipt1,test_dish1)
    test_mealorder.add_dishes(1,1,1,1)
    test_receipt1.add_dish(test_dish1).return_value = test_receipt1.dishes.append(test_dish1)
    test_receipt1.add_dish(test_dish1).return_value = test_receipt1.dishes.append(test_dish1)
    test_receipt1.add_dish(test_dish1).return_value = test_receipt1.dishes.append(test_dish1)
    assert test_mealorder.receipt.dishes == [test_dish1,test_dish1,test_dish1,test_dish1]

def test_get_total_single_item():
    test_mealorder = OrderMeal(test_receipt1,test_dish1)
    test_mealorder.add_dishes(1)
    assert test_mealorder.get_total() == f'{test_dish1.format()}\n\n\n    Total: £2.25'

def test_total_multiple_dishes():
    test_mealorder = OrderMeal(test_receipt2,test_dish1,test_dish2,test_dish3)
    test_mealorder.add_dishes(1,2,3)
    assert test_mealorder.get_total() == f'{test_dish1.format()}\n{test_dish2.format()}\n{test_dish3.format()}\n\n\n    Total: £6.25'

def test_place_order_with_single_dish():
    test_mealorder = OrderMeal(test_receipt1,test_dish1)
    test_mealorder.add_dishes(1)
    client.messages.create.return_value.sid = 'SM87105da94bff44b999e4e6eb90d8eb6a'
    assert test_mealorder.place_order(client,test_phone_no,twil_phone_no) == 'SM87105da94bff44b999e4e6eb90d8eb6a'
    