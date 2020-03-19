#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Arkanoid MSX
# Фоновая картинка
from superwires import games

games.init(screen_width=544, screen_height=480, fps=50)

class Ball(games.Sprite):
    """Скачущий шарик"""

    def update(self):
        """Обращает одну или обе компоненты скорости, если достигнута граница экрана"""
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


def main():
    background_image = games.load_image("ch12_arkanoid_MSX_background_01.png", transparent=False)
    games.screen.background = background_image

    bat_image = games.load_image("ch12_arkanoid_MSX_bat.png", transparent=True)
    bat = games.Sprite(image = bat_image,
                       x = 224,  # исходное положение биты по горизонтали
                       y = 406)  # исходное положение биты по вертикали
    games.screen.add(bat)

    ball_image = games.load_image("ch12_arkanoid_MSX_ball.png")
    the_ball = Ball(image = ball_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 3,
                      dy = 3)
    games.screen.add(the_ball)

    games.screen.mainloop()


if __name__ == "__main__":
    main()