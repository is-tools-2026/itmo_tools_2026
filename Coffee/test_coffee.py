import unittest

from coffee import (
    MENU,
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt
)



class GetPriceTestCase(unittest.TestCase):
    def test_espresso_price(self):
        self.assertEqual(get_price("espresso"), 150)

    def test_capuccino_price(self):
        self.assertEqual(get_price("capuccino"), 250)

    def test_all_prices(self):
        for name in MENU:
            self.assertEqual(get_price(name), MENU[name])

    def test_price_is_int(self):
        self.assertTrue(type(get_price("latte")) == int)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            get_price("unknown_drink")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            get_price("")


    def test_number_name(self):
        with self.assertRaises(ValueError):
            get_price(5)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            get_price(None)

    def test_list_name(self):
        with self.assertRaises(ValueError):
            get_price(["latte"])

    def test_big_letter(self):
        with self.assertRaises(ValueError):
            get_price("Latte")


class CalculateOrderTotalTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(calculate_order_total(3, 280), 840)

    def test_zero_quantity(self):
        self.assertEqual(calculate_order_total(0, 280), 0)

    def test_big_order(self):
        self.assertEqual(calculate_order_total(1000, 250), 250000)

    def test_float_price(self):
        self.assertAlmostEqual(calculate_order_total(3, 99.9), 299.7)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_order_total(-1, 280)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, -280)

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, 0)

    def test_nan_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, float("nan"))

    def test_inf_price(self):
        with self.assertRaises(ValueError):
            calculate_order_total(2, float("inf"))


    def test_drink_name_instead_of_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total("latte", 5)

    def test_string_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total("3", 280)

    def test_float_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(2.5, 280)

    def test_none_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(None, 280)

    def test_bool_quantity(self):
        with self.assertRaises(TypeError):
            calculate_order_total(True, 280)

    def test_string_price(self):
        with self.assertRaises(TypeError):
            calculate_order_total(3, "280")

    def test_bool_price(self):
        with self.assertRaises(TypeError):
            calculate_order_total(3, False)


class GetMostExpensiveDrinkTestCase(unittest.TestCase):
    def test_latte(self):
        self.assertEqual(get_most_expensive_drink(), ("latte", 280))

    def test_max_price(self):
        name, price = get_most_expensive_drink()
        self.assertEqual(price, max(MENU.values()))

    def test_more_than_others(self):
        name, price = get_most_expensive_drink()
        for drink in MENU:
            self.assertTrue(price >= MENU[drink])

    def test_not_tea(self):
        name, price = get_most_expensive_drink()
        self.assertFalse(name == "tea")

    def test_other_menu(self):
        old = MENU.copy()
        MENU.clear()
        MENU["a"] = 10
        MENU["b"] = 30
        MENU["c"] = 20
        result = get_most_expensive_drink()
        MENU.clear()
        MENU.update(old)
        self.assertEqual(result, ("b", 30))

    def test_empty_menu(self):
        old = MENU.copy()
        MENU.clear()
        error = False
        try:
            get_most_expensive_drink()
        except ValueError:
            error = True
        MENU.update(old)
        self.assertTrue(error)

    def test_menu_not_changed(self):
        old = MENU.copy()
        get_most_expensive_drink()
        self.assertEqual(MENU, old)


class GenerateWifiPasswordTestCase(unittest.TestCase):
    def test_length_8(self):
        self.assertEqual(len(generate_wifi_password()), 8)

    def test_length_12(self):
        self.assertEqual(len(generate_wifi_password(12)), 12)

    def test_length_64(self):
        self.assertEqual(len(generate_wifi_password(64)), 64)


    def test_only_letters_and_digits(self):
        for i in range(300):
            self.assertRegex(generate_wifi_password(), "^[A-Za-z0-9]{8}$")

    def test_has_big_letter(self):
        for i in range(300):
            password = generate_wifi_password()
            self.assertRegex(password, "[A-Z]")

    def test_has_small_letter(self):
        for i in range(300):
            password = generate_wifi_password()
            self.assertRegex(password, "[a-z]")

    def test_has_digit(self):
        for i in range(300):
            password = generate_wifi_password()
            self.assertRegex(password, "[0-9]")

    def test_random(self):
        passwords = []
        for i in range(20):
            passwords.append(generate_wifi_password())
        self.assertTrue(len(set(passwords)) > 1)

    def test_length_7(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(7)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(-8)

    def test_too_long(self):
        with self.assertRaises(ValueError):
            generate_wifi_password(10000)

    def test_string_length(self):
        with self.assertRaises(TypeError):
            generate_wifi_password("8")

    def test_float_length(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(10.5)

    def test_none_length(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(None)

    def test_bool_length(self):
        with self.assertRaises(TypeError):
            generate_wifi_password(True)


class FormatReceiptTestCase(unittest.TestCase):
    def test_format(self):
        self.assertRegex(
            format_receipt("latte", 2),
            "^Чек CampusCoffee\nНапиток: latte\nКоличество: 2\nИтого: 560 руб\\.$"
        )

    def test_total(self):
        self.assertIn("Итого: 560 руб.", format_receipt("latte", 2))

    def test_quantity(self):
        self.assertIn("Количество: 3", format_receipt("tea", 3))

    def test_all_drinks(self):
        for name in MENU:
            self.assertIn("Итого: " + str(MENU[name] * 3) + " руб.", format_receipt(name, 3))

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            format_receipt("", 1)

    def test_none_name(self):
        with self.assertRaises(ValueError):
            format_receipt(None, 1)

    def test_unknown_drink(self):
        with self.assertRaises(ValueError):
            format_receipt("margarita", 1)

    def test_number_name(self):
        with self.assertRaises(ValueError):
            format_receipt(5, 1)

    def test_list_name(self):
        with self.assertRaises(ValueError):
            format_receipt(["latte"], 1)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", -1)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            format_receipt("latte", 0)

    def test_string_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", "2")

    def test_float_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", 2.5)

    def test_bool_quantity(self):
        with self.assertRaises(TypeError):
            format_receipt("latte", True)


if __name__ == "__main__":
    unittest.main()
