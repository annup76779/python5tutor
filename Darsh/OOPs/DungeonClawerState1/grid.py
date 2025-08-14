import random

from DungeonClawerState1.characters import GridItem, Character, Wall, Player, Goblin, Dragon
from DungeonClawerState1.engine import fight


class Grid:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid: list[list[GridItem]] = [[GridItem() for i in range(column)] for j in range(row)]
        self.player = None
        self.score = 0
        self.status = "playing"

    def is_cell_available(self, row, column):
        if 0 <= row < self.row and 0 <= column < self.column:
            if isinstance(self.grid[row][column], (Wall,)):
                return False
            else:
                return True
        return False

    def add_character(self, character: Character):
        position: tuple[int, int] | None = None
        if isinstance(character, Player):
            position = (0, 0)
            self.player = character
        elif isinstance(character, Goblin):
            available_positions = [(i, j) for i in range(self.row) for j in range(self.column) if self.is_cell_available(i, j)]
            position = random.choice(available_positions)
        elif isinstance(character, Dragon):
            position = (self.row - 1, self.column - 1)

        # set its coordinates
        character.x = position[0]
        character.y = position[1]

        self.grid[position[0]][position[1]] = character


    def add_wall(self, index: tuple[int, int]):
        if len(index) == 2:
            self.grid[index[0]][index[1]] = Wall(x=index[0], y=index[1])
        else:
            raise Exception("Invalid index")

    def show_grid(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print()

        print("Health: ", self.player.health, "\tScore: ", self.score, end="\n\n")


    def move_player(self, direction):
        x, y = self.player.x, self.player.y
        if direction == "up":
            if self.is_cell_available(self.player.x - 1, self.player.y):
                self.player.x -= 1
        elif direction == "down":
            if self.is_cell_available(self.player.x + 1, self.player.y):
                self.player.x += 1
        elif direction == "left":
            if self.is_cell_available(self.player.x, self.player.y - 1):
                self.player.y -= 1
        elif direction == "right":
            if self.is_cell_available(self.player.x, self.player.y + 1):
                self.player.y += 1

        if not (x != self.player.x or y != self.player.y):
            print(f"You cannot move in {direction} direction")
        else:
            if isinstance(self.grid[self.player.x][self.player.y], (Goblin, Dragon)):
                if not fight(self, (self.player.x, self.player.y)):
                    self.status="lost"
                    return False

                self.grid[x][y], self.grid[self.player.x][self.player.y] = GridItem(), self.grid[x][y]
            else:
                self.grid[x][y], self.grid[self.player.x][self.player.y] = self.grid[self.player.x][self.player.y], self.grid[x][y]

        if self.player.x == self.row - 1 and self.player.y == self.column - 1:
            self.status = "win"
        return None
