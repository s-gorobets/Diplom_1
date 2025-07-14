from praktikum.burger import Burger
from unittest.mock import Mock


def test_set_buns():
    burger = Burger()
    bun_mock = Mock()
    burger.set_buns(bun_mock)
    assert burger.bun == bun_mock

def test_add_ingridient():
    burger = Burger()
    ingridient_mock = Mock()
    burger.add_ingredient(ingridient_mock)
    assert ingridient_mock in burger.ingredients

def test_remove_ingridient():
    burger = Burger()
    ingridient_1 = Mock()
    ingridient_2 = Mock()
    burger.ingredients = [ingridient_2, ingridient_1]
    burger.remove_ingredient(0)
    assert burger.ingredients == [ingridient_1]

def test_move_ingridient():
    burder = Burger()
    ingridient_1 = Mock()
    ingridient_2 = Mock()
    burder.ingredients = [ingridient_2, ingridient_1]
    burder.move_ingredient(0, 1)
    assert burder.ingredients == [ingridient_1, ingridient_2]

def test_get_price():
    burger = Burger()

    bun_mock = Mock()
    bun_mock.get_price.return_value = 100.0

    ingridient_1 = Mock()
    ingridient_1.get_price.return_value = 34.6

    ingridient_2 = Mock()
    ingridient_2.get_price.return_value = 75.213

    burger.set_buns(bun_mock)
    burger.add_ingredient(ingridient_1)
    burger.add_ingredient(ingridient_2)

    expected_price = 100.0 * 2 + 34.6 + 75.213
    assert burger.get_price() == expected_price

def test_get_receipt():
    burger = Burger()
    bun_mock = Mock()
    bun_mock.get_name.return_value = 'Drakula'
    bun_mock.get_price.return_value = 50.0

    ingridient_1 = Mock()
    ingridient_1.get_type.return_value = 'Meat'
    ingridient_1.get_name.return_value = 'Beef'
    ingridient_1.get_price.return_value = 150.0

    ingridient_2 = Mock()
    ingridient_2.get_type.return_value = 'Filling'
    ingridient_2.get_name.return_value = 'Cheese'
    ingridient_2.get_price.return_value = 30.0

    burger.set_buns(bun_mock)
    burger.add_ingredient(ingridient_1)
    burger.add_ingredient(ingridient_2)

    expected_receipr = (
        "(==== Drakula ====)\n"
        "= meat Beef =\n"
        "= filling Cheese =\n"
        "(==== Drakula ====)\n"
        "\n"
        "Price: 280.0"
    )

    assert burger.get_receipt() == expected_receipr