#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Отгадай число
#
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# и пытается отгадать это число и компьютер говорит
# предположение больше/меньше, чем загаданное число
# или попало в точку
import random
print("Добро пожаловать в игру 'Отгадай число'!")
print("Я загадал натуральное число из диапазона от 1 до 100.")
print("Постараюсь отгадать его за минимальное число попыток.")
# начальные значения
first_num, last_num = 1, 100
number = random.randint(first_num, last_num)
tries = 1
# цикл отгадывания
while True:
    guess = (first_num + last_num) // 2
    print("Попытка #%d" % tries)
    print("Предполагаю, что это число %d" % guess)
    if guess > number:
        print("Меньше...")
        last_num = guess
    elif guess < number:
        print("Больше...")
        first_num = guess
    elif guess == number:
        print("Вам удалось отгадать число! Это в самом деле %d." % number)
        print("вы затратили на отгадывание всего лишь %d попыток." % tries)
        break
    tries += 1
