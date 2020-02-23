#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Сумасшедший сказочник
# Создаёт рассказ на основе пользовательского ввода
from tkinter import *

class Application(Frame):
    """GUI-приложение, создающее рассказ на основе пользовательского ввода"""
    def __init__(self, master):
        """Инициализирует рамку"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создаёт элементы управления, с помощью которых пользователь
        будет вводить исходные данные и получать готовый рассказ"""
        # метка с текстом-инструкцией
        Label(self,
              text = "Введите данные для создания нового рассказа"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # метка и поле ввода для имени человека
        Label(self,
              text = "Имя человека: "
              ).grid(row = 1, column = 0, columnspan = 2, sticky = W)

        self.person_ent = Entry(self)
        self