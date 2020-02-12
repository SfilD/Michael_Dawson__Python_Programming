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
