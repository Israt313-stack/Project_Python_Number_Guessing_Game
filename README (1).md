<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:0a2a0a,100:1a4a1a&height=200&section=header&text=Number%20Guessing%20Game&fontSize=50&fontColor=39ff14&fontAlignY=38&desc=A%20simple%20Python%20number%20guessing%20game%20with%20attempt%20tracking&descAlignY=60&descColor=7fff7f" />
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python&logoColor=white" /></a>
  <a href="https://www.linux.org/"><img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" /></a>
  <a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/Editor-VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" /></a>
  <a href="https://github.com/Israt313-stack/Project_Python_Number_Guessing_Game/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square" /></a>
  <a href="https://github.com/Israt313-stack/Project_Python_Number_Guessing_Game"><img src="https://img.shields.io/badge/Copyright-IJMCoding-933ea3?style=flat-square" /></a>
</p>

<p align="center">
  <a href="https://github.com/Israt313-stack/Project_Python_Number_Guessing_Game/blob/main/number_guessing_game.py">
    <img src="https://img.shields.io/badge/-%F0%9F%92%BB%20VIEW%20SOURCE%20%20%E2%86%92-0a2a0a?style=for-the-badge&logoColor=39ff14" />
  </a>
</p>
<p align="center">✦ Click above to view the full source code on GitHub ✦</p>

---

### 🎮 Features

| 🎲 Random Number | ⬆️⬇️ Hints | 📊 Attempt Counter | 🏆 Win Message | 🔁 Replayable |
|---|---|---|---|---|
| Random number generated between 1 and 100 each game | "Too Low!" / "Too High!" feedback after every guess | Tracks and displays total number of attempts taken | Congratulations message with attempt count on win | Simple loop-based flow, run again anytime |

---

## 🖥️ Terminal Preview

```
Welcome to the world of Guessing Numbers!
Enter your guess (1-100): 50
Too High!
Enter your guess (1-100): 25
Too Low!
Enter your guess (1-100): 37
Too High!
Enter your guess (1-100): 30
Congratulations!
You guessed the number in 4 attempts.
```

---

## 🧠 How It Works

### Random Number Generation

```python
import random

secret_number = random.randint(1, 100)
attempt = 0

print("Welcome to Number Guessing Game!")
```

### Guess Comparison Loop

```python
while True:
    guess = int(input("Enter your guess (1-100): "))
    attempt += 1

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratulations!")
        print("You guessed the number in", attempt, "attempts.")
        break
```

### Attempt Counter and Win Condition

```python
attempt += 1        # increments on every guess
if guess == secret_number:
    print("You guessed the number in", attempt, "attempts.")
    break            # exits the loop once the correct number is guessed
```

---

## 🛠️ Run the Game

### Prerequisites

- Python 3 installed

```bash
# Check Python version
python3 --version
```

### Run

```bash
python3 number_guessing_game.py
```

---

## 📁 Project Structure

```
Project_Python_Number_Guessing_Game/
│
├── 📄 number_guessing_game.py   ← Full source code
└── 📄 README.md                 ← Project documentation
```

---

## 🛠️ Tech Stack

```
┌──────────────────────────────────────────────────┐
│           Python Console Application              │
├─────────────────┬────────────────────────────────┤
│  Language       │  Python 3                       │
│  Editor         │  VS Code                        │
│  Modules        │  random                          │
│  UI             │  Console / terminal input-output │
│  Platform       │  Cross-platform (Linux, Windows) │
└─────────────────┴────────────────────────────────┘
```

---

## 📚 Key Concepts Used

```
random.randint(1, 100) → generate a random number between 1 and 100
while True              → keep asking until correct guess
if / elif / else        → compare guess to secret number
attempt += 1             → increment counter on every guess
input() / int()          → read and convert user input
break                    → exit the loop once guessed correctly
```

---

## 👤 Developer

**Israt Jahan Mojumder**
Competitive Programmer · Game Development Learner · CSE @ DIU

<p>
  <a href="https://github.com/Israt313-stack"><img src="https://img.shields.io/badge/GitHub-Israt313--stack-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://github.com/Israt313-stack/Project_Python_Number_Guessing_Game/blob/main/number_guessing_game.py"><img src="https://img.shields.io/badge/Source%20Code-View%20File-0a2a0a?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

*"The computer knows the number. Do you?"* 🎮

---

<p align="center">MIT License · © 2026 Israt Jahan Mojumder · ⭐ Star this repo if it helped you!</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a4a1a,50:0a2a0a,100:0d1117&height=120&section=footer" />
