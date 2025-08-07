import random

from DungeonClawerState1.characters import GridItem, Character, Wall, Player, Goblin, Dragon


class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid: list[list[GridItem]] = [[GridItem() for i in range(column)] for j in range(row)]

    def is_cell_available(self, row, column):
        return isinstance(self.grid[row][column], (Character, Wall))

    def add_character(self, character: Character):
        position: tuple[int, int] | None = None
        if isinstance(character, Player):
            position = (0, 0)
        elif isinstance(character, Goblin):
            available_positions = [(i, j) for i in range(self.row) for j in range(self.column) if self.is_cell_available(i, j)]
            position = random.choice(available_positions)
        elif isinstance(character, Dragon):
            position = (self.row - 1, self.column - 1)

        self.grid[position[0]][position[1]] = character


    def add_wall(self, index: tuple[int, int]):
        if len(index) == 2:
            self.grid[index[0]][index[1]] = Wall()
        else:
            raise Exception("Invalid index")

    def show_grid(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print()


def make_grid():
    grid = Grid(9, 9)
    # from column 6-8
    grid.add_wall((0, 6))
    grid.add_wall((0, 7))
    grid.add_wall((0, 8))

    # from column 0-3
    grid.add_wall((1, 0))
    grid.add_wall((1, 1))
    grid.add_wall((1, 2))
    grid.add_wall((1, 3))

    # from column 0-7
    grid.add_wall((2, 0))
    grid.add_wall((2, 1))
    grid.add_wall((2, 2))
    grid.add_wall((2, 3))
    grid.add_wall((2, 4))
    grid.add_wall((2, 5))
    grid.add_wall((2, 6))
    grid.add_wall((2, 7))

    # from row 3-7
    grid.add_wall((3, 0))
    grid.add_wall((4, 0))
    grid.add_wall((5, 0))
    grid.add_wall((6, 0))
    grid.add_wall((7, 0))

    # from row 3-7
    grid.add_wall((4, 1))
    grid.add_wall((4, 2))
    grid.add_wall((4, 4))
    grid.add_wall((4, 5))
    grid.add_wall((4, 6))
    grid.add_wall((4, 7))
    grid.add_wall((4, 8))

    # from row 5
    grid.add_wall((5, 1))
    grid.add_wall((5, 2))
    grid.add_wall((5, 4))
    grid.add_wall((5, 6))
    grid.add_wall((5, 7))
    grid.add_wall((5, 8))

    # from row 6
    grid.add_wall((6, 1))
    grid.add_wall((6, 4))
    grid.add_wall((6, 6))
    grid.add_wall((6, 7))
    grid.add_wall((6, 8))

    grid.add_wall((7, 6))
    grid.add_wall((7, 7))
    grid.add_wall((7, 8))

    grid.add_wall((8, 2))
    grid.add_wall((8, 3))
    grid.add_wall((8, 4))

    grid.add_character(Player())
    grid.add_character(Goblin())
    grid.add_character(Goblin())
    grid.add_character(Goblin())
    grid.add_character(Dragon())

    grid.show_grid()

if __name__ == "__main__":
    make_grid()