from tkinter import *
def main():
    root = Tk()
    a_canvas = Canvas(root, width=400, height=300)
    a_canvas.config(background="pink")
    a_canvas.pack(fill=BOTH, expand = True)
    draw_shapes(a_canvas, 20, 30, 3)
    root.mainloop()

def draw_oval(a_canvas, start_x, start_y, number_of_rows):
    size = 50
    for i in range(number_of_rows, 0, -1):
        x, y = start_x+(size*(number_of_rows - i)), start_y+(size*(number_of_rows - i))
        for _ in range(i * 2):
            a_canvas.create_oval(x, y, x+size, y+size, fill=file)
            x += size
        y+= size
            


main()
