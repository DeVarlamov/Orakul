import random


class Random_choise:
    """Класс определения случайного выбора"""
    def __init__(self, args) -> str:
        self.args = args

    def get_random_str(args) -> str:
        """Метод случайного выбора в строке"""
        return random.choice(args)

    def get_random_smails(args) -> str:
        """Метод случаного выбора гифок"""
        return random.choice(args)


def get_random_card(cartes):
    """Вспомогательный метод отображения карты и значения"""
    card, pack = random.choice(list(cartes.items()))
    if card is None:
        card = 'carts/ожидание.png'
    return card, pack
