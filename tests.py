import pytest
from main import *


def test_init():
    item = Items('phone', 10000, 1)
    assert item.product == 'phone'
    assert item.price == 10000
    assert item.amount == 1


def test_calculate_total_price():
    assert calculate_total_price(["laptop", 50000, 1]) == 50000
