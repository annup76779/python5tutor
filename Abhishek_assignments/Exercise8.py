from tkinter import *
import random
"""A5: Draws a pattern
Username:
Name:
"""
import time


def main():
    size = 50
    start_x = 20
    start_y = 30
    # filename = input("Enter a filename: ")
    # contents = read_lines(filename)
    # patterns_dict = create_patterns_dictionary(contents)
    number_of_rows = 8
    canvas_size = size * number_of_rows + start_x * 2
    window = Tk()
    #Insert your username
    window.title("A5 by YOUR_USERNAME")
    window.geometry(str(canvas_size)+"x"+str(canvas_size)+"+10+20")
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True)   
    patterns_dict = {  
      0: ['#f0e8cd', '#dbd5b9', '#c0ba99', '#feebc9', '#fdcaa2', '#fca985'], 
      1: ['#fdcaa2', '#f0e8cd', '#fca985', '#c0ba99', '#feebc9', '#dbd5b9'],
      2: ['#f0e8cd', '#fdcaa2', '#dbd5b9', '#fca985', '#feebc9', '#c0ba99'], 
      3: ['#fca985', '#f0e8cd', '#dbd5b9', '#c0ba99', '#fdcaa2', '#feebc9'], 
      4: ['#fdcaa2', '#c0ba99', '#fca985', '#feebc9', '#dbd5b9', '#f0e8cd'], 
      5: ['#fdcaa2', '#f0e8cd', '#fca985', '#feebc9', '#c0ba99', '#dbd5b9'] 
    }
    start = time.time()
    draw_shapes(a_canvas, start_x, start_y, patterns_dict, size, number_of_rows)
    print((time.time() - start) * 1000, "miliseconds")
    window.mainloop()

def read_lines(filename):
    #complete this function
    pass

def create_patterns_dictionary(lines):
    #complete this function
    pass


def draw_shapes(a_canvas, start_x, start_y, patterns_dict, size, number_of_rows):
    y = start_y
    x = start_x
    # number_of_colours = len(patterns_dict[0])
    #complete this function
    
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


# def get_pattern(s, n):
#     ns = s[:n]
#     n = n - len(s)
#     if n <= 0:
#         return ns
#     return ns + get_pattern(s, n)
main()