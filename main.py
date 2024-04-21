import time  # Импорт модуля для работы со временем
from colorama import Fore  # Импорт модуля для работы с цветами

from deck import Deck  # Импорт класса для колоды из файла deck.py
from player import Player  # Импорт класса для игрока из файла player.py
from dealer import Dealer  # Импорт класса для крупье из файла dealer.py

from utils import *  # Импорт дополнительных функций из файла utils.py


def play_game(player_bankroll, first_time, player_name):
    """
        Основная функция для игры в блэкджек.
    Аргументы на вход:
        player_bankroll (int): Начальный банкрол игрока.
        first_time (bool): Флаг, указывающий, является ли это первой игрой.
        player_name (str): Имя игрока.

    Возвращает:
        int: Итоговый банкрол игрока после окончания игры.
    """
    doubled_down = False  # Флаг для отслеживания удвоения ставки
    if first_time:  # Проверка, первая ли это игра
        print(f"Добро пожаловать, {player_name}!")
        time.sleep(2)
        print("Давайте сыграем в блэкджек.")
        time.sleep(2)
        print(
            "Блэкджек - это классическая карточная игра, также известная как `Двадцать одно`. Цель игры - набрать как можно большее количество очков до 21."
        )
        time.sleep(2)
        print(
            "Распределение очков: карты с цифрами стоят от 2 до 10 очков; карты с фигурами (валеты, короли и дамы) стоят 10 очков; тузы стоят 11 очков, если нет перебора, и 1 очко, в противном случае."
        )
        time.sleep(3)
        first_time = False

    deck = Deck()  # Создание новой колоды карт
    player = Player(player_bankroll)  # Создание нового игрока с начальным банкроллом
    dealer = Dealer()  # Создание нового крупье

    # Ставка игрока
    while True:
        try:
            bet = int(
                input(
                    f"{player_name}, у вас на счету {player.bankroll}. Сколько вы хотите поставить? "
                )
            )
            if bet <= 0:
                print("Ставка должна быть положительным числом.")
            elif bet > player.bankroll:
                print("Недостаточно средств на счету.")
            elif player.place_bet(bet):
                print(f"{player_name}, ваша ставка принята!")
                time.sleep(2)
                break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    # Раздача карт
    player.hand.append(deck.deal_card())
    player.hand.append(deck.deal_card())
    dealer.hand.append(deck.deal_card())
    dealer.hand.append(deck.deal_card())

    # Показываем карты
    print("Ваши карты:")
    print(display_hand(player.hand))
    dealer.show_hand_with_hidden_card(
        hide_first_card=True
    )  # hide_first_card - Флаг, для скрытой карты

    # Ход игрока
    while True:
        choice = (
            input(
                f"{player_name}, хотите взять еще карту, удвоить ставку и взять карту или закончить? (в/у/з) "
            )
            .strip()
            .lower()
        )
        if choice == "в":
            player.hand.append(deck.deal_card())  # Раздача карты игроку
            print(display_hand(player.hand))
            if calculate_score(player.hand) > 21:
                print_message(f"{player_name}, перебор! Вы проиграли.", Fore.RED)
                player.lose_bet()  # Списание ставки со счета игрока
                return player.bankroll
        elif choice == "у":
            if not doubled_down: # Проверка на уже удвоенную ставку
                if player.double_down():
                    player.hand.append(deck.deal_card())
                    print(display_hand(player.hand))
                    if calculate_score(player.hand) > 21:
                        print_message(
                            f"{player_name}, перебор! Вы проиграли.", Fore.RED
                        )
                        player.lose_bet()  # Списание ставки со счета игрока
                        return player.bankroll
                    doubled_down = True  # Устанавливаем флаг удвоения ставки
                    break
            else:
                print(f"{player_name}, вы уже удваивали ставку!")
        elif choice == "з":
            break

    # Ход крупье
    dealer.reveal_hidden_card()
    while calculate_score(dealer.hand) < 17:
        dealer.hit(deck)

    # Вывод карт крупье после завершения игры
    display_dealer_hand(dealer.hand)

    # Определение победителя
    player_score = calculate_score(player.hand) # Подсчет очков игрока
    dealer_score = calculate_score(dealer.hand) # Подсчет очков крупье
    if player_score > 21:
        print_message(f"{player_name}, у вас перебор! Вы проиграли.", Fore.RED)
        player.lose_bet()
    elif dealer_score > 21:
        print_message(
            f"У дилера перебор! Поздравляю, {player_name}, вы выиграли.", Fore.GREEN
        )
        player.win_bet()
    elif player_score > dealer_score:
        print_message(f"Поздравляю, {player_name}, вы выиграли!", Fore.GREEN)
        player.win_bet()
    elif player_score < dealer_score:
        print_message(f"{player_name}, вы проиграли.", Fore.RED)
        player.lose_bet()
    else:
        print_message("Ничья.", Fore.YELLOW)

    return player.bankroll


# Запуск игры
def main():
    """
    Основная функция для запуска игры.
    Запускает игру блэкджека и отображает историю игр.
    
    """
    player_bankroll = 5000 # Начальный банкролл игрока
    games_history = [] # История банкролла
    first_time = True # Флаг первой игры
    player_name = input("Привет! Как вас зовут?")
    while True:
        player_bankroll = play_game(
            player_bankroll, first_time=first_time, player_name=player_name
        )
        first_time = False # Сброс флага первой игры
        games_history.append(player_bankroll)
        if player_bankroll <= 0:
            print_message("У вас закончились деньги!", Fore.RED)
            break
        choice = input("Хотите сыграть еще раз? (да/нет) ").strip().lower()
        while choice not in ["да", "нет"]:
            choice = input("Пожалуйста, введите 'да' или 'нет': ").strip().lower()
        if choice != "да":
            break
    print("\nСпасибо за игру \nИстория игр:")
    for i, result in enumerate(games_history, start=1): # Итерация по истории банкролла
        print(f"Игра {i}: Банкролл: {result}")


if __name__ == "__main__":
    main()
