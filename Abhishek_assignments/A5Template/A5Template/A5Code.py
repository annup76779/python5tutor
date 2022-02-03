from tkinter import *
import random
"""A5: Draws a pattern
Username:
Name:
"""


def main():
    size = 50
    start_x = 20
    start_y = 30
    filename = input("Enter a filename: ")
    contents = read_lines(filename)
    patterns_dict = create_patterns_dictionary(contents)
    number_of_rows = 8
    canvas_size = size * number_of_rows + start_x * 2
    window = Tk()
    #Insert your username
    window.title("A5 by aban377")
    window.geometry(str(canvas_size)+"x"+str(canvas_size)+"+10+20")
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True)   
    draw_shapes(a_canvas, start_x, start_y, patterns_dict, size, number_of_rows)
    window.mainloop()

def read_lines(filename):
    """funtion returns list of each line in the file without any newline character"""
    with open(filename, "r") as file_:
        return [x.strip() for x in file_.readlines()]


def create_patterns_dictionary(lines):
    """Returns: dict: dictionay of colors keyed by the rowid in the file"""
    dictionary_of_colors = {}
    for i , j in enumerate(lines):
        dictionary_of_colors[i] = j.split(",")
    return dictionary_of_colors
    

def draw_shapes(a_canvas, start_x, start_y, patterns_dict, size, number_of_rows):
    y = start_y
    x = start_x
    i = 0
    for _ in range(number_of_rows):
        g = get_pattern(patterns_dict[i], number_of_rows)
        for color in g:
            a_canvas.create_rectangle(x, y, x+size, y+size, fill=color)
            x += size
        y+= size
        x = start_x
        i += 1
        if i >= len(patterns_dict):
            i = 0



def get_pattern(s, n):
    j = 0
    for _ in range(n):
        yield s[j]
        j += 1
        if j >= len(s):
            j = 0

main()
