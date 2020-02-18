#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Простая игра
# Демонстрирует импорт модулей
import ch09_games, random

print("Добро пожаловать в самую простую игру!")
again = None
while again != "n":
    players = []
    num = ch09_games.ask_number(question="Сколько игроков участвует? (2 - 5): ", low=2, high=6)

    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(100) + 1
        player = ch09_games.Player(name, score)
        players.append(player)

    print("Вот результаты игры:")
    for player in players:
        print(player)

    again = ch09_games.ask_yes_no("Хотите сыграть ещё раз? (y/n): ")
