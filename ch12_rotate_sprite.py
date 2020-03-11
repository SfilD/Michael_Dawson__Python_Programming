#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Крутящийся спрайт
# Демонстрирует вращение спрайта
from superwires import games
games.init(screen_width=640, screen_height=480, fps=50)

class Ship(games.Sprite):
    """Вращающийся космический корабль"""
    def update(self):
        """Вращает корабль определённым образом, исходя из нажатых клавиш"""
        if games.keyboard.is_pressed(games.K_d):
            self.angle += 1

        if games.keyboard.is_pressed(games.K_a):
            self.angle -= 1

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0

        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90

        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180

        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

        if games.keyboard.is_pressed(games.K_UP):
            self.y -= 1

        if games.keyboard.is_pressed(games.K_DOWN):
            self.y += 1

        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 1

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 1


def main():
    nebula_image = games.load_image("nebula.jpg", transparent=False)
    games.screen.background = nebula_image
    ship_image = games.load_image("ship.bmp")
    the_ship = Ship(image=ship_image,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()


if __name__ == "__main__":
    main()
