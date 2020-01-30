#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Просто зверюшка
# Демонстрирует простейшие класс и объект

class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет! Я - зверюшка, экземпляр класса Critter.")


# Основная часть
crit = Critter()
crit.talk()
