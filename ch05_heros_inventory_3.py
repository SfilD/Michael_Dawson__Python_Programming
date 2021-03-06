#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Арсенал героя 3.0
# Демонстрирует работу со списками

# создадим список с несколькими элементами и выведем его с помощью цикла for
inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("Итак, в вашем арсенале:")
for item in inventory:
    print(item)

# найдём длину списка
print("Сейчас в вашем распоряжении", len(inventory), "предмет(а/ов).")

# проверка на принадлежность списку с помощью in
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

# соединим два списка
chest = ["золото", "драгоценные камни"]
print("Вы нашли ларец. Вот что в нём есть:")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("Теперь в вашем распоряжении:")
print(inventory)

# присваиваем значение элементу по индексу
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Теперь ваш арсенал содержит следующие предметы:")
print(inventory)

# приписываем значение элементам по срезу индексов
print("За золото и драгоценные камни вы купили магический кристалл, способный предсказывать будущее.")
inventory[4:6] = ["магический кристалл"]
print("Теперь в вашем распоряжении:")
print(inventory)

# удаляем элемент
print("В тяжёлом бою был раздроблен ваш щит.")
del inventory[2]
print("Вот что осталось в арсенале:")
print(inventory)

# удаляем срез
print("Воры лишили вас арбалета и кольчуги.")
del inventory[:2]
print("В арсенале теперь только:")
print(inventory)
