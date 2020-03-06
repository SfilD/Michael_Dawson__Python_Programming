#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ничего себе результат!
# Демонстрирует отображение текста на графическом экране
from superwires import games, color

games.init(screen_width=640, screen_height=480, fps=50)
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image
score = games.Text(value=88,
                   size=60,
                   color=color.brown,
                   x=0,
                   y=0)
games.screen.add(score)
games.screen.mainloop()
