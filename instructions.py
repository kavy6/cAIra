# Instructions page

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# change the title
root.title("Instructions")
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

    elif choice == "About":
        root.destroy()
        import about

    else:
        pass

clicked = tk.StringVar()
options = ["Home", "About", "Instructions"]
clicked.set(options[2])

menu = tk.OptionMenu(root, clicked, *options, command=menu_funct)
menu.config(bg = bg, fg = "#808080")
menu["highlightthickness"] = 0
menu.pack()



canvas = tk.Canvas(root, width = 1000, height = 500, bg = bg)
canvas["highlightthickness"] = 0
canvas.pack()
canvas.create_text(200, 200, font=('Helvetica', 50), text='Instructions')
canvas.create_text(300, 270, font=('Helvetica', 15), text="Step 1: Click on the 'Get Started' button on the Home page", fill = "#900C3F")
canvas.create_text(280, 300, font=('Helvetica', 15), text="Step 2: Look into the camera for facial recognition       ", fill = "#900C3F")
canvas.create_text(275, 330, font=('Helvetica', 15), text="Step 3: Once identified, click on the 'Next' button       ", fill = "#900C3F")
canvas.create_text(290, 360, font=('Helvetica', 15), text="Step 4: Look into the camera for emotion detection        ", fill = "#900C3F")
canvas.create_text(260, 390, font=('Helvetica', 15), text="Step 5: Have a chat with cAIra!                           ", fill = "#900C3F")
