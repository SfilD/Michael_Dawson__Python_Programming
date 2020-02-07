#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger # голод
        self.boredom = boredom # уныние

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "Имя объекта: " + self.name + "\n"
        rep += "Уровень голода: " + str(self.hunger) + "\n"
        rep += "Уровень уныния: " + str(self.boredom) + "\n"
        return rep

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать, чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood)
        self.__pass_time()

    def eat(self, food):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = -1
        self.__pass_time()

    def play(self, fun):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = -1
        self.__pass_time()


def main():
    import random
    crit_name = ["Sonya", "Murrr'ka", "Vasssiliy"]
    crit_len = len(crit_name)
    crit = []
    span = 6 # диапазон кормления/игры от 0 до span исключительно
    for i in range(crit_len):
        crit.append(Critter(crit_name[i]))

    choice = None
    while choice != "0":
        print \
        ("""
Мои зверюшки
0 - Выйти
1 - Узнать о самочувствии зверюшек
2 - Покормить зверюшек
3 - Поиграть со зверюшками""")
        choice = input("Ваш выбор: ")
        # выход
        if choice == "0":
            print("До свидания")
        # беседа со зверюшками
        elif choice == "1":
            for i in range(crit_len):
                crit[i].talk()
        # кормление зверюшек
        elif choice == "2":
            for i in range(crit_len):
                crit[i].eat(random.randrange(span))

        # игра со зверюшками
        elif choice == "3":
            for i in range(crit_len):
                crit[i].play(random.randrange(span))

        # вывод служебной информации об объекте
        elif choice == "21":
            for i in range(crit_len):
                print(crit[i])

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


main()
