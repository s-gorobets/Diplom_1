import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize('name', [
    "white",
    "чёрный",
    "white123",
    "white_bun!",
    "",
])
def test_get_bun_name(name):
    bun = Bun(name, 100.0)
    assert bun.get_name() == name


@pytest.mark.parametrize('price', [
    0.0,
    0.01,
    100.0,
    9999999.99,
])
def test_get_bun_price(price):
    bun = Bun('Test_bun', price)
    assert bun.get_price() == price
