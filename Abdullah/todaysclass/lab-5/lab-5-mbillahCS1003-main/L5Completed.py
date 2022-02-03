import matplotlib.pyplot as plt
import csv
import math

#This function takes the dictionary of items and a key and returns the amount of time it
#will take to blend
def to_zero(items_dict, key_name):
    blend_times = items_dict[key_name][4]
    time_to_zero = blend_times[len(blend_times) - 1]
    return time_to_zero

file = open('/content/Items.csv')
reader = csv.reader(file, delimiter=',')
items = dict()

for row in reader:
    print(row)
    if row[0] != '\ufeffItem':
        items[row[0]] = row[1:]


for key in items:
    c1 = float(items[key][0])
    c2 = float(items[key][1])
    c3 = float(items[key][2])
    constant = float(items[key][3])
    pieceSize = constant
    x = [0]
    y = [constant]
    timer = 0
    while pieceSize > 0:
        pieceSize = (c1 * (timer ** 3)) + (c2 * (timer ** 2)) + (c3 * timer) + constant
        y.append(pieceSize)
        timer += 0.1
        x.append(timer)
    
    items[key].append(x)
    items[key].append(y)

print(items)

choice = 1
while choice != 6:
    print('\n\nSelect an option:')
    print('\t1: Search Item’s Blend Time')
    print('\t2: Longest Blend Time')
    print('\t3: Shortest Blend Time')
    print('\t4: Compare Blend Times')
    print('\t5: Percentage of Blend Times')
    print('\t6: Exit')
    choice = int(input())

    # Search Item’s Blend Time
    if choice == 1:
        item_name = input("item name>")
        if item_name in items:
            blend_time = to_zero(items, item_name)
            print(f"{item_name} takes approximately {blend_time}s to blend.")
        else:
            print(f"{item_name} does not exist in the file")

    # Find the item with the Longest Blend Time
    elif choice == 2:
        # assume that the longest blend time is the
        # smallest number possible (negative infinity)
        longest_time = math.inf * -1
        longest_item = ''

        # loop through all items
        for key in items:
            time_to_zero = to_zero(items, key)

            # if the item's time is longer than the current longest
            if time_to_zero > longest_time:
                #set new longest time and longest item name
                longest_item = key
                longest_time = time_to_zero

        print("%s takes approximately %gs to blend and is the item that takes the longest time" %(longest_item,longest_time))
    
    # Find the item with the Shortest Blend Time
    elif choice == 3:
        # you can borrow from the code for choice == 2
        # but change it from the longest to the shortest blend time
        shortest_time = None
        shortest_item = ''

        # loop through all items
        for key in items:
            time_to_zero = to_zero(items, key)
            print(time_to_zero)

            # if the item's time is longer than the current longest
            if shortest_time is not None:
                if time_to_zero < shortest_time:
                    #set new longest time and longest item name
                    shortest_item = key
                    shortest_time = time_to_zero
            else:
                shortest_time = time_to_zero

        print("%s takes approximately %gs to blend and is the item that takes the shortest time" %(shortest_item, shortest_time))
        

    elif choice == 4:
        graph1 = input("item 1>")
        graph2 = input("item 2>")
        graph3 = input("item 3>")
        colour1 = input("color for item 1>")
        colour2 = input("color for item 2>")
        colour3 = input("color for item 3>")

        # TODO 5
        # create the line graphs for the 3 items, using the 3 colors
        plt.plot(items[graph1][4], items[graph1][5], "--.", color=colour1, label = graph1)
        plt.plot(items[graph2][4], items[graph2][5], "--*", color=colour2, label = graph2)
        plt.plot(items[graph3][4], items[graph3][5], "--+", color=colour3, label = graph3)

        plt.title("User Comparison")
        plt.xlabel("Time")
        plt.ylabel("Size of Piece")
        plt.legend()
        plt.show()

    elif choice == 5:
        time_given = float(input("Time for pie chart>"))

        below_above = [0, 0]

        for key in items:
        #   to_zero = to_zero(items, key)
          toZero = to_zero(items, key)

          if toZero <= time_given:
            below_above[0] += 1

          else:
            below_above[1] += 1

        plt.pie(below_above, colors=['red','blue'], labels=['%gs or less' %time_given, 'Above %gs' %time_given],explode = (0.1, 0),autopct = '%1.1f%%')

        plt.legend()
        plt.show()


file.close()