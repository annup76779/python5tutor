class GridItem:
    symbol = "·"
    def __init__(self, new_symbol=None):
        if new_symbol is not None:
            self.symbol = new_symbol

    @property
    def can_move(self):
        return True

    def __repr__(self):
        return f" {self.symbol} " if self.can_move else f"[{self.symbol}]"


class Character(GridItem):
    pass


class Player(Character):
    symbol = "P"


class Goblin(Character):
    symbol = "G"


class Dragon(Character):
    symbol = "D"


class Wall(GridItem):
    symbol = "#"

    @property
    def can_move(self):
        return False
