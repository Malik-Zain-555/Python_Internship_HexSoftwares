# Tic-Tac-Toe Game (Python + Tkinter)

## Internship Project

This project was developed as the **first task of my internship at HEX Softwares**.
The objective of this task was to build a fully functional **Tic-Tac-Toe game using Python and Tkinter**, demonstrating GUI programming, game logic implementation, and basic AI behavior.

The project focuses on strengthening programming fundamentals while building an interactive desktop application.

---

# Overview

This project is a graphical implementation of the classic **Tic-Tac-Toe** game built using **Python** and the **Tkinter GUI library**.

The application supports two modes:

* **Player vs Player (PvP)**
* **Player vs Computer (PvC)**

Players take turns placing their symbols on a **3×3 board**, and the game automatically detects **wins, losses, and draws**.

---

# Objectives of the Task

This internship task was designed to help develop practical skills in:

* Python GUI development
* Event-driven programming
* Logical problem solving
* Game state management
* Implementing basic artificial intelligence behavior

Through this project, the developer learns how a simple concept can be turned into a **complete interactive desktop application**.

---

# Game Features

## 1. Two Game Modes

### Player vs Player (PvP)

* Two players play on the same system.
* Players alternate between **❌ and ⭕**.
* The system checks for winners after every move.

---

### Player vs Computer (PvC)

* The user plays against a computer opponent.
* The computer automatically selects its moves.

---

## 2. Smart CPU Opponent

The computer opponent uses a simple strategy:

1. Check if it can **win immediately**
2. If not, check if the **player is about to win** and block the move
3. Otherwise select a **random available position**

This creates a more intelligent opponent instead of a completely random one.

---

# Game Board Representation

The board consists of **9 buttons arranged in a 3×3 grid**.

Board Index Layout:

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

These indices are used internally to detect winning patterns.

---

# Win Detection Logic

The program checks all possible winning patterns:

Rows

* `[0,1,2]`
* `[3,4,5]`
* `[6,7,8]`

Columns

* `[0,3,6]`
* `[1,4,7]`
* `[2,5,8]`

Diagonals

* `[0,4,8]`
* `[2,4,6]`

When a player wins:

* The winning buttons turn **green**
* All other buttons are **disabled**
* A popup message displays the **winner**

---

# Draw Detection

If all cells are filled and no winning pattern is found:

* The board turns **gray**
* A popup message displays **"It's a Draw!"**
* The player can choose to restart the game.

---

# Replay System

After a game finishes, the program shows a popup dialog:

```
Game Over
Player Wins!
Play Again?
```

Options:

**Yes**

* Reset the board
* Start a new game

**No**

* Close the application

---

# Technologies Used

* **Python**
* **Tkinter (GUI Library)**
* **Random Module**

Tkinter is used for:

* Creating the window interface
* Managing button layouts
* Handling user click events
* Displaying popup messages

---

# Grid Layout Logic

The buttons are arranged using the following logic:

```python
row = index // 3
col = index % 3
```

This automatically maps a list of buttons into a **3×3 grid structure**.

Example:

| Index | Row | Column |
| ----- | --- | ------ |
| 0     | 0   | 0      |
| 1     | 0   | 1      |
| 2     | 0   | 2      |
| 3     | 1   | 0      |
| 4     | 1   | 1      |
| 5     | 1   | 2      |

---

# How to Run the Project

### 1. Install Python

Download Python from:

https://www.python.org

---

### 2. Run the Program

Open terminal or command prompt and run:

```
python main.py
```

The Tic-Tac-Toe game window will appear.

---

# Project Structure

```
tic-tac-toe/
│
├── main.py
└── README.md
```

---

# Learning Outcomes

By completing this internship task, the developer gains practical experience in:

* GUI programming with Tkinter
* Event-driven application design
* Game logic implementation
* Basic artificial intelligence decision making
* Writing clean and modular Python code

---

# Future Improvements

Possible future improvements include:

* Scoreboard system
* Player name input
* Advanced AI using the **Minimax Algorithm**
* Sound effects
* Improved UI design
* Dark mode interface

---

# Author

**Zain Ali**

BS Computer Science Student
Frontend & Full Stack Developer
Game and Software Enthusiast

---

# Internship

This project was completed as part of my internship work at **HEX Softwares**.
