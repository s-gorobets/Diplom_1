import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize('ingredient_type, name, price',[
    ("sauce", "ketchup", 50.0),
    ("filling", "beef", 150.0),
    ("sauce", "mustard", 30.5),
    ("filling", "tofu", 99.9),
])

def test_get_ingridient_params(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price