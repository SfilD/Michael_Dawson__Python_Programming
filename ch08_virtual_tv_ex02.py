#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Программа имитирует телевизор, как объект
# У пользователя есть возможность вводить номер канала
# и увеличивать и уменьшать громкость

class Virtual_tv(object):
    """Virtual TV"""
    def __init__(self, channel = 0, volume = 0):
        self.channel = channel
        self.volume = volume

    def __str__(self):
        rep = "Текущее состояние телевизора:\n"
        rep += "Номер канала: " + str(self.channel) + "\n"
        rep += "Уровень громкости: " + str(self.volume) + "\n"
        return rep


def main():
    tv = Virtual_tv()
    key_control = None
    while key_control != "|":
        print(tv)
        key_control = input("Ввести номер канала (0-200)\n"
                            "Увеличить/уменьшить громкость (+/-)\n"
                            "Выключить телевизор (|): ")
        if key_control == "|":
            print("Выход из программы")
            break

        elif key_control == "":
            continue

        elif key_control == "+":
            if tv.volume < 200:
                tv.volume += 1

        elif key_control == "-":
            if tv.volume > 0:
                tv.volume -= 1

        elif int(key_control) >= 0 and int(key_control) <= 200:
            tv.channel = int(key_control)


main()
