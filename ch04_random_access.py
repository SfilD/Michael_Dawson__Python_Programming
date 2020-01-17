#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Случайные буквы
# Демонстрирует индексацию строк
import random
word = "индекс"
print("В переменной word хранится слово ", word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])
