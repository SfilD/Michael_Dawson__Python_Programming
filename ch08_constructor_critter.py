#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Зверюшка с конструктором
# Демонстрирует метод-конструктор

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет новая зверюшка!")

    def talk(self):
        print("Привет! Я - зверюшка, экземпляр класса Critter.")


# Основная часть
crit1 = Critter()
crit2 = Critter()
crit3 = Critter()
crit1.talk()
crit2.talk()
crit3.talk()
