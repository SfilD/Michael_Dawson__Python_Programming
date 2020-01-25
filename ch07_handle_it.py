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

