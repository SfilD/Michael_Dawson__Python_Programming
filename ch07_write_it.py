#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Запишем
# Демонстрирует запись в текстовый файл

print("Создаю текстовый файл методом write().")
text_file = open("ch07_write_it.txt", "w", encoding='utf-8')
text_file.write("Строка 1\n")
text_file.write("Это строка 2\n")
text_file.write("Этой строке достался номер 3\n")
text_file.close()

print("Читаю вновь созданный файл.")
text_file = open("ch07_write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()

print("Создаю текстовый файл методом writelines().")
text_file = open("ch07_write_it.txt", "w", encoding='utf-8')
