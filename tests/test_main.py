from main import *

item = Items('phone', 10000, 2)


def test_init():
    assert item.product == 'phone'
    assert item.price == 10000
    assert item.amount == 2


def test_calculate_total_price():
    assert item.calculate_total_price() == 20000

def test_apply_discount():
    assert item.apply_discount() == 8000.0
