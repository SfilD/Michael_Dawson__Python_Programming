#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Доработка функции ask_number()
# для вызова с дополнительным параметром - кратностью (величиной шага)
# Шаг по-умолчанию - 1

def ask_number(question = "Введите число из диапазона от", low = 0, high = 100, multiplicity = 1):
    """Просит ввести число из диапазона"""
    text = question + " " + str(low) + " до " + str(high) + ", с шагом " + str(multiplicity) + ": "
    response = None
    while response not in range(low, high + 1, multiplicity):
        response = int(input(text))
    return response


# Программа
print(ask_number())
