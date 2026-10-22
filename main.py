"""
main.py
=======
Main application entry point for NOVA (Natural Offline Virtual Assistant).
Coordinates command routing, state management, and the central execution loop.

PRD Compliance:
- FR-01: Greets the user on startup and asks for their name.
- FR-02: Remembers user's name for session duration and uses it in responses.
- FR-03 & FR-04: Date and Time reporting.
- FR-05: Basic calculator functionality without eval().
- FR-06, FR-07, FR-08: Motivational quotes, jokes, and facts.
- FR-09: Number guessing game.
- FR-10: Help menu.
- FR-11: Graceful exit handling.
- FR-12: Unrecognized input fallback.
- FR-13: Rule-based recommendation (AI concept).
- FR-14: Perceptron demonstration (DL concept).
"""

import sys
import re

import greetings
import datetime_utils
import calculator
import content
import game
import ai_concepts
import help_menu


def route_command(user_input: str, user_name: str) -> bool:
    """
    Evaluates normalized user input against keyword and pattern matching rules,
    invoking the appropriate functional module.

    Args:
        user_input (str): The raw string entered by the user.
        user_name (str): The active session user's name.

    Returns:
        bool: True if the session should continue, False if an exit command was received.
    """
    # Normalize input: trim outer whitespace and convert to lowercase
    normalized = user_input.strip().lower()

    if not normalized:
        # User entered blank line; continue listening
        return True

    # -------------------------------------------------------------
    # 1. Exit Commands (FR-11)
    # -------------------------------------------------------------
    if normalized in ("exit", "quit", "bye", "goodbye", "close"):
        print(f"Assistant: Goodbye, {user_name}! Have a great day.")
        return False

    # -------------------------------------------------------------
    # 2. Help Menu (FR-10)
    # -------------------------------------------------------------
    elif normalized in ("help", "commands", "menu", "?"):
        help_menu.print_help()

    # -------------------------------------------------------------
    # 3. Interactive Greetings (FR-01 / FR-02)
    # -------------------------------------------------------------
    elif any(
        normalized.startswith(greet)
        for greet in ("hello", "hi", "hey", "greetings", "good morning", "good evening")
    ):
        print(f"Assistant: Hello, {user_name}! How can I help you today? Type 'help' for options.")

    # -------------------------------------------------------------
    # 4. Date and Time Reporting (FR-03 & FR-04)
    # -------------------------------------------------------------
    elif "time" in normalized or "clock" in normalized:
        print(datetime_utils.get_current_time())

    elif "date" in normalized or "today" in normalized:
        print(datetime_utils.get_current_date())

    # -------------------------------------------------------------
    # 5. Basic Calculator (FR-05)
    # -------------------------------------------------------------
    elif (
        normalized.startswith("calculate")
        or normalized.startswith("calc")
        or bool(re.search(r"^\s*[+-]?\d+(?:\.\d+)?\s*[\+\-\*\/]\s*[+-]?\d+", normalized))
    ):
        print(calculator.parse_expression(user_input))

    # -------------------------------------------------------------
    # 6. Quotes, Jokes, and Facts (FR-06, FR-07, FR-08)
    # -------------------------------------------------------------
    elif "quote" in normalized or "motivat" in normalized or "inspire" in normalized:
        print(content.get_random_quote(user_name))

    elif "joke" in normalized or "funny" in normalized or "laugh" in normalized:
        print(content.get_random_joke())

    elif "fact" in normalized or "trivia" in normalized or "knowledge" in normalized:
        print(content.get_random_fact())

    # -------------------------------------------------------------
    # 7. Number Guessing Game (FR-09)
    # -------------------------------------------------------------
    elif "game" in normalized or "guess" in normalized:
        game.play_guessing_game(user_name=user_name)

    # -------------------------------------------------------------
    # 8. Rule-Based Activity Recommendation (FR-13 - AI Concept)
    # -------------------------------------------------------------
    elif (
        "recommend" in normalized
        or "activity" in normalized
        or "schedule" in normalized
        or "what should i do" in normalized
    ):
        print(ai_concepts.recommend_activity(user_name=user_name))

    # -------------------------------------------------------------
    # 9. Artificial Neuron / Perceptron Demo (FR-14 - DL Concept)
    # -------------------------------------------------------------
    elif (
        "perceptron" in normalized
        or "neuron" in normalized
        or "neural" in normalized
        or "ai demo" in normalized
        or "dl demo" in normalized
    ):
        raw_args = re.findall(r"[-+]?\d*\.?\d+", user_input)
        nums = [float(x) for x in raw_args] if raw_args else None
        print(ai_concepts.perceptron_demo(custom_inputs=nums, interactive=(nums is None)))

    # -------------------------------------------------------------
    # 10. Fallback for Unrecognized Input (FR-12)
    # -------------------------------------------------------------
    else:
        print(f"Assistant: I'm not sure I understood that -- type 'help' to see what I can do.")

    return True


def main() -> None:
    """
    Primary application control loop.
    Initializes session, manages user state, and routes inputs safely.
    """
    try:
        # Step 1: Capture user name and greet (FR-01, FR-02)
        user_name = greetings.get_user_name()

        # Step 2: Display initial welcome with help prompt
        print(greetings.build_greeting(user_name))

        # Step 3: Main conversational loop
        is_running = True
        while is_running:
            try:
                user_input = input("You: ")
                is_running = route_command(user_input, user_name)
            except (KeyboardInterrupt, EOFError):
                print(f"\nAssistant: Goodbye, {user_name}! Have a great day.")
                break
            except Exception as e:
                # Top-level fault tolerance: prevent unexpected errors from terminating session
                print(f"Assistant: An unexpected error occurred: {e}. Please try again.")

    except (KeyboardInterrupt, EOFError):
        print("\nAssistant: Session terminated. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
