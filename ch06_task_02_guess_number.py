#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Доработка игры "Отгадай число" из главы 3
# с использованием функции ask_number()

# Отгадай число
# Компьютер выбирает случайное число в диапазоне от 1 до 100
# Игрок пытается отгадать это число и компьютер говорит
# Предположение больше/меньше, чем загаданное число
# Или попало в точку

low = 0
high = 100


def ask_number(question, low, high):
    """Просит ввести число из диапазона от low до high"""

    text = question + " " + str(low) + " до " + str(high) + ": "
    response = None
    while response not in range(low, high + 1):
        response = int(input(text))
    return response


def main(low, high):
    import random
    print("\tДобро пожаловать в игру 'Отгадай число'!")
    print("\nЯ загадал натуральное число из диапазона от", low, "до", high)
    print("Постарайся отгадать его за минимальное число попыток.\n")

    the_number = random.randint(low, high)
    guess = ask_number("Введите число в диапазоне от", low, high)
    tries = 1
    # цикл отгадывания
    while guess != the_number:
        if guess > the_number:
            print("Меньше...")
            high = guess - 1
        else:
            print("Больше...")
            low = guess + 1
        guess = ask_number("Введите число в диапазоне от", low, high)
        tries += 1
    print("Вам удалось отгадать число! Это в самом деле %d." % the_number)
    print("Вы затратили на отгадывание всего лишь %d попыток." % tries)


# Основная программа
main(low, high)
