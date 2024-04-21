from utils import *


# Класс для крупье
class Dealer:
    """Класс, представляющий крупье в игре в блэкджек."""
    def __init__(self):
        self.hand = []
        self.hidden_card = None

    def clear_hand(self):
        """Очистка руки крупье."""
        self.hand = []

    def show_hand(self, hide_first_card=False):
        """Отображение карт крупье.
        Аргументы:
            hide_first_card (bool, optional): Флаг, указывающий, нужно ли скрыть первую карту.
                По умолчанию False.
        """
        if hide_first_card:
            print(
                "Карты крупье: [Скрытая карта]", *[str(card) for card in self.hand[1:]]
            )
        else:
            print("Карты крупье: \n", *[str(card) for card in self.hand])

    def hit(self, deck):
        """Крупье берет карту из колоды и добавляет ее в руку.

        Аргументы:
            deck (Deck): Колода карт.
        """
        self.hand.append(deck.deal_card())

    def reveal_hidden_card(self):
        """Раскрытие скрытой карты крупье."""
        self.hidden_card = self.hand[0]

    def show_hand_with_hidden_card(self, hide_first_card=False):
        """Отображение карт крупье с возможностью скрыть первую карту.

        Аргументы:
            hide_first_card (bool, optional): Флаг, указывающий, нужно ли скрыть первую карту.
                По умолчанию False.
        """
        if hide_first_card == True:
            if hide_first_card:
                print("Карты крупье:")
                print(display_card(self.hand[0], hidden=True))
                for card in self.hand[1:]:
                    print(display_card(card=card, hidden=False))
            else:
                print("Карты крупье:", *[display_card(card) for card in self.hand])
        else:
            print("Карты крупье: [Скрытые карты]")
            for card in self.hand[1:]:
                print(display_card(card, True))

