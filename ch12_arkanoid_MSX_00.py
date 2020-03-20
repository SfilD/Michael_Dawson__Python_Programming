#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Arkanoid MSX
# Фоновая картинка
from superwires import games

games.init(screen_width=544, screen_height=480, fps=50)


class Bat(games.Sprite):
    """Движущаяся бита"""
    image = games.load_image("ch12_arkanoid_MSX_bat.png")

    def __init__(self, x = 224, y = 406): # x = 224, y = 406
        """Инициализация биты"""
        super(Bat, self).__init__(image = Bat.image,
                                  x = x,
                                  y = y)
        games.mouse.is_visible = False # выключить курсор
        games.mouse.position = (self.x, self.y) # позиционировать биту в x = 224, y = 406
        # пока не знаю, чем отличается self.x от x, в данном случае эффект одинаковый

    def update(self):
        """Перемещение биты вправо-влево по горизонтали до границ рабочего поля"""
        self.x = games.mouse.x
        if self.left <= 0 + Ball.gap_left:
            self.left = 0 + Ball.gap_left

        if self.right >= games.screen.width - Ball.gap_right:
            self.right = games.screen.width - Ball.gap_right

#        if games.keyboard.is_pressed(games.K_LEFT) and self.left > 0 + Ball.gap_left:
#            self.x -= 1

#        if games.keyboard.is_pressed(games.K_RIGHT) and self.right < games.screen.width - Ball.gap_right:
#            self.x += 1


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
#        if self.top < 0 + Ball.gap_top:
            self.dy = -self.dy


def main():
    background_image = games.load_image("ch12_arkanoid_MSX_background_01.png", transparent=False)
    games.screen.background = background_image

    the_bat = Bat()
    games.screen.add(the_bat)

    the_ball = Ball()
    games.screen.add(the_ball)

    games.screen.mainloop()


if __name__ == "__main__":
    main()