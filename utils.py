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


class Taro:
    def __init__(self, cart, description, image) -> None:
        self.cart = cart
        self.description = description
        self.image = image

    def get_cart_tree(card):
        """Метод раздачи карт."""
        return random.choice(card)
