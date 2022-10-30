from operator import itemgetter

file = open('original.txt', 'r')
head = file.readline()
print(head)
data = file.readlines()
file.close()
players = []
for row in data:
    p = row.strip().split(',')
    player = [p[0].title(), tuple(int(x) for x in p[1].split("'"))]
    players.append((player))
players.sort(key=itemgetter(1))
print(players)

with open("players.txt", "w" , encoding="utf-8") as outfile:
    outfile.write("This file contains names and heights\n")
    for player_data in players:
        outfile.write(f"{player_data[1][0]} feet {player_data[1][1]} inches => {player_data[0]}\n")
