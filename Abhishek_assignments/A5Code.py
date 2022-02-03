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
    window.title("A5 by YOUR_USERNAME")
    window.geometry(str(canvas_size)+"x"+str(canvas_size)+"+10+20")
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True)   
    draw_shapes(a_canvas, start_x, start_y, patterns_dict, size, number_of_rows)

def read_lines(filename):
    #complete this function


def create_patterns_dictionary(lines):
    #complete this function


def draw_shapes(a_canvas, start_x, start_y, patterns_dict, size, number_of_rows):
    y = start_y
    x = start_x
    number_of_colours = len(patterns_dict[0])
    #complete this function

        
main()
