#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Рекорды
# Демонстрирует списочные методы
scores = []
choice = None

while choice != "0":
    print( """
Рекорды
0 - Выйти
1 - Показать рекорды
2 - Добавить рекорд
3 - Удалить рекорд
4 - Сортировать список """)

    choice = input("Ваш выбор: ")
    print()

    # выход (0)
    if choice == "0":
        print("До свидания.")

    # вывод лучших результатов на экран (1)
    elif choice == "1":
        print("Рекорды")
        for score in scores:
            print(score)

    # добавление рекорда (2)
    elif choice == "2":
        score = int(input("Впишите свой рекорд: "))
        scores.append(score)

    # удаление рекорда (3)
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
        else:
            print("Результат", score, "не содержится в списке рекордов.")

    # сортировка рекордов (4)
    elif choice == "4":
        scores.sort(reverse = True)

    # непонятный пользовательский ввод
    else:
        print("Извините, в меню нет такого пункта", choice)
