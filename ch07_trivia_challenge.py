#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Викторина
# Игра на выбор правильного варианта ответа,
# вопросы которой читаются из текстового файла

import sys

def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')

    except IOError as err:
        print("Невозможно открыть файл", file_name, ", работа программы будет завершена.\n", err)
        sys.exit()

    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        correct = next_line(the_file)
        if correct:
            correct = correct[0]
            explanation = next_line(the_file)
    return category, question, answers, correct, explanation


