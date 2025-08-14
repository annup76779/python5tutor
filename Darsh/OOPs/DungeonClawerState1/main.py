from DungeonClawerState1.characters import Player, Goblin, Dragon
from DungeonClawerState1.grid import Grid


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

    grid.add_character(Player(health=20))
    grid.add_character(Goblin(health=5))
    grid.add_character(Goblin(health=7))
    grid.add_character(Goblin(health=4))
    grid.add_character(Dragon(health=23))

    grid.show_grid()
    return grid


def run():
    grid = make_grid()
    while grid.status == "playing":
        direction = input("Enter direction: ")
        grid.move_player(direction)
        grid.show_grid()

    print("Final Score: ", grid.score)
    print("Result: ", grid.status)

if __name__ == "__main__":
    run()