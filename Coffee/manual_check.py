from coffee import (
    get_price,
    calculate_order_total,
    get_most_expensive_drink,
    generate_wifi_password,
    format_receipt,
)

print("Цена эспрессо:")
print(get_price("espresso"))

print("\nСтоимость двух напитков по 150 рублей:")
print(calculate_order_total(2, 150))

print("\nСамый дорогой напиток:")
print(get_most_expensive_drink())

print("\nПароль Wi-Fi:")
password = generate_wifi_password()
print(password)
print("Длина:", len(password))

print("\nЧек на два латте:")
print(format_receipt("latte", 2))