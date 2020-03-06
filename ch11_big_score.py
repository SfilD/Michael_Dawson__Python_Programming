#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ничего себе результат!
# Демонстрирует отображение текста на графическом экране
from superwires import games, color

games.init(screen_width=640, screen_height=480, fps=50)
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image
score = games.Text(value=1756521,
                   size=60,
                   color=color.black,
                   x=games.screen.width/2,
                   y=games.screen.height/2)
games.screen.add(score)
games.screen.mainloop()
