#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Паница в пиццерии
# Игрок должен ловить падающую пиццу, пока она не достигла земли
from superwires import games
import random

games.init(screen_width=640, screen_height=480, fps=50)

class Pan(games.Sprite):
    """Сковорода, в которую игрок может ловить падающую пиццу"""
    image = games.load_image("pan.bmp")

    def __init__(self):
        """Инициализирует объект Pan и создаёт объект Text для отображения счёта"""
        super(Pan, self).__init__(image=Pan.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
        self.score = games.Text(value=0,
                                size=25,
                                color=color.black,
                                top=5,
                                right=games.screen.width-10)
        games.screen.add(self.score)

    def update(self):
        """Передвигает объект по горизонтали в точку с абциссой, как у указателя мыши"""
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """Проверяет, поймал ли игрок падающую пиццу"""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
