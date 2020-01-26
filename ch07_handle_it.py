#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try / except

# обработка исключения определённого типа
try:
    num = float(input("Введите число: "))
    print(num)
except ValueError:
    print("Похоже, это не число!")

# обработка исключений нескольких разных типов
print()
for value in (None, "Привет!", "77", 21):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже, это не число!")
