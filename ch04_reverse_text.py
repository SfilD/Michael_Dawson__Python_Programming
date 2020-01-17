#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reverse Text
# Программа принимает текст из пользовательского ввода
# и выводит его на экран наоборот

text = input("Введите текст: ")
for i in range(-1, -(len(text) + 1), -1):
    print(text[i], end = '')
print()
