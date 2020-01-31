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
        print("Привет! Меня зовут ", self.name, ".", sep="")


# Основная часть
crit1 = Critter("Бобик")
crit1.talk()

crit2 = Critter("Мурзик")
crit2.talk()

crit3 = Critter("Соня")
crit3.talk()

print("Вывод объекта crit3 на экран:")
print(crit3)
print("Непосредственный доступ к атрибуту crit3.name:")
print(crit3.name)
