#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Доработка программы "Викторина"
# В текстовом файле хранятся имена игроков и их лучшие результаты

import sys, shelve

def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')

    except IOError as err:
        print("Невозможно открыть файл", file_name, ", работа программы будет завершена.", err)
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

    points = next_line((the_file))
    explanation = next_line(the_file)
    return category, question, answers, correct, points, explanation


def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("Добро пожаловать в игру 'Викторина'!")
    print(title)


def main():
    trivia_file = open_file("ch07_trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    names_and_scores = {}
    with open('ch07_name_scores.txt') as inp:
        for i in inp.readlines():
            key, val = i.strip().split(':')
            names_and_scores[key] = val

    inp.close()

    name = input("Введите ваше имя: ")
    if names_and_scores.get(name) == None:
        print(name, ", это ваша первая игра", sep="")
        names_and_scores[name] = score
    else:
        print(name, ", ваш лучший результат составляет ", names_and_scores[name], " балл(а/ов)", sep="")

    # извлечение первого блока
    category, question, answers, correct, points, explanation = next_block(trivia_file)

    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print(i + 1, "-", answers[i], end="")

        # получение ответа
        answer = input("Ваш ответ: ")

        # проверка ответа
        if answer == correct:
            print("Да!", end=" ")
            score += int(points)

        else:
            print("Нет.", end=" ")
        print(explanation)
        print("Счёт:", score)

        # переход к следующему вопросу
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("Это был последний вопрос!")
    print("На вашем счету", score, "балл(а/ов)")

    if int(names_and_scores[name]) < score:
        names_and_scores[name] = score

    with open('ch07_name_scores.txt', 'w') as out:
        for key, val in names_and_scores.items():
            out.write('{}:{}\n'.format(key, val))
    out.close()


main()
