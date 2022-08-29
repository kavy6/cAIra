import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# change the title
root.title("Emotion Detection")
bg = "#43BFDB"
root['bg'] = bg

# resizing the window 
root.geometry('1150x550+50+50')


# change window icon
root.iconbitmap('C:/Users/DELL/OneDrive/Desktop/Project/icon-Copy1.ico')


# dropdown menu
def menu_funct(choice):
    choice = clicked.get()

    if choice == "About":
        root.destroy()
        import about

    elif choice == "Instructions":
        root.destroy()
        import instructions

    else:
        pass

clicked = tk.StringVar()
options = ["Home", "About", "Instructions"]
clicked.set(options[0])


menu = tk.OptionMenu(root, clicked, *options, command=menu_funct)
menu.config(bg = bg, fg = "#808080")
menu["highlightthickness"] = 0
menu.pack()




canvas = tk.Canvas(root, width = 1000, height = 500, bg = bg)
canvas["highlightthickness"] = 0
canvas.pack()
canvas.create_text(100, 200, font=('Helvetica', 50), text='Hello!')
canvas.create_text(145, 250, font=('Helvetica', 25), text='Welcome to cAIra', fill = "#900C3F")

# add image
img = tk.PhotoImage(file="C:/Users/DELL/OneDrive/Desktop/Project/emotions.png")
canvas.create_image(620,80, anchor=tk.NW, image=img)
    
    

# button to move to next page
def start():
    # open new page
    root.destroy()
    import live_video

    

# Get Started button
btn = tk.Button(root, text = "Get Started -->", bg = "#29799E", command = start,activeforeground = "green",activebackground = "pink",pady=10, padx=10)
btn.place(x=65, y=100)
btn.pack()



# keep displaying the window
root.mainloop()
