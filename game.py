"""
game.py
=======
Module implementing an interactive number guessing game.

PRD Compliance:
- FR-09: Number-guessing game with a limited number of attempts.
- Fixed range (1 to 20).
- Gives 'higher'/'lower' feedback.
- Gracefully handles non-numeric input.
- Enforces maximum attempt limit.
"""

import random


def play_guessing_game(
    user_name: str = "Friend",
    max_attempts: int = 5,
    lower_bound: int = 1,
    upper_bound: int = 20,
) -> None:
    """
    Executes an interactive number-guessing game session.

    Args:
        user_name (str): Name of the active user.
        max_attempts (int): Maximum attempts permitted (default: 5).
        lower_bound (int): Lowest possible number in range (default: 1).
        upper_bound (int): Highest possible number in range (default: 20).
    """
    target = random.randint(lower_bound, upper_bound)
    attempts_used = 0

    print(
        f"Assistant: I'm thinking of a number between {lower_bound} and {upper_bound}. "
        f"You have {max_attempts} tries."
    )

    import sys
    if not sys.stdin.isatty():
        print(f"Assistant: Interactive terminal not attached. Returning to main menu.")
        return

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        try:
            prompt = f"You (Guess {attempts_used + 1}/{max_attempts}): "
            user_input = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAssistant: Game session aborted. Returning to main menu.")
            return

        # Check for quit/exit inside the game
        if user_input.lower() in ("exit", "quit", "cancel"):
            print(f"Assistant: Game cancelled! The number was {target}.")
            return

        # Validate numeric integer input
        try:
            guess = int(user_input)
        except ValueError:
            print("Assistant: Please enter a valid whole number.")
            continue

        attempts_used += 1

        if guess == target:
            print(
                f"Assistant: Congratulations, {user_name}! You guessed the number "
                f"{target} in {attempts_used} {'try' if attempts_used == 1 else 'tries'}!"
            )
            return
        elif guess < target:
            if attempts_used < max_attempts:
                print("Assistant: Too low! Try a higher number.")
        else:
            if attempts_used < max_attempts:
                print("Assistant: Too high! Try a lower number.")

    print(f"Assistant: Game over! The number was {target}. Better luck next time, {user_name}!")
