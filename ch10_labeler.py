#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Это я, метка
# Демонстрирует применение меток
from tkinter import *

# создание базового окна
root = Tk()
root.title("Это я, метка")
root.geometry("160x90")

# внутри окна создаётся рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание метки внутри рамки
lbl = Label(app, text = "Вот она я!")
lbl.grid()

# старт событийного цикла
root.mainloop()
