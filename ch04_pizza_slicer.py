#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Резчик пиццы
# Демонстрирует срезы строк
word = "пицца"
memo = \
"""
Памятка
0   1   2   3   4   5
+---+---+---+---+---+
| п | и | ц | ц | а |
+---+---+---+---+---+
-5  -4  -3  -2  -1
"""
#print(memo)
print("Введите начальный и конечный индексы для того среза 'пиццы', который хотите получить.")
print("Для выхода нажмите Enter, не вводя начальную позицию.")
start = None
while start != "":
    print(memo)
    start = input("Начальная позиция: ")
    if start:
        start = int(start)
        finish = int(input("Конечная позиция: "))
        print("Срез word[", start, ":", finish, "] выглядит как", sep = "", end = " ")
        print(word[start:finish])
