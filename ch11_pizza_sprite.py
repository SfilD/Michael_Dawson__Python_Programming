#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Спрайт-пицца
# Демонстрирует создание спрайта
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp", transparent=True)
pizza = games.Sprite(image=pizza_image,
                     x=games.screen.width/2,
                     y=games.screen.height/2)
games.screen.add(pizza)

games.screen.mainloop()
