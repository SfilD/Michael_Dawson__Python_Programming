#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Летающая пицца
# Демонстрирует движущиеся спрайты
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")
the_pizza = games.Sprite(image=pizza_image,
                         x=games.screen.width/2,
                         y=games.screen.height/2,
                         dx=4,
                         dy=4)
games.screen.add(the_pizza)

games.screen.mainloop()
