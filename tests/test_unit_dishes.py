from lib.Dishes import *

def test_init_of_Dishes():
    test_dish = Dishes('Taco',2.25)
    assert test_dish.name == 'Taco'
    assert test_dish.price == 2.25

def test_format_returns_correct_format():
    test_dish = Dishes('Taco',2.25)
    assert test_dish.format() == 'Taco: £2.25'

def test_get_price_returns_correct_float():
    test_dish = Dishes('Taco',2.25)
    assert test_dish.get_price() == 2.25