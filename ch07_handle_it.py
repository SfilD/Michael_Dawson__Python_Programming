#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try / except

# обработка исключения определённого типа
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Похоже, это не число!")
else:
    print("Вы ввели число", num)

# обработка исключений нескольких разных типов
print()
for value in (None, "Привет!", "77", 21):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")

print()
for value in (None, "Привет!", 21, "77.0"):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError as e:
        print("Я умею преобразовывать только строки, составленные из цифр!")
        print("Интерпретатор говорит нам:")
        print(e)
