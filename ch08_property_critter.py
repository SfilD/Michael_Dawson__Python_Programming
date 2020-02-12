#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Зверюшка со свойствами
# Демонстрирует свойства

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой")
        else:
            self.__name = new_name
            print("Имя успешно изменено")

    def talk(self):
        print("Привет, меня зовут", self.name)


# Основная часть
crit = Critter("Шарик")
crit.talk()

print("Мою зверюшку зовут", end=" ")
print(crit.name)

print("Пробую изменить имя зверюшки на Мурзик")
crit.name = "Мурзик"
print("Мою зверюшку зовут", end=" ")
print(crit.name)

print("Пробую изменить имя зверюшки на пустую строку")
crit.name = ""
print("Мою зверюшку зовут", end=" ")
print(crit.name)
print("Имя успешно изменено")
