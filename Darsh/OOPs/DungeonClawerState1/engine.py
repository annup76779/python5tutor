from random import randint, choices, choice


def fight(grid, position: list | tuple):
    goblin_dragon = grid.grid[position[0]][position[1]]
    player = grid.player

    fighters = [goblin_dragon, player]

    scores = [x/10 for x in range(1, 11)]

    while goblin_dragon.health > 0 and player.health > 0:
        defender_index = randint(0, 1)
        defender = fighters[defender_index]

        defender.health -= choice(scores)
        grid.score += 1

    return player.health > 0

"""
1. When will the fighting starts?
    - When the index of goblin/dragon == index of player -> they will start fighting

2.What is the algo
    we will maintain the attacker and defender
    while the health of player > 0 and health of goblin/dragon > 0:
        for each attach, the health of defender will be reduced randomly by a number from range 0.1 - 1
        if attacker is dragon, the player gets chance to attach twice, but the damage by dragon will be 1.5 time more than that of player
        also for each win, the score of player will be increased by 1
"""