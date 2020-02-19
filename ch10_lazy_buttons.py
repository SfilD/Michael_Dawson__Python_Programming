#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Бесполезные кнопки
# Демонстрирует создание кнопок
from tkinter import *

# создание базового окна
root = Tk()
root.title("Бесполезные кнопки")
root.geometry("500x250")

# внутри окна создаётся рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание кнопки внутри рамки
bttn_1 = Button(app, text = "lll")
# bttn_1.configure(text = "xxx") # переопределение текста
bttn_1.grid()

# создание второй кнопки внутри рамки
bttn_2 = Button(app)
bttn_2.grid()
bttn_2.configure(text = "www")

# создание третьей кнопки внутри рамки
bttn_3 = Button(app)
bttn_3.grid()
bttn_3["text"] = "---"

# старт событийного цикла
root.mainloop()
