# Класс для карты
class Card:
    def __init__(self, value, suit):
        if value not in ['Валет', 'Дама', 'Король', 'Туз'] and not (2 <= value <= 10):
            raise ValueError("Недопустимое значение карты")
        if suit not in ['Черви', 'Бубны', 'Трефы', 'Пики']:
            raise ValueError("Недопустимая масть карты")
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.suit}"
