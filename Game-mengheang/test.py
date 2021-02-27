import tkinter as tk

from random import randrange

main=tk.Tk()

main.geometry("600x600")

frame =tk.Frame()

frame.master.title("mengheang's work")

draw=tk.Canvas(frame)
def pressEnter(event):
    draw.delete("all")
# example
draw.create_rectangle(100,100,400,400,fill="red")

main.bind("<Return>",pressEnter)
draw.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
main.mainloop()