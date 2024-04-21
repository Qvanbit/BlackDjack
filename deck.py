import random

from card import Card


# Класс для колоды
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Черви", "Бубны", "Трефы", "Пики"]:
            for value in range(2, 11):
                self.cards.append(Card(value, suit))
            for face in ["Валет", "Дама", "Король", "Туз"]:
                self.cards.append(Card(face, suit))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
