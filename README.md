# NOVA — Natural Offline Virtual Assistant

> **Simple Commands. Smart Responses. Zero Internet.**

NOVA is a lightweight, rule-based virtual assistant built with **pure Python standard library**. It runs completely offline in your terminal, providing instant responses with **zero external dependencies, zero APIs, and zero network calls**.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8 or higher.
- No installation needed (`pip install` not required).

### 2. Run the Assistant
```bash
python main.py
```

### 3. Run the Automated Tests
```bash
python test_nova.py
```

---

## 💬 Supported Commands

Type any of the following commands when prompted by `You: `:

| Command | What It Does | Example |
|---|---|---|
| `help` | Lists all available commands | `help` |
| `time` | Shows the current 12-hour time | `time` |
| `date` | Shows today's full date | `date` |
| `calculate <expr>` | Performs safe arithmetic (`+`, `-`, `*`, `/`) | `calculate 12 + 8` or `calc 5 / 0` |
| `quote` | Displays an inspiring motivational quote | `quote` |
| `joke` | Tells a clean programming/tech joke | `joke` |
| `fact` | Shares an interesting computing/tech fact | `fact` |
| `game` | Plays a number guessing game (1–20, 5 tries) | `game` |
| `recommend` | Recommends an activity based on the time of day | `recommend` |
| `perceptron` | Runs an artificial neuron simulation | `perceptron` or `perceptron 1.0 0.5 -0.8` |
| `exit` | Gracefully closes the assistant | `exit` or `bye` |

---

## 🖥️ Example Usage

```text
==============================================================
         NOVA -- Natural Offline Virtual Assistant
       Simple Commands. Smart Responses. Zero Internet.
==============================================================
Assistant: Hi! I'm NOVA (Natural Offline Virtual Assistant). What's your name?
You: Priya
Assistant: Nice to meet you, Priya! Type 'help' to see what I can do.

You: time
Assistant: It's currently 08:45 PM.

You: calculate 12 + 8
Assistant: The result is 20

You: joke
Assistant: Why do programmers prefer dark mode? Because light attracts bugs!

You: recommend
Assistant: [Evening Recommendation for Priya]
  Current Hour: 20:00
  Suggested Activity: Take a brisk walk, unwind with family or friends, and step away from screens.

You: exit
Assistant: Goodbye, Priya! Have a great day.
```

---

## 📁 Project Structure

```text
NOVA/
├── main.py              # Main loop, command routing, and session state
├── greetings.py         # Banner, greeting, and user name capture
├── datetime_utils.py    # Date and time formatting
├── calculator.py        # Safe arithmetic parsing without eval()
├── content.py           # Predefined quotes, jokes, and facts
├── game.py              # Interactive number guessing game
├── ai_concepts.py       # Rule-based recommendation & Perceptron demo
├── help_menu.py         # Formatted command help menu
├── test_nova.py         # Automated test suite (16 test cases)
└── README.md            # Project documentation
```

---

## 🧠 AI / ML / DL Concepts Demonstrated

| Concept | File Location | How It Works in Plain English |
|---|---|---|
| **Rule-Based AI** | `ai_concepts.py` | Uses explicit `if-elif-else` rules (decision tree) to recommend an activity based on the current hour. |
| **Intent Recognition** | `main.py` | Uses keyword detection to route user input to the correct feature without external NLP models. |
| **Artificial Neuron** | `ai_concepts.py` | Demonstrates a single Perceptron: multiplies inputs by weights, adds a bias ($z = \sum x_i w_i + b$), and applies a step activation function ($f(z) = 1 \text{ if } z > 0 \text{ else } 0$). |
| **Hidden Layer Analogy** | `ai_concepts.py` | Illustrates forward propagation through a simple 2-layer network. |

> **Note**: NOVA uses deterministic rule-based logic and arithmetic demonstrations. It does **not** perform gradient descent, parameter training, or statistical inference.

---

## 📋 Requirement Compliance & Test Results

All 14 Functional Requirements from the PRD were implemented and verified with automated tests:

| PRD ID | Feature Description | Implementation File | Status |
|:---:|---|---|:---:|
| **FR-01** | Greeting & Name Capture | `greetings.py` | **PASS** |
| **FR-02** | Session Name Memory & Reuse | `main.py`, `content.py` | **PASS** |
| **FR-03** | Date Reporting | `datetime_utils.py` | **PASS** |
| **FR-04** | Time Reporting | `datetime_utils.py` | **PASS** |
| **FR-05** | Basic Calculator (Safe, No `eval`) | `calculator.py` | **PASS** |
| **FR-06** | Motivational Quotes (Randomized) | `content.py` | **PASS** |
| **FR-07** | Joke Generator (Randomized) | `content.py` | **PASS** |
| **FR-08** | Fact Generator (Randomized) | `content.py` | **PASS** |
| **FR-09** | Number Guessing Game (1–20, 5 Tries) | `game.py` | **PASS** |
| **FR-10** | Help Menu | `help_menu.py` | **PASS** |
| **FR-11** | Graceful Exit | `main.py` | **PASS** |
| **FR-12** | Friendly Fallback for Unknown Input | `main.py` | **PASS** |
| **FR-13** | Rule-Based Activity Recommendation | `ai_concepts.py` | **PASS** |
| **FR-14** | Perceptron Simulation (Forward Pass) | `ai_concepts.py` | **PASS** |

### Test Suite Summary:
```text
Ran 16 tests in 0.003s — OK (100% Pass Rate)
```
