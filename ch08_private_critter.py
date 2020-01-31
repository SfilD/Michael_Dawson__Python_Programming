#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name    # открытый атрибут
        self.__mood = mood  # закрытый атрибут


    def talk(self):
        print("Меня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood)

    def __private_method(self):
        print("Это закрытый метод")


    def public_method(self):
        print("Это открытый метод")
        self.__private_method()


# Основная часть
crit = Critter(name="Бобик", mood="прекрасно")
crit.talk()
crit.public_method()
