#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Взрыв
# Демонстрирует создание анимации
from superwires import games
games.init(screen_width=640, screen_height=480, fps=50)
nebula_image = games.load_image("nebula.jpg", transparent=0)
games.screen.background = nebula_image
explosion_files = ["explosion1.bmp",
                   "explosion2.bmp",
                   "explosion3.bmp",
                   "explosion4.bmp",
                   "explosion5.bmp",
                   "explosion6.bmp",
                   "explosion7.bmp",
                   "explosion8.bmp",
                   "explosion9.bmp"]
explosion = games.Animation(images=explosion_files,
                            x=games.screen.width/2,
                            y=games.screen.height/2,
                            n_repeats=1,
                            repeat_interval=3)
games.screen.add(explosion)
games.screen.mainloop()
