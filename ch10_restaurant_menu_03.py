#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Программа "Счёт, пожалуйста!"
# Показывает пользователю несложное ресторанное меню с блюдами и ценами,
# принимает заказ и выводит на экран сумму счёта
from tkinter import *

class Application(Frame):
    """GUI-приложение, позволяющее выбрать любимые блюда"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создаёт элементы, с помощью которых пользователь будет выбирать"""
        # метка-описание
        Label(self,
              text = "Ресторанное меню"
              ).grid(row = 0, column = 0, sticky = E)

        # метка-инструкция
        Label(self,
              text = "Выберите всё, что вам по вкусу:"
              ).grid(row = 1, column = 0, sticky = W)

        # флажок "Блюдо 1"
        self.likes_dish_01 = BooleanVar()
        Checkbutton(self,
                    text = "Блюдо 1",
                    variable = self.likes_dish_01,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        # флажок "Блюдо 2"
        self.likes_dish_02 = BooleanVar()
        Checkbutton(self,
                    text = "Блюдо 2",
                    variable = self.likes_dish_02,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        # флажок "Блюдо 3"
        self.likes_dish_03 = BooleanVar()
        Checkbutton(self,
                    text = "Блюдо 3",
                    variable = self.likes_dish_03,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        # текстовая область с результатами
        self.results_txt = Text(self, width = 50, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
        self.price = 0.0
        self.literal = "Итоговая стоимость: "
        self.literal += str(self.price)
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, self.literal)

    def update_text(self):
        """Обновляет текстовый элемент по мере того, как пользователь
        выбирает свои любимые блюда"""
        likes = ""
        self.price = 0.0

        if self.likes_dish_01.get():
            value = 11.11
            likes += "Вы выбрали Блюдо 1, его стоимость: "
            self.price += value
            likes += str(value) + "\n"

        if self.likes_dish_02.get():
            value = 22.22
            likes += "Вы выбрали Блюдо 2, его стоимость: "
            self.price += value
            likes += str(value) + "\n"

        if self.likes_dish_03.get():
            value = 33.33
            likes += "Вы выбрали Блюдо 3, его стоимость: "
            self.price += value
            likes += str(value) + "\n"

        self.literal = "Итоговая стоимость: " + str(self.price)
        likes += self.literal
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)


# основная часть
root = Tk()
root.title("Ресторанное меню")
app = Application(root)
root.mainloop()