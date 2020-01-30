#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Зверюшка с атрибутами
# Демонстрирует создание атрибутов объекта и доступ к ним

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name
        return rep

    def talk(self):
        print("Привет! Меня зовут", self.name)


# Основная часть
crit1 = Critter("Бобик")
crit1.talk()

crit2 = Critter("Мурзик")
crit2.talk()

print("Вывод объекта crit1 на экран:")
print(crit1)
print("Непосредственный доступ к атрибуту crit1.name:")
print(crit1.name)
