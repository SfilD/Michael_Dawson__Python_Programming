#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Блэк-джек
# От 1 до 7 игроков против дилера
import ch09_cards, ch09_games

class BJ_Card(ch09_cards.Card):
    """Карта для игры в Блэк-джек"""
    ACE_VALUE = 1
    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self, rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(ch09_cards.Deck):
    """Колода для игры в 'Блэк-джек'"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(ch09_cards.Hand):
    """Набор карт 'Блэк-джека' у одного игрока"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # если у одной из карт value равно None, то и всё свойство равно None
        for card in self.cards:
            if not card.value:
                return None
        # суммируем очки, считая каждый туз за 1 очко
        t = 0
        for card in self.cards:
            t += card.value
        # определяем, есть ли туз на руках у игрока