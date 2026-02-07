from tkinter import *
import random

def nextturn(row, cols):

    global player

    if buttons[row][cols]['text'] == "" and checkwinner() is False:
        if player == players[0]:

            buttons[row][cols]['text'] = player

            if checkwinner() is False:
                player = players[1]
                label.config(text = (players[1]+"\'s turn")) 

            elif checkwinner() is True:
                label.config(text=(players[0]+" wins"))
            
            elif checkwinner() == ("Draw"):
                label.config(text=("Draw"))
        
        else:
            
            buttons[row][cols]['text'] = player

            if checkwinner() is False:
                player = players[0]
                label.config(text = (players[0]+"\'s turn")) 

            elif checkwinner() is True:
                label.config(text=(players[1]+" wins"))
            
            elif checkwinner() == "Draw":
                label.config(text=("Draw"))

def checkwinner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg= "green")
            buttons[row][1].config(bg= "green")
            buttons[row][2].config(bg= "green")
            return True
    
    for cols in range(3):
        if buttons[0][cols]['text'] == buttons[1][cols]['text'] == buttons[2][cols]['text'] != "":
            buttons[0][cols].config(bg= "green")
            buttons[1][cols].config(bg= "green")
            buttons[2][cols].config(bg= "green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg= "green")
        buttons[1][1].config(bg= "green")
        buttons[2][2].config(bg= "green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg= "green")
        buttons[1][1].config(bg= "green")
        buttons[2][0].config(bg= "green")
        return True
    
    elif emptyspaces() is False:
        
        for row in range(3):
            for cols in range(3):
                buttons[row][cols].config(bg= "yellow")
        return "Draw"

    else:
        return False

def emptyspaces():

    spaces = 9

    for row in range(3):
        for cols in range(3):
            if buttons[row][cols]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def newgame():
    global player

    player = random.choice(players)

    label.config(text=player +"\'s turn")

    for row in range(3):
        for cols in range(3):
            buttons[row][cols].config(text ="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x" , "o"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text= player + "\'s Turn", font=("consolas",40))
label.pack(side="top")

reset_button = Button(text="Restart", font=("consolas",20), command=newgame)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for cols in range(3):
        buttons[row][cols] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                    command=lambda row= row, cols= cols: nextturn(row, cols))
        buttons[row][cols].grid(row=row, column=cols)

window.mainloop()