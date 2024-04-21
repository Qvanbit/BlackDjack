from colorama import Fore
from utils import *


# Класс для игрока
class Player:
    def __init__(self, bankroll=5000):
        self.hand = []
        self.bankroll = bankroll
        self.bet = 0

    def place_bet(self, amount):
        """
        Метод для размещения ставки игроком.

        Аргументы:
        amount (int): Сумма ставки.

        Возвращает:
        bool: True, если ставка размещена успешно, иначе False.
        """
        if amount > self.bankroll:
            print_message("Недостаточно средств", Fore.RED)
            return False
        self.bet = amount
        return True

    def double_down(self):
        """
        Метод для удвоения ставки игроком.

        Возвращает:
        bool: True, если удвоение ставки прошло успешно, иначе False.
        """
        if self.bet * 2 > self.bankroll:
            print_message("Недостаточно средств для удвоения ставки", Fore.RED)
            return False
        self.bet *= 2
        return True

    def win_bet(self):
        """Метод для увеличения банкролла игрока при выигрыше."""
        self.bankroll += self.bet

    def lose_bet(self):
        """Метод для уменьшения банкролла игрока при проигрыше."""
        self.bankroll -= self.bet

    def clear_hand(self):
        """Метод для очистки руки игрока."""
        self.hand = []

    def show_hand(self, hide_first_card=False):
        """
        Метод для отображения карт на руке игрока.

        Аргументы:
        hide_first_card (bool): Флаг, указывающий, нужно ли скрыть первую карту.

        Возвращает:
        str: Строка с отображением карт на руке игрока.
        """
        if hide_first_card:
            print("Ваши карты: [Скрытая карта]", *[str(card) for card in self.hand[1:]])
        else:
            print("Ваши карты:", *[str(card) for card in self.hand])
