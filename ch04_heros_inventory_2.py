#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Арсенал героя 2.0
# Демонстрирует работу с кортежами

# создадим кортеж с несколькими элементами и выведем его с помощью цикла for
inventory = ("меч", "кольчуга", "щит", "целебное снадобье")
print("Итак, в вашем арсенале:")
for item in inventory:
    print(item)

# найдём длину кортежа
print("Сейчас в вашем распоряжении", len(inventory), "предмет(а/ов).")

# проверка на принадлежность кортежу с помощью in
if "целебное снадобье" in inventory:
    print("Вы ещё поживёте и повоюете.")

# вывод одного элемента с определённым индексом
index = int(input("Введите индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])

# отобразим срез
start = int(input("Введите начальный индекс среза: "))
finish = int(input("Введите конечный индекс среза: "))
print("Срез inventory[", start, ":", finish, "] - это", sep = "", end = " ")
print(inventory[start:finish])

# соединим два кортежа
chest = ("золото", "драгоценные камни")
print("Вы нашли ларец. Вот что в нём есть:")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)

