#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Payer(object):
    """Игрок в экшен-игре"""
    def blast(self, enemy):
        print("Игрок стреляет во врага")
        enemy.die()


class Alien(object):
    """Враждебный пришелец-инопланетянин в экшен-игре"""
    def die(self):
        print("Пришелец умирает")


# Основная часть программы
print("Гибель пришельца")
hero = Payer()
invader = Alien()
hero.blast(invader)
