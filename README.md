# NOVA — Natural Offline Virtual Assistant

> **"Simple Commands. Smart Responses. Zero Internet."**

---

## 1. Project Overview & Purpose

**NOVA (Natural Offline Virtual Assistant)** is a lightweight, rule-based virtual assistant built entirely in Python using only the Python standard library. Developed as the foundational deliverable for the **Nexbridge Technologies AI Internship Program (Project Code: AI-INT-P1-VAA)**, NOVA demonstrates core software engineering disciplines, pattern matching, rule-based systems, and foundational concepts of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) through code-based analogies.

NOVA operates strictly offline within a standard command-line interface (CLI), providing instant responses without any third-party dependencies, network requests, cloud APIs, or persistent databases.

---

## 2. Business Problem Addressed

New engineers entering AI often face a significant gap between theoretical classroom programming and shipping a modular, structured, production-grade deliverable:
1. **Bridging Classroom Concepts**: Connecting fundamental constructs (conditionals, loops, functions, exception handling) to an interactive, user-facing product.
2. **Foundational AI/ML/DL Vocabulary**: Understanding what "rule-based expert systems", "classification analogies", "artificial neurons (perceptrons)", and "forward propagation" actually mean before using heavy black-box frameworks (like PyTorch or TensorFlow).
3. **Engineering Discipline**: Establishing baseline standards in modular design, error handling, strict PRD compliance, and verifiable acceptance testing.

---

## 3. Project Scope & Technology Boundaries

### In-Scope
- Pure Python 3.x console application running in terminal/CLI.
- Text-based input and output only.
- Strict use of the Python standard library only (`datetime`, `random`, `re`, `sys`, `typing`, `unittest`).
- 100% offline execution with zero network access.
- In-memory session state (user name, active dialogue) reset upon exit.
- Explicit rule-based decision logic and keyword pattern matching.
- Concrete, untrainded arithmetic demonstrations of perceptron forward propagation.

### Strictly Out-of-Scope (Strict PRD Compliance)
- No external machine learning or deep learning frameworks (no TensorFlow, PyTorch, Keras, scikit-learn).
- No external data libraries or databases (no pandas, NumPy, SQLite, SQL, MongoDB).
- No network APIs, external LLMs, or cloud services (no OpenAI, Gemini, REST endpoints).
- No GUI, web frameworks, or web servers (no Flask, Django, Streamlit, Tkinter).
- No audio/voice processing, speech recognition, or text-to-speech.
- No persistent storage across sessions (no disk serialization, config files, or databases).
- No multi-threaded or multi-user server architecture.

---

## 4. Prerequisites

- **Operating System**: Windows, macOS, or Linux.
- **Python Version**: Python 3.8+ (tested on Python 3.12+).
- **Dependencies**: None. Only the built-in Python standard library is required.

---

## 5. Project Folder Structure

The project strictly follows the recommended modular architecture specified in Section 24 and 25 of the PRD:

```text
NOVA/
├── main.py              # Application entry point; runs input/response loop and coordinates modules
├── greetings.py         # Startup banner, greeting logic, and session user-name capture
├── datetime_utils.py    # Date and time retrieval and formatting functions
├── calculator.py        # Safe arithmetic parsing and execution without eval()
├── content.py           # Predefined quotes, jokes, facts, and randomized accessors
├── game.py              # Number guessing game with attempt constraints and hints
├── ai_concepts.py       # Rule-based recommendation engine and Perceptron forward-pass demo
├── help_menu.py         # Formatted help catalog of supported commands
├── test_nova.py         # Automated unit and integration test suite
└── README.md            # Complete project documentation and verification audit
```

---

## 6. Installation & How to Run

### Installation
Clone or navigate to the project directory:
```bash
cd "c:\Users\badam giridhar\Desktop\NOVA"
```
No `pip install` commands are needed because NOVA relies exclusively on the Python standard library.

### Launching the Assistant
Run the following command in your terminal:
```bash
python main.py
```

### Running the Automated Test Suite
To execute the comprehensive test suite verifying all 14 Functional Requirements and edge cases:
```bash
python test_nova.py
```

---

## 7. Supported Commands

| Command Keyword | Description | Example Usage |
|---|---|---|
| `help` / `commands` / `menu` | Displays the help menu listing all available commands | `help` |
| `time` / `clock` | Shows the current system time in 12-hour format | `time` or `what time is it?` |
| `date` / `today` | Displays today's full formatted date | `date` or `today's date` |
| `calculate <expr>` | Performs safe arithmetic (`+`, `-`, `*`, `/`) without `eval()` | `calculate 12 + 8`, `calc 5 / 0` |
| `quote` / `motivate` | Returns a random motivational quote | `quote` |
| `joke` / `funny` | Returns a random programmer/tech joke | `joke` |
| `fact` / `trivia` | Shares an interesting technology or computing fact | `fact` |
| `game` / `guess` | Plays the interactive number guessing game (1–20, 5 tries) | `game` |
| `recommend` / `activity` | Demonstrates rule-based activity recommendations based on hour | `recommend` |
| `perceptron` / `ai demo` | Runs an artificial neuron simulation with forward pass breakdown | `perceptron` or `perceptron 1.0 0.5 -0.8` |
| `exit` / `quit` / `bye` | Gracefully terminates the session with a personalized farewell | `exit` |

---

## 8. Example Terminal Interactions

### Session Startup & Greeting
```text
==============================================================
         NOVA -- Natural Offline Virtual Assistant
       Simple Commands. Smart Responses. Zero Internet.
==============================================================
Assistant: Hi! I'm NOVA (Natural Offline Virtual Assistant). What's your name?
You: Priya
Assistant: Nice to meet you, Priya! Type 'help' to see what I can do.
```

### Time, Date, and Calculator
```text
You: time
Assistant: It's currently 08:45 PM.

You: date
Assistant: Today's date is Thursday, October 22, 2026.

You: calculate 12 + 8
Assistant: The result is 20

You: calculate 5 / 0
Assistant: I can't divide by zero -- try a different number.
```

### Content Generation
```text
You: joke
Assistant: Why do programmers prefer dark mode? Because light attracts bugs!

You: quote
Assistant: Here is an inspiring quote for you, Priya:
  "The secret of getting ahead is getting started. - Mark Twain"

You: fact
Assistant: Did you know? The world's first programmer was Ada Lovelace, who wrote an algorithm for Charles Babbage's Analytical Engine in 1843.
```

### Rule-Based Recommendation (AI Concept Demo)
```text
You: recommend
Assistant: [Evening Recommendation for Priya]
  Current Hour: 20:00
  Suggested Activity: Take a brisk walk, unwind with family or friends, and step away from screens.

  [AI Concept Note]
  This recommendation uses a Rule-Based Expert System (decision tree logic).
  The hour feature is evaluated against predefined threshold rules to classify
  the appropriate response, illustrating explicit condition-based AI.
```

### Perceptron Calculation (DL Concept Demo)
```text
You: perceptron 1.0 0.5 -0.8
Assistant: --- Artificial Neuron (Perceptron) Forward Pass ---
  Inputs (x)         : [1.0, 0.5, -0.8]
  Weights (w)        : [0.6, 0.4, -0.5]
  Bias (b)           : -0.2
  Formula            : z = sum(x_i * w_i) + b
  Calculation        : (1.0 * 0.6) + (0.5 * 0.4) + (-0.8 * -0.5) + (-0.2)
  Dot Product        : 1.2
  Weighted Sum (z)   : 1.0
  Activation Function: Step Function (output = 1 if z > 0 else 0)
  Final Output (y)   : 1
  -------------------------------------------------------
  [Deep Learning Concept Breakdown]
  1. Input: Numerical features representing observed data.
  2. Weight: Multipliers that amplify or inhibit specific inputs.
  3. Bias: An offset shifting the activation threshold.
  4. Forward Propagation: Left-to-right calculation from inputs to output.
  5. Note: This demo uses fixed handcrafted weights to illustrate neuron
     arithmetic. No actual gradient descent or parameter training occurred.

  [Optional Hidden Layer Analogy (2-Layer Network)]
  Layer 1 (Hidden Neurons):
    - Neuron H1 Output: 0 (Sum: -0.39)
    - Neuron H2 Output: 0 (Sum: -0.21)
  Layer 2 (Output Neuron):
    - Inputs from Hidden Layer: [0.0, 0.0]
    - Final Network Output: 0 (Sum: -0.5)
```

### Graceful Exit
```text
You: exit
Assistant: Goodbye, Priya! Have a great day.
```

---

## 9. Major Module Responsibilities

1. **`main.py`**:
   - Manages the primary user interaction loop (`while is_running`).
   - Normalizes input (`.strip().lower()`) and matches intent keywords.
   - Preserves session variables (such as `user_name`) in-memory.
   - Traps exceptions, `KeyboardInterrupt`, and `EOFError` so the assistant never crashes unexpectedly.

2. **`greetings.py`**:
   - Renders the official NOVA ASCII banner.
   - Implements `get_user_name()` with sanitization and a safe default fallback.
   - Provides `build_greeting()` to greet the user and suggest `help`.

3. **`datetime_utils.py`**:
   - Interfaces with the built-in `datetime` module.
   - Formats current 12-hour time and complete date strings cleanly.

4. **`calculator.py`**:
   - Safely parses mathematical expressions using regular expressions.
   - Disallows `eval()` to prevent code injection vulnerabilities.
   - Implements division-by-zero protection and handles malformed strings cleanly.

5. **`content.py`**:
   - Stores curated, predefined lists (`QUOTES`, `JOKES`, `FACTS`).
   - Uses `random.choice()` to return varied items on repeated requests.

6. **`game.py`**:
   - Implements the number-guessing mini-game with random target generation (`1` to `20`).
   - Enforces the 5-attempt limit and provides directional hints (`Too high!` / `Too low!`).
   - Rejects non-numeric guesses gracefully.

7. **`ai_concepts.py`**:
   - **Rule-Based Decision Logic**: Implements `recommend_activity()` using explicit conditionals (`if-elif-else`) based on the current hour.
   - **Perceptron Forward Pass**: Implements `perceptron_demo()` showing weighted sum calculation, bias offset, and Heaviside step activation ($f(z) = 1 \text{ if } z > 0 \text{ else } 0$).
   - **Hidden Layer Analogy**: Simulates an optional 2-layer forward propagation to illustrate deep learning layering.

8. **`help_menu.py`**:
   - Formats and prints the command index with clear, concise descriptions.

---

## 10. AI, ML, and DL Concepts Demonstrated

| Domain | Concept | Implementation in NOVA | Conceptual Analogy |
|---|---|---|---|
| **AI** | **Rule-Based Expert System** | `ai_concepts.recommend_activity()` | Demonstrates how traditional symbolic AI systems make decisions via deterministic conditional rules rather than statistical learning. |
| **AI** | **Keyword & Intent Recognition** | `main.route_command()` | Simulates NLU (Natural Language Understanding) command routing by matching keywords within normalized free-form text. |
| **ML** | **Classification Analogy** | `ai_concepts.recommend_activity()` | Input feature (time of day) is mapped to one of several discrete activity categories, mirroring a decision tree classifier. |
| **ML** | **In-Memory Parameter Retention** | `main.py` (`user_name` state) | Storing and reusing session attributes resembles how a model retains learned parameters during inference. |
| **DL** | **Artificial Neuron (Perceptron)** | `ai_concepts.calculate_neuron()` | Computes $z = \sum (x_i \cdot w_i) + b$, illustrating the mathematical foundation of neural networks. |
| **DL** | **Activation Function** | `ai_concepts.step_activation()` | Applies a threshold step function ($y = 1$ if $z > 0$ else $0$) to introduce non-linearity. |
| **DL** | **Forward Propagation** | `ai_concepts.perceptron_demo()` | Demonstrates the left-to-right information flow from inputs through weights and bias to the activation output. |
| **DL** | **Hidden Layer Layering** | `ai_concepts.multi_layer_analogy()` | Demonstrates intermediate hidden activations feeding into an output neuron. |

### Distinction Between Rule-Based Logic and Trained Models
- **Rule-Based Logic (What NOVA uses)**: Behavior is explicitly hard-coded by the developer using if/else statements. No data is analyzed, no parameters are adjusted, and no optimization algorithms (like gradient descent) run.
- **Trained Machine Learning (What NOVA does NOT use)**: A system infers patterns and learns numerical weights automatically from empirical training data by minimizing a loss function.

NOVA makes this distinction explicit in its code, documentation, and user output.

---

## 11. Requirement Traceability Matrix (Acceptance Criteria)

| PRD Requirement | Implementation Location | Test Performed | Result |
|---|---|---|---|
| **FR-01**: Greet user on startup and capture name | `greetings.py` (`get_user_name`) | Tested prompt, whitespace handling, and fallback in `test_nova.py` | **PASS** |
| **FR-02**: Remember name and use in responses | `main.py`, `content.py`, `greetings.py` | Verified name appears in greeting, quotes, recommendations, and exit | **PASS** |
| **FR-03**: Display current date on request | `datetime_utils.py` (`get_current_date`) | Verified formatted date string with current year and month in `test_nova.py` | **PASS** |
| **FR-04**: Display current time on request | `datetime_utils.py` (`get_current_time`) | Verified formatted 12-hour time string with AM/PM indicator in `test_nova.py` | **PASS** |
| **FR-05**: Basic arithmetic (`+`, `-`, `*`, `/`) | `calculator.py` (`calculate`, `parse_expression`) | Tested addition, subtraction, multiplication, division, floats, and zero-division | **PASS** |
| **FR-06**: Random motivational quote | `content.py` (`get_random_quote`) | Repeated 10 times; verified at least 2 distinct items returned | **PASS** |
| **FR-07**: Random joke from predefined list | `content.py` (`get_random_joke`) | Repeated 10 times; verified at least 2 distinct items returned | **PASS** |
| **FR-08**: Random fact from predefined list | `content.py` (`get_random_fact`) | Repeated 10 times; verified at least 2 distinct items returned | **PASS** |
| **FR-09**: Number guessing game (1-20, 5 tries) | `game.py` (`play_guessing_game`) | Verified bound parameters (1-20, max 5 attempts) and feedback hints | **PASS** |
| **FR-10**: Help menu listing all commands | `help_menu.py` (`print_help`, `get_help_text`) | Verified presence of all 11 commands in help output | **PASS** |
| **FR-11**: Graceful exit on exit/quit command | `main.py` (`route_command`) | Tested `exit`, `quit`, `bye`, `goodbye`; confirmed clean termination flag | **PASS** |
| **FR-12**: Fallback for unrecognized input | `main.py` (`route_command`) | Tested 5+ unknown phrases and random gibberish; confirmed friendly fallback | **PASS** |
| **FR-13**: Rule-based recommendation (AI demo) | `ai_concepts.py` (`recommend_activity`) | Evaluated across Morning (8h), Afternoon (14h), Evening (19h), and Night (23h) | **PASS** |
| **FR-14**: Perceptron demo (DL demo) | `ai_concepts.py` (`perceptron_demo`, `calculate_neuron`) | Verified weighted sum, bias offset, and binary step activation output | **PASS** |
| **Non-Functional**: Reliability (no crash on invalid inputs) | Entire application | Stress-tested with 25 diverse valid, invalid, empty, and malformed inputs | **PASS** |

---

## 12. Testing Verification Summary

- **Total Automated Tests**: 16 unit and integration test cases in `test_nova.py`.
- **Pass Rate**: 100% (16 Passed, 0 Failed, 0 Skipped).
- **Interactive Session Verification**: Full simulation completed via pipe automation verifying end-to-end user journey from startup greeting to clean farewell.
- **Dependencies Audit**: 0 third-party packages installed or imported.
- **Portability**: Verified against standard Python 3 runtime on Windows OS.
