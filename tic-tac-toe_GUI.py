import tkinter as tk
from tkinter import messagebox
import random   

current_turn = "X"
game_mode = None

Player_Move = "X"
CPU_Move = "O"

def PvP(clicked_button):
    if response != True:
        global current_turn
        clicked_button.config(text=current_turn)
        clicked_button.config(state="disabled")
                
        if current_turn == "X":
            current_turn = "O"
        else: 
            current_turn = "X"  
        lable.config(text=f"{current_turn}-Turn")
        
        winner = clicked_button.cget("text") # Finding the value of clicked btn
        
        if Buttons[0].cget("text") == Buttons[1].cget("text") == Buttons[2].cget("text") != "" :
            return endGame(winner=winner)
        if Buttons[3].cget("text") == Buttons[4].cget("text") == Buttons[5].cget("text") != "" :
            return endGame(winner=winner)
        if Buttons[6].cget("text") == Buttons[7].cget("text") == Buttons[8].cget("text") != "" :
            return endGame(winner=winner)
        
        if Buttons[0].cget("text") == Buttons[3].cget("text") == Buttons[6].cget("text") != "" :
            return endGame(winner=winner)
        if Buttons[1].cget("text") == Buttons[4].cget("text") == Buttons[7].cget("text") != "" :
            return endGame(winner=winner)
        if Buttons[2].cget("text") == Buttons[5].cget("text") == Buttons[8].cget("text") != "" :
            return endGame(winner=winner)
        
        if Buttons[0].cget("text") == Buttons[4].cget("text") == Buttons[8].cget("text") != "" :
            return endGame(winner=winner)
        if Buttons[2].cget("text") == Buttons[4].cget("text") == Buttons[6].cget("text") != "" :
            return endGame(winner=winner)
       
       # Checking Draw 
        if all(btn.cget("text") != "" for btn in Buttons):
            messagebox.showinfo("Game Over","It's a Draw!")
            resetGame()
    else:
        CPU()

def CPU(player_clicked):
    global Player_Move, CPU_Move
    
    lable.config(text="PvC Mode")
    
    if player_clicked.cget("text") == "":
        
        # Player-Move
        player_clicked.config(text=Player_Move, state="disabled")
        
        if checkWin(Player_Move):
            return endGame("Player")
        
        # Finding empty btn after player move
        emptyButtons = [btn for btn in Buttons if btn.cget("text") == ""]        

        for btn in emptyButtons:
            btn.config(text=CPU_Move)
            if checkWin(CPU_Move):
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
                return endGame("CPU")
    
        # Checking Draw 
        if all(btn.cget("text") != "" for btn in Buttons):
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
            return True
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
        btn.config(text="", state="normal")
    global current_turn
    current_turn = "X"
    lable.config(text="X-turn")
    
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
        lable = tk.Label(root, text="PvC Mode ",font=("Arial",14))
    else:
        btn.config(font=80,command=lambda b=btn: PvP(b))
        Buttons.append(btn)
        lable = tk.Label(root, text="X-Turn",font=("Arial",14))
        
        
title.grid(row=0, column=0, columnspan=3)
lable.grid(row=1, column=0, columnspan=3) 

# Arranging Buttons in Grid Layout
for index,btn in enumerate(Buttons):
    row = index // 3
    col = index % 3
    btn.grid(row=row+2,column=col)

root.mainloop()