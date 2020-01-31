#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Классово верная зверюшка
# Демонстрирует атрибуты класса и статические методы

class Critter(object):
    """Виртуальный питомец"""
    total = 0
    @staticmethod
    def status():
        print("Всего зверюшек сейчас", Critter.total)

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1


# Основная часть
print("Нахожу значение атрибута класса Critter.total:", end=" ")
print(Critter.total)
print("Создаю зверюшек:")
Critter.status()
crit1 = Critter("Зверюшка 1")
Critter.status()
crit2 = Critter("Зверюшка 2")
Critter.status()
crit3 = Critter("Зверюшка 3")
Critter.status()
print("Обращаюсь к атрибуту класса через объект:", end=" ")
print(crit1.total)
