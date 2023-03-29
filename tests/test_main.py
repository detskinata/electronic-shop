from utils.main import Items, Phone
import pytest

item = Items('phone', 10000, 2)


@pytest.fixture
def items():
    return Items("Смартфон", 1000, 20)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


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


def test_phone_init(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.amount == 5
    assert phone.number_of_sim == 2


def test_phone_number_of_sim():
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_repr(phone):
    assert Phone.__repr__(phone) == 'iPhone 14, 120000, 5, 2'
