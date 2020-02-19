#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Бесполезные кнопки 2.0
# Демонстрирует создание класса в оконном приложении на основе tkinter
from tkinter import *

class Application(Frame):
    """GUI-приложение с тремя кнопками"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создаёт три бесполезные кнопки"""
        # первая кнопка
        self.bttn1 = Button(self, text = "Я ничего не делаю!")
        self.bttn1.grid()

        # вторая кнопка
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "И я тоже!")

        # третья кнопка
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "И я!"


# основная часть
root = Tk()
root.title("Бесполезные кнопки 2.0")
root.geometry("500x250")
app = Application(root)
root.mainloop()
