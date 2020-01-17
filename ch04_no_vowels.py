#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Только согласные
# Демонстрирует создание новых строк из исходных с помощью цикла for
message = input("Введите текст: ")
new_message = ""
VOWELS = "eyuioaёуеыаоэяию"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Создана новая строка:", new_message)
print("\nВот ваш текст с изъятыми гласными буквами:", new_message)
