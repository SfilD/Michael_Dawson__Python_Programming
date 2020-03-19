#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Arkanoid MSX
# Фоновая картинка
from superwires import games

games.init(screen_width=544, screen_height=480, fps=50)

class Ball(games.Sprite):
    """Скачущий шарик"""
    image = games.load_image("ch12_arkanoid_MSX_ball.png")
    gap_top = 64
    gap_left = 48
    gap_right = 144
    gap_bottom = 48

    def __init__(self, x = 233, y = 392): # x = 233, y = 392
        """Инициализация шарика"""
        super(Ball, self).__init__(image = Ball.image,
                                   x = x,
                                   y = y,
                                   dx = 3, #  3
                                   dy = -3) # -3

    def update(self):
        """Обращает одну или обе компоненты скорости, если достигнута граница экрана"""
        if self.right > games.screen.width - Ball.gap_right or self.left < 0 + Ball.gap_left:
            self.dx = -self.dx

        if self.bottom > games.screen.height - Ball.gap_bottom or self.top < 0 + Ball.gap_top:
            self.dy = -self.dy


def main():
    background_image = games.load_image("ch12_arkanoid_MSX_background_01.png", transparent=False)
    games.screen.background = background_image

    bat_image = games.load_image("ch12_arkanoid_MSX_bat.png", transparent=True)
    bat = games.Sprite(image = bat_image,
                       x = 224,  # исходное положение биты по горизонтали
                       y = 406)  # исходное положение биты по вертикали
    games.screen.add(bat)

    the_ball = Ball()
    games.screen.add(the_ball)

    games.screen.mainloop()


if __name__ == "__main__":
    main()