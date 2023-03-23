from utils.main import Items
import pytest

item = Items('phone', 10000, 2)


def test_init():
    assert item.name == 'phone'
    assert item.price == 10000
    assert item.amount == 2


def test_calculate_total_price():
    assert item.calculate_total_price() == 20000


def test_apply_discount():
    assert item.apply_discount() == 8500.0


def test_name():
    name = "смартфон"
    assert name == "смартфон"


def test_instantiate_from_csv():
    assert len(Items.all) == 5

def test_repr():
    assert item.__repr__() == 'phone, 8500.0, 2'


def test_str():
    assert item.__str__() == 'phone'



