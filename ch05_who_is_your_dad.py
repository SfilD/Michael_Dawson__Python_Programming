#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Программа "Моя семья"

# Пользователь вводит имя человека,
# программа называет его отца, мать,
# дедушку и бабушку.
# Имеется возможность искать,
# добавлять и удалять информацию об
# имеющихся родственниках.

dict_family = {}
choice = None
while choice != "0":
    print('''Программа "Моя семья":
0 - Выйти
1 - Искать в словаре
2 - Добавить в словарь
3 - Удалить информацию''')

    choice = input("Ваш выбор: ")
    print()

    # 0 - Выйти
    if choice == "0":
        print("До свидания")

    # 1 - Искать в словаре
    elif choice == "1":
        fio_child = input("Введите полное ФИО для поиска по словарю: ")
        if fio_child in dict_family:
            fio_father, fio_mother, fio_grand_dad, fio_grand_mother = dict_family[fio_child]
            print(fio_child)
            print("Отец: ", fio_father)
            print("Мать: ", fio_mother)
            print("Дедушка: ", fio_grand_dad)
            print("Бабушка: ", fio_grand_mother)
        else:
            print("Увы,", fio_child, "мне не знаком")

    # 2 - Добавить в словарь
    elif choice == "2":
        fio_child = input("Введите полное ФИО для добавления в словарь: ")
        if fio_child not in dict_family:
            fio_father = input("Введите полное ФИО отца: ")
            fio_mother = input("Введите полное ФИО матери: ")
            fio_grand_dad = input("Введите полное ФИО дедушки: ")
            fio_grand_mother = input("Введите полное ФИО бабушки: ")
            dict_family[fio_child] = [fio_father, fio_mother, fio_grand_dad, fio_grand_mother]
            print("Добавлена новая запись")
        else:
            print("Такая запись уже есть!")

    # 3 - Удалить термин
    elif choice == "3":
        fio_child = input("Введите полное ФИО для удаления из словаря: ")
        if fio_child in dict_family:
            del dict_family[fio_child]
            print("Запись удалена")
        else:
            print("Удаление невозможно, такой записи не существует")

    # Неправильный пользовательский ввод
    else:
        print("Извините, в меню нет пункта", choice)
