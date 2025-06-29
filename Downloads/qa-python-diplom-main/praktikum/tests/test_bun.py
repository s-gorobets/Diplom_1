import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize('name, price', [
    ("white", 555.55),
    ("black", 200.9),
    ("orange", 100.0)
])

def test_get_bun_params(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name and bun.get_price() == price