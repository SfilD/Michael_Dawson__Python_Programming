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

    def eat(self, food = 4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = -1
        self.__pass_time()

    def play(self, fun = 4):
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = -1
        self.__pass_time()


def main():
    crit_name = input("Как вы назовёте свою зверюшку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
Моя зверюшка
0 - Выйти
1 - Узнать о самочувствии зверюшки
2 - Покормить зверюшку
3 - Поиграть со зверюшкой""")
        choice = input("Ваш выбор: ")
        # выход
        if choice == "0":
            print("До свидания")
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        # кормление зверюшки
        elif choice == "2":
            eat_choice = None
            while eat_choice != "0":
                print \
                ("""
0 - Выйти
1 - Еда на 1 балл
2 - Еда на 2 балла
3 - Еда на 3 балла
4 - Еда на 4 балла""")
                eat_choice = input("Выберите еду для зверюшки: ")
                # выход
                if eat_choice == "0":
                    print("Передумал кормить зверюшку")
                # выбор еды
                elif eat_choice == "1" or eat_choice == "2" or eat_choice == "3" or eat_choice == "4":
                    crit.eat(int(eat_choice))
                    eat_choice = "0"

        # игра со зверюшкой
        elif choice == "3":
            play_choice = None
            while play_choice != "0":
                print \
                    ("""
0 - Выйти
1 - Игра на 1 минуту
2 - Игра на 2 минуты
3 - Игра на 3 минуты
4 - Игра на 4 минуты""")
                play_choice = input("Выберите игру для зверюшки: ")
                # выход
                if play_choice == "0":
                    print("Передумал играть со зверюшкой")
                # выбор игры
                elif play_choice == "1" or play_choice == "2" or play_choice == "3" or play_choice == "4":
                    crit.play(int(play_choice))
                    play_choice = "0"

        # вывод служебной информации об объекте
        elif choice == "21":
            print(crit)

        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


main()
