#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Программа "Генератор персонажей" для ролевой игры
# Пользователю предоставлено 30 пунктов, которые распределяются между 4 характеристиками: Сила, Здоровье, Мудрость и
# Ловкость. Пользователь может не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик,
# которым он решит присвоить другие значения.

# Объявление списков:
pool = ['Пункт_01', 'Пункт_02', 'Пункт_03', 'Пункт_04', 'Пункт_05',
        'Пункт_06', 'Пункт_07', 'Пункт_08', 'Пункт_09', 'Пункт_10',
        'Пункт_11', 'Пункт_12', 'Пункт_13', 'Пункт_14', 'Пункт_15',
        'Пункт_16', 'Пункт_17', 'Пункт_18', 'Пункт_19', 'Пункт_20',
        'Пункт_21', 'Пункт_22', 'Пункт_23', 'Пункт_24', 'Пункт_25',
        'Пункт_26', 'Пункт_27', 'Пункт_28', 'Пункт_29', 'Пункт_30']
specifications = [[], [], [], []]
name_spec = ("Сила", "Здоровье", "Мудрость", "Ловкость")

choice = None
while choice != "0":
    print('''
Программа "Генератор персонажей"
0 - Выйти
1 - Добавить пункт в характеристику
2 - Удалить пункт из характеристики''')

    choice = input("Выберите пункт меню: ")
    # 0 - Выйти
    if choice == "0":
        print("До свидания")

    # 1 - Добавить пункт в характеристику
    elif choice == "1":
        count: int = 1
        for i in pool:
            print(count, i)
            count += 1
        pool_num_choice = int(input("Введите номер выбранного пункта из общего списка: "))
        while pool_num_choice < 1 or pool_num_choice > count - 1:
            pool_num_choice = int(input("Введите номер выбранного пункта из общего списка: "))
        for i in range(len(name_spec)):
            print(i + 1, "-", name_spec[i])
        spec_num_choice = int(input("Введите номер изменяемой характеристики: "))
        while spec_num_choice < 1 or spec_num_choice > i + 1:
            spec_num_choice = int(input("Введите номер изменяемой характеристики: "))
        specifications[spec_num_choice - 1].append(pool.pop(pool_num_choice - 1))
        print("В наличии:")
        for i in range(len(name_spec)):
            print(i + 1, "-", name_spec[i], sep=" ")
            for j in range(len(specifications[i])):
                print(specifications[i][j], sep=" ")

    # 2 - Удалить пункт из характеристики
    elif choice == "2":
        print("В наличии:")
        for i in range(len(name_spec)):
            print(i + 1, "-", name_spec[i], sep=" ")
            for j in range(len(specifications[i])):
                print(specifications[i][j], sep=" ")
        spec_num_choice = int(input("Введите номер изменяемой характеристики: "))
        while spec_num_choice < 1 or spec_num_choice > i + 1:
            spec_num_choice = int(input("Введите номер изменяемой характеристики: "))
        if specifications[spec_num_choice - 1]:
            print(name_spec[spec_num_choice - 1])
            count = 1
            for i in range(len(specifications[spec_num_choice - 1])):
                print(count, specifications[spec_num_choice - 1][i])
                count += 1
            pool_num_choice = int(input("Введите номер выбранного пункта из списка: "))
            while pool_num_choice < 1 or pool_num_choice > count - 1:
                pool_num_choice = int(input("Введите номер выбранного пункта из списка: "))
            pool.append(specifications[spec_num_choice - 1].pop(pool_num_choice - 1))
        else:
            print("Список", name_spec[spec_num_choice - 1], "пустой")
