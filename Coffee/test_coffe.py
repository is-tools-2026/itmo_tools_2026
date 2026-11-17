
import pytest
import coffee

from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
    MENU,
)


@pytest.mark.parametrize("drink, expected", [
    ("espresso", 150),
    ("capuccino", 250),
    ("latte", 280),
    ("americano", 200),
    ("tea", 120),
    ("hot_chocolate", 220),
])
def test_get_price_positive(drink, expected):
    assert get_price(drink) == expected


@pytest.mark.parametrize("quantity, price, expected", [
    (1, 150, 150),
    (2, 280, 560),
    (3, 120, 360),
    (0, 200, 0),
    (5, 250, 1250),
])
def test_calculate_order_total_positive(quantity, price, expected):
    assert calculate_order_total(quantity, price) == expected


def test_get_most_expensive_drink_positive():
    assert get_most_expensive_drink() == ("latte", 280)


@pytest.mark.parametrize("length", [8, 9, 12, 20])
def test_generate_wifi_password_positive(length):
    password = generate_wifi_password(length)

    assert isinstance(password, str)
    assert len(password) == length
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert password.isascii()
    assert password.isalnum()


@pytest.mark.parametrize("drink", [
    "espresso",
    "capuccino",
    "latte",
    "americano",
    "tea",
    "hot_chocolate",
])
def test_format_receipt_positive(drink):
    receipt = format_receipt(drink, 1)

    assert isinstance(receipt, str)
    assert "Чек CampusCoffee" in receipt
    assert f"Напиток: {drink}" in receipt
    assert "Количество: 1" in receipt
    assert f"Итого: {MENU[drink]} руб." in receipt


def test_get_price_returns_int():
    assert isinstance(get_price("latte"), int)


def test_calculate_order_total_returns_int():
    assert isinstance(calculate_order_total(2, 100), int)


def test_get_most_expensive_drink_returns_tuple():
    assert isinstance(get_most_expensive_drink(), tuple)


def test_generate_wifi_password_returns_string():
    assert isinstance(generate_wifi_password(8), str)


def test_format_receipt_returns_string():
    assert isinstance(format_receipt("latte", 1), str)


def test_zero_quantity():
    assert calculate_order_total(0, 280) == 0


@pytest.mark.parametrize("drink", [
    "",
    "unknown_drink",
    None,
])
def test_get_price_invalid_drink(drink):
    with pytest.raises(ValueError):
        get_price(drink)


def test_calculate_order_total_invalid_quantity_type():
    with pytest.raises(ValueError):
        calculate_order_total("2", 100)


def test_calculate_order_total_invalid_price_type():
    with pytest.raises(ValueError):
        calculate_order_total(2, "100")


def test_calculate_order_total_negative_values():
    with pytest.raises(ValueError):
        calculate_order_total(-1, 100)

    with pytest.raises(ValueError):
        calculate_order_total(1, -100)


def test_get_most_expensive_drink_empty_menu(monkeypatch):
    monkeypatch.setattr(coffee, "MENU", {})

    with pytest.raises(ValueError):
        get_most_expensive_drink()


def test_generate_wifi_password_too_short():
    with pytest.raises(ValueError):
        generate_wifi_password(7)


def test_generate_wifi_password_invalid_type():
    with pytest.raises(ValueError):
        generate_wifi_password("eight")


def test_format_receipt_invalid_drink_type():
    with pytest.raises(ValueError):
        format_receipt(123, 1)


def test_format_receipt_unknown_drink():
    with pytest.raises(ValueError):
        format_receipt("unknown_drink", 1)


def test_format_receipt_invalid_quantity_type():
    with pytest.raises(ValueError):
        format_receipt("latte", "two")


def test_format_receipt_negative_quantity():
    with pytest.raises(ValueError):
        format_receipt("latte", -1)
