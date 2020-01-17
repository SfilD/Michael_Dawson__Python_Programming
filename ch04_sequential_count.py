#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sequential Count
# Программа запрашивает начальное, конечное и
# шаг значений выводимой последовательности чисел

start = int(input("Введите начальное значение последовательности: "))
finish = int(input("Введите конечное значение : "))
step = int(input("Введите необходимый интервал между значениями : "))
for i in range(start, finish + 1, step):
    print(i, end = " ")
print()
