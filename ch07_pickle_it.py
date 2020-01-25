#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Законсервируем
# Демонстрирует консервацию данных и доступ к ним через интерфейс полки

import pickle, shelve

print("Консервация списков.")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Главпродукт", "Чумак", "Бондюэль"]
# Открытие на запись нового файла
f = open("ch07_pickles_1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)

print("Расконсервация списков.")
f = open("ch07_pickles_1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

print("Помещение списков на полку.")
s = shelve.open("ch07_pickles_2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубиками", "соломкой"]
s["brand"] = ["Главпродукт", "Чумак", "Бондюэль"]
s.sync()    # убедимся, что данные записаны

print("Извлечение списков из файла полки в обратном порядке:")
print("Торговые марки: ", s["brand"])
print("Формы: ", s["shape"])
print("Виды овощей: ", s["variety"])
s.close()
