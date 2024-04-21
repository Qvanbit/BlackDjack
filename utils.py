from colorama import Fore, Style


def calculate_score(hand):
    """Вычисляет сумму очков в руке игрока.

    Аргументы:
        hand (list): Список карт в руке.

    Возвращает:
        int: Сумма очков.
    """
    score = sum(
        [
            (
                card.value
                if isinstance(card.value, int)
                else 10 if card.value in ["Валет", "Дама", "Король"] else 11
            )
            for card in hand
        ]
    )
    num_aces = sum([1 for card in hand if card.value == "Туз"])
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score


def display_card(card, hidden=False):
    """Возвращает строковое представление карты.

    Аргументы:
        card (Card): Карта.
        hidden (bool, optional): Флаг, указывающий, скрыта ли карта. По умолчанию False.

    Возвращает:
        str: Строковое представление карты.
    """
    suits_symbols = {"Черви": "♥", "Бубны": "♦", "Трефы": "♣", "Пики": "♠"}
    card_values = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        "Валет": "J",
        "Дама": "Q",
        "Король": "K",
        "Туз": "A",
    }
    value_str = f"{card_values[card.value]:<2}" # Форматируем строковое представление значения карты с выравниванием по левому краю и минимальной шириной 2 символа
    suit_str = f"{suits_symbols[card.suit]:<2}" # Форматируем изображение  карты с выравниванием по левому краю и минимальной шириной 2 символа

    if hidden:
        return f"{Fore.BLUE}┌───────┐\n│░░░░░░░│\n│░░░░░░░│\n│░░░░░░░│\n└───────┘{Style.RESET_ALL}"
    else:
        return f"{Fore.BLUE}┌───────┐\n│ {value_str}    │\n│       │\n│   {suit_str}  │\n└───────┘{Style.RESET_ALL}"


# Функция для вывода сообщений с цветом
def print_message(message, color=Fore.WHITE):
    print(color + message + Style.RESET_ALL)


# Функция для отображения руки
def display_hand(hand):
    return "\n".join(map(display_card, hand))


# Функция для отображения руки крупье
def display_dealer_hand(hand, hide_first_card=False):
    if hide_first_card:
        hidden_card = display_card(hand[0], True)
        other_cards = [display_card(card) for card in hand[1:]]
        print("Карты крупье: [Скрытая карта]\n", hidden_card, *other_cards)
    else:
        print("Карты крупье:")
        for card in hand:
            print(display_card(card))
