# 🎰 Python Slot Machine Game

## 📌 Overview

This is a simple command-line slot machine game written in Python.
Players can deposit money, place bets on multiple lines, spin the slot machine, and win based on matching symbols.

---

## 🚀 Features

* Deposit money to start playing
* Choose number of lines to bet on (1–3)
* Set bet amount per line
* Randomized slot spins
* Winning system based on matching symbols across rows
* Tracks player balance

---

## 🧠 How It Works

* The slot machine is a 3x3 grid.
* Each column is randomly generated using weighted symbols:

  * A (rare, high payout)
  * B
  * C
  * D (common, low payout)
* You win when all symbols in a selected row match.

---

## 💰 Symbol Values

| Symbol | Count | Value |
| ------ | ----- | ----- |
| A      | 2     | 5x    |
| B      | 4     | 4x    |
| C      | 6     | 3x    |
| D      | 8     | 2x    |

---

## ▶️ How to Run

1. Make sure you have Python installed
2. Save the file as `slot_machine.py`
3. Run the program:

```bash
python slot_machine.py
```

---

## 🎮 How to Play

1. Enter a deposit amount
2. Choose number of lines to bet on
3. Enter your bet per line
4. Spin the slot machine
5. Win money if symbols match across a row
6. Press **Enter** to keep playing or type **q** to quit

---

## 🛠 Requirements

* Python 3.x
* No external libraries needed (uses built-in `random` module)

---

## 📈 Example Output

```
D | B | A
C | C | C
A | D | B

You won $9.
You won on lines: 2
```

---

## 📌 Notes

* Total bet = bet per line × number of lines
* Winnings are added to your balance
* The game continues until you quit

---

## ✨ Future Improvements

* Add animations for spins
* Add jackpot system
* GUI version using Tkinter or Pygame
* Sound effects

---

## 👤 Author

Created as a beginner Python project to practice loops, functions, and logic.
