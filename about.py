# About page

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# change the title
root.title("About")
bg = "#43BFDB"
root['bg'] = bg

# resizing the window 
root.geometry('1150x550+50+50')


# change window icon
root.iconbitmap('C:/Users/DELL/OneDrive/Desktop/Project/icon-Copy1.ico')


# dropdown menu
def menu_funct(choice):
    choice = clicked.get()

    if choice == "Home":
        root.destroy()
        import final_project

    elif choice == "Instructions":
        root.destroy()
        import instructions

    else:
        pass

clicked = tk.StringVar()
options = ["Home", "About", "Instructions"]
clicked.set(options[1])


menu = tk.OptionMenu(root, clicked, *options, command=menu_funct)
menu.config(bg = bg, fg = "#808080")
menu["highlightthickness"] = 0
menu.pack()


canvas = tk.Canvas(root, width = 1000, height = 500, bg = bg)
canvas["highlightthickness"] = 0
canvas.pack()
canvas.create_text(100, 200, font=('Helvetica', 50), text='About')
canvas.create_text(370, 280, font=('Helvetica', 15), text='cAIra is an AI chatbot that enables mental health professionals to gain insight into', fill = "#900C3F")
canvas.create_text(360, 300, font=('Helvetica', 15), text='their client\'s concerns/ state of mind prior to meeting them in person.               ', fill = "#900C3F")

canvas.create_text(340, 370, font=('Helvetica', 15), text='It employs AI techniques such as facial recognition and emotion detection.', fill="#900C3F")
