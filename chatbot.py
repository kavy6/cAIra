from tkinter import *
import random


def send():

    
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower().strip()
         

    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, How are you feeling today?")
          
                 
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hello! How are you feeling today?")

        
    elif (user == "i feel good"):
        txt.insert(END, "\n" + "Bot -> That's wonderful! Tip of the day: " + tip)
        f.write(user)
        f.write(" ")
        

    elif (user == "i don't feel so good today"):
        txt.insert(END, "\n" + "Bot -> I'm sorry to hear that. Is there any particular reason?")
        f.write(user)
        f.write(" ")
        

    elif ("because" in user or "as" in user):                
        txt.insert(END, "\n" + "Bot -> Kindly book an appointment with the counsellor. They will be able to assist you further.")
        f.write(user)
        f.write(" ")

    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine!")

    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

        
    elif (user == "thanks" or user == "thank you"):
        txt.insert(END, "\n" + "Bot -> My pleasure!")

    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

    elif (user == "bye" or user == "see you later" or user == "goodbye"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")
        f.write("\n")
        f.close()

    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you")

    e.delete(0, END)




# Main
f = open("data.txt", "a")
f.write("Details: ")


    
# GUI
root = Tk()
root.title("Chatbot")


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

root.iconbitmap('C:/Users/DELL/OneDrive/Desktop/Project/icon-Copy1.ico')


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="cAIra", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

tips = ["Remember to sleep well!", "Keep in touch with friends", "Try meditation to enhance your mood further", "Go for a walk today", "Try a new workout!"]
tip = random.choice(tips)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)


