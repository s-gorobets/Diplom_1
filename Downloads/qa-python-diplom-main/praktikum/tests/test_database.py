import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize('index, expected_name, expected_price',[
    (0, "black bun", 100),
    (1, "white bun", 200),
    (2, "red bun", 300)
])

def test_available_buns(index, expected_name, expected_price):
    db = Database()
    bun = db.available_buns()[index]
    assert bun.get_name() == expected_name
    assert bun.get_price() == expected_price

@pytest.mark.parametrize('index, expected_type, expected_name, expected_price',[
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
])

def test_available_ingredients(index, expected_type, expected_name, expected_price):
    db = Database()
    ingrident = db.available_ingredients()[index]
    assert ingrident.get_type() == expected_type
    assert ingrident.get_name() == expected_name
    assert ingrident.get_price() == expected_price
