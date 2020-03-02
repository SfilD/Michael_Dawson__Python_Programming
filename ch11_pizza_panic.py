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


class Pizza(games.Sprite):
    """Круги пиццы, падающие на землю"""
    image = games.load_image("pizza.bmp")
    speed = 1

    def __init__(self, x, y=90):
        """Инициализирует объект Pizza"""
        super(Pizza, self).__init__(image=Pizza.image,
                                    x=x,
                                    y=y,
                                    dy=Pizza.speed)

    def update(self):
        """Проверяет, не коснулась ли нижняя кромка спрайта нижней границы экрана"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """Разрушает объект, пойманный игроком"""
        self.destroy()

    def end_game(self):
        """Завершает игру"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    """Кулинар, который, двигаясь влево-вправо, разбрасывает пиццу"""
    image = games.load_image("chef.bmp")

    def __init__(self, y=55, speed=2, odds_change=200):
        """Инициализирует объект Chef"""
        super(Chefб self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dx=speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

