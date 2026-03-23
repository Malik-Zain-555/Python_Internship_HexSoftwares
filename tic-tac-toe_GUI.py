import tkinter as tk
from tkinter import messagebox
import random   

current_turn = "❌"
game_mode = None

Player_Move = "❌"
CPU_Move = "⭕"

def PvP(clicked_button):
    if response != True:
        global current_turn
        
        if clicked_button.cget("text") == "":
            clicked_button.config(text=current_turn, state="disabled")                
        
        winPattern = checkWin(current_turn)
        
        if winPattern:
            for i in winPattern:
                Buttons[i].config(background="green", fg="white")
            return endGame(current_turn)

        # Checking Draw 
        if all(btn.cget("text") != "" for btn in Buttons):
            for btn in Buttons:
                btn.config(background="grey",fg="white")
            messagebox.showinfo("Game Over","It's a Draw!")
            resetGame()
            return
        
        if current_turn == "❌":
            current_turn = "⭕"
        else: 
            current_turn = "❌"  

        lable.config(text=f"{current_turn}-Turn")
        
    else:
        CPU()

def CPU(player_clicked):
    global Player_Move, CPU_Move
    
    lable.config(text="PvC Mode")
    
    if player_clicked.cget("text") == "":
        
        # Player-Move
        player_clicked.config(text=Player_Move, state="disabled")
        
        if checkWin(Player_Move):
            winPattern = checkWin(Player_Move)
            if winPattern:
                for i in winPattern:
                    Buttons[i].config(background="green", fg="white")
                return endGame("Player")
        
        # Finding empty btn after player move
        emptyButtons = [btn for btn in Buttons if btn.cget("text") == ""]        

        for btn in emptyButtons:
            btn.config(text=CPU_Move)
            if checkWin(CPU_Move):
                winPattern = checkWin(CPU_Move)
                if winPattern:
                    for i in winPattern:
                        Buttons[i].config(background="green", fg="white")
                    btn.config(state="disabled")
                    return endGame("CPU")
            btn.config(text="")

        for btn in emptyButtons:
            btn.config(text=Player_Move)
            if checkWin(Player_Move):
                btn.config(text=CPU_Move, state="disabled")
                return
            btn.config(text="")
        
        # Computer Move
        if emptyButtons:
            cpuChoice = random.choice(emptyButtons)
            cpuChoice.config(text=CPU_Move, state="disabled")
            if checkWin(CPU_Move):
                winPattern = checkWin(CPU_Move)
                if winPattern:
                    for i in winPattern:
                        Buttons[i].config(background="green", fg="white")
                    return endGame("CPU")
    
        # Checking Draw 
        if all(btn.cget("text") != "" for btn in Buttons):
            for btn in Buttons:
                btn.config(background="grey",fg="white")
            messagebox.showinfo("Game Over","It's a Draw!")
            resetGame()
    
def checkWin(symbol):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    for pattern in win_patterns:
        if all(Buttons[i].cget("text") == symbol for i in pattern):
            return pattern
    return False

def endGame(winner):
    for btn in Buttons:
        btn.config(state="disabled")
        
    response = messagebox.askyesno("Game Over", f"{winner} Wins!\nPlay Again?")
    print(winner)
    print("Response: ",response)
    
    if response == True:
        resetGame() 
    else:
        root.destroy()

def resetGame():
    for btn in Buttons:
        btn.config(text="", state="normal", background="SystemButtonFace")
    global current_turn
    current_turn = "❌"
    lable.config(text="❌-turn")
    
root = tk.Tk()
response = messagebox.askyesno("Game Mode", "Play vs Computer?")
root.title("Zain Game")
root.geometry("400x400")
title = tk.Label(root, text="TIC-TAC-TOE",font=("Arial",16))

Buttons = []

# Creating Buttons
for btn in range(9):
    btn = tk.Button(root, text="", width=10, height=4)
    
    if response == True:
        btn.config(font=80,command=lambda b=btn: CPU(b))
        Buttons.append(btn)
    else:
        btn.config(font=80,command=lambda b=btn: PvP(b))
        Buttons.append(btn)
        

if response:
    lable = tk.Label(root, text="PvC Mode", font=("Arial",14))
else:
    lable = tk.Label(root, text="X-Turn", font=("Arial",14))
    
title.grid(row=0, column=0, columnspan=3)
lable.grid(row=1, column=0, columnspan=3) 

# Arranging Buttons in Grid Layout
for index,btn in enumerate(Buttons):
    row = index // 3
    col = index % 3
    btn.grid(row=row+2,column=col)

root.mainloop()