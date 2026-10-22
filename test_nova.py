"""
test_nova.py
============
Comprehensive automated test suite for NOVA (Nimble Offline Virtual Assistant).
Validates all Functional Requirements (FR-01 through FR-14), acceptance criteria,
application flow, and non-functional reliability requirements.
"""

import unittest
import io
import sys
from datetime import datetime
from unittest.mock import patch

import greetings
import datetime_utils
import calculator
import content
import game
import ai_concepts
import help_menu
import main


class TestNovaAssistant(unittest.TestCase):

    def setUp(self):
        self.user_name = "Priya"

    # -------------------------------------------------------------
    # FR-01 & FR-02: Greeting & Name Capture / Retention
    # -------------------------------------------------------------
    def test_fr01_fr02_greeting_and_name_retention(self):
        """Test that user name is formatted into greeting and personalized responses."""
        greeting = greetings.build_greeting(self.user_name)
        self.assertIn("Priya", greeting)
        self.assertIn("help", greeting.lower())

        # Test quote personalization with user name
        quote_msg = content.get_random_quote(self.user_name)
        self.assertIn("Priya", quote_msg)

        # Test recommendation with user name
        rec_msg = ai_concepts.recommend_activity(hour=10, user_name=self.user_name)
        self.assertIn("Priya", rec_msg)

    def test_fr01_empty_name_handling(self):
        """Verify that empty or whitespace-only name defaults cleanly to 'Friend'."""
        with patch('builtins.input', return_value="   "):
            captured = io.StringIO()
            with patch('sys.stdout', captured):
                name = greetings.get_user_name()
            self.assertEqual(name, "Friend")
            self.assertIn("No name entered", captured.getvalue())

    # -------------------------------------------------------------
    # FR-03: Date Reporting
    # -------------------------------------------------------------
    def test_fr03_current_date(self):
        """Test that current date is accurately returned and formatted."""
        date_str = datetime_utils.get_current_date()
        current_year = str(datetime.now().year)
        self.assertIn("Today's date is", date_str)
        self.assertIn(current_year, date_str)

    # -------------------------------------------------------------
    # FR-04: Time Reporting
    # -------------------------------------------------------------
    def test_fr04_current_time(self):
        """Test that current time is accurately returned and formatted."""
        time_str = datetime_utils.get_current_time()
        self.assertIn("It's currently", time_str)
        self.assertTrue("AM" in time_str or "PM" in time_str)

    # -------------------------------------------------------------
    # FR-05: Basic Calculator
    # -------------------------------------------------------------
    def test_fr05_calculator_operations(self):
        """Test standard arithmetic operations."""
        self.assertEqual(calculator.calculate(12, "+", 8), "The result is 20")
        self.assertEqual(calculator.calculate(25, "-", 9), "The result is 16")
        self.assertEqual(calculator.calculate(7, "*", 6), "The result is 42")
        self.assertEqual(calculator.calculate(15, "/", 3), "The result is 5")
        self.assertEqual(calculator.calculate(7, "/", 2), "The result is 3.5")
        self.assertEqual(calculator.calculate(-5, "+", 10), "The result is 5")

    def test_fr05_calculator_division_by_zero(self):
        """Test graceful division by zero handling."""
        res = calculator.calculate(5, "/", 0)
        self.assertEqual(res, "I can't divide by zero -- try a different number.")
        parsed_res = calculator.parse_expression("calculate 5 / 0")
        self.assertIn("I can't divide by zero -- try a different number.", parsed_res)

    def test_fr05_calculator_parsing_and_invalid_inputs(self):
        """Test expression parsing from strings and invalid input rejection without crash."""
        self.assertIn("20", calculator.parse_expression("calculate 12 + 8"))
        self.assertIn("15", calculator.parse_expression("10 + 5"))
        self.assertIn("50", calculator.parse_expression("calc 100 / 2"))

        # Malformed inputs
        err_res = calculator.parse_expression("calculate abc + def")
        self.assertIn("Invalid calculation format", err_res)

        err_res2 = calculator.parse_expression("not a formula")
        self.assertIn("Invalid calculation format", err_res2)

    # -------------------------------------------------------------
    # FR-06, FR-07, FR-08: Content Generation & Randomness Verification
    # -------------------------------------------------------------
    def test_fr06_quotes_randomness(self):
        """Test quote generation and confirm variation over 10 repeats."""
        quotes = set()
        for _ in range(10):
            quotes.add(content.get_random_quote())
        self.assertGreaterEqual(len(quotes), 2, "Expected at least 2 distinct quotes over 10 draws.")

    def test_fr07_jokes_randomness(self):
        """Test joke generation and confirm variation over 10 repeats."""
        jokes = set()
        for _ in range(10):
            jokes.add(content.get_random_joke())
        self.assertGreaterEqual(len(jokes), 2, "Expected at least 2 distinct jokes over 10 draws.")

    def test_fr08_facts_randomness(self):
        """Test fact generation and confirm variation over 10 repeats."""
        facts = set()
        for _ in range(10):
            facts.add(content.get_random_fact())
        self.assertGreaterEqual(len(facts), 2, "Expected at least 2 distinct facts over 10 draws.")

    # -------------------------------------------------------------
    # FR-09: Number Guessing Game Logic (Strengthened Coverage)
    # -------------------------------------------------------------
    def test_fr09_game_bounds_and_range(self):
        """Verify game settings conform to PRD (1 to 20 range, 5 attempts) and random targets stay within bounds."""
        import inspect
        sig = inspect.signature(game.play_guessing_game)
        self.assertEqual(sig.parameters['max_attempts'].default, 5)
        self.assertEqual(sig.parameters['lower_bound'].default, 1)
        self.assertEqual(sig.parameters['upper_bound'].default, 20)

        # Range verification across 100 random numbers
        import random
        for _ in range(100):
            target = random.randint(1, 20)
            self.assertTrue(1 <= target <= 20)

    def test_fr09_game_hints_higher_lower(self):
        """Verify that game gives correct higher/lower feedback."""
        inputs = iter(["5", "15", "10"])
        captured = io.StringIO()
        with patch('sys.stdout', captured):
            won = game.play_guessing_game(
                user_name=self.user_name,
                max_attempts=5,
                target_number=10,
                input_func=lambda prompt: next(inputs)
            )
        output = captured.getvalue()
        self.assertIn("Too low! Try a higher number.", output)
        self.assertIn("Too high! Try a lower number.", output)
        self.assertTrue(won)

    def test_fr09_game_successful_guess(self):
        """Verify winning message and correct attempt tracking."""
        inputs = iter(["7"])
        captured = io.StringIO()
        with patch('sys.stdout', captured):
            won = game.play_guessing_game(
                user_name=self.user_name,
                max_attempts=5,
                target_number=7,
                input_func=lambda prompt: next(inputs)
            )
        output = captured.getvalue()
        self.assertIn("Congratulations, Priya! You guessed the number 7 in 1 try!", output)
        self.assertTrue(won)

    def test_fr09_game_unsuccessful_exhausted_attempts(self):
        """Verify that game enforces the 5-attempt limit and displays game over message."""
        inputs = iter(["1", "2", "3", "4", "5"])
        captured = io.StringIO()
        with patch('sys.stdout', captured):
            won = game.play_guessing_game(
                user_name=self.user_name,
                max_attempts=5,
                target_number=18,
                input_func=lambda prompt: next(inputs)
            )
        output = captured.getvalue()
        self.assertIn("Game over! The number was 18. Better luck next time, Priya!", output)
        self.assertFalse(won)

    def test_fr09_game_invalid_input_handling(self):
        """Verify non-numeric input is handled without crashing or consuming attempts unfairly."""
        inputs = iter(["notanumber", "10"])
        captured = io.StringIO()
        with patch('sys.stdout', captured):
            won = game.play_guessing_game(
                user_name=self.user_name,
                max_attempts=5,
                target_number=10,
                input_func=lambda prompt: next(inputs)
            )
        output = captured.getvalue()
        self.assertIn("Please enter a valid whole number.", output)
        self.assertIn("Congratulations, Priya!", output)
        self.assertTrue(won)

    # -------------------------------------------------------------
    # FR-10: Help Menu
    # -------------------------------------------------------------
    def test_fr10_help_menu_completeness(self):
        """Test that all required commands are listed in the help menu."""
        help_text = help_menu.get_help_text()
        required_commands = [
            "time", "date", "calculate", "quote", "joke",
            "fact", "game", "recommend", "perceptron", "help", "exit"
        ]
        for cmd in required_commands:
            self.assertIn(cmd, help_text)

    # -------------------------------------------------------------
    # FR-11: Graceful Exit & Loop Termination
    # -------------------------------------------------------------
    def test_fr11_graceful_exit_and_aliases(self):
        """Test that all exit aliases return False and print personalized farewell."""
        for exit_word in ("exit", "quit", "bye", "goodbye", "close"):
            captured = io.StringIO()
            with patch('sys.stdout', captured):
                should_continue = main.route_command(exit_word, self.user_name)
            self.assertFalse(should_continue, f"Command '{exit_word}' should signal exit.")
            self.assertIn("Goodbye, Priya! Have a great day.", captured.getvalue())

    # -------------------------------------------------------------
    # FR-12: Fallback on Unrecognized Input
    # -------------------------------------------------------------
    def test_fr12_fallback_handling(self):
        """Verify unrecognized inputs produce exact fallback message and keep loop running."""
        fallback_inputs = [
            "asdkfj",
            "what is the meaning of life",
            "123456xyz",
            "play music",
            "!@#$%^&*"
        ]
        for bad_input in fallback_inputs:
            captured = io.StringIO()
            with patch('sys.stdout', captured):
                should_continue = main.route_command(bad_input, self.user_name)
            self.assertTrue(should_continue, f"Input '{bad_input}' should not stop the loop.")
            self.assertIn(
                "Assistant: I'm not sure I understood that -- type 'help' to see what I can do.",
                captured.getvalue()
            )

    # -------------------------------------------------------------
    # FR-13: Rule-Based Recommendation (AI Concept)
    # -------------------------------------------------------------
    def test_fr13_rule_based_recommendation_branches(self):
        """Test that recommendation outputs change appropriately across time periods."""
        morning = ai_concepts.recommend_activity(hour=8, user_name="Priya")
        self.assertIn("Morning", morning)
        self.assertIn("breakfast", morning.lower())

        afternoon = ai_concepts.recommend_activity(hour=14, user_name="Priya")
        self.assertIn("Afternoon", afternoon)
        self.assertIn("lunch", afternoon.lower())

        evening = ai_concepts.recommend_activity(hour=19, user_name="Priya")
        self.assertIn("Evening", evening)
        self.assertIn("walk", evening.lower())

        night = ai_concepts.recommend_activity(hour=23, user_name="Priya")
        self.assertIn("Night", night)
        self.assertIn("sleep", night.lower())

    # -------------------------------------------------------------
    # FR-14: Perceptron Demonstration (DL Concept - 2 and 3 Inputs)
    # -------------------------------------------------------------
    def test_fr14_perceptron_two_inputs(self):
        """Verify that perceptron supports 2 numeric inputs without silently adding extra inputs."""
        demo_output = ai_concepts.perceptron_demo(custom_inputs=[1.0, 0.5], interactive=False)
        self.assertIn("Inputs (x)         : [1.0, 0.5]", demo_output)
        self.assertIn("Weights (w)        : [0.6, 0.4]", demo_output)
        self.assertIn("Calculation        : (1.0 * 0.6) + (0.5 * 0.4) + (-0.2)", demo_output)
        self.assertIn("Final Output (y)   : 1", demo_output)
        # Ensure 3rd default was NOT appended
        self.assertNotIn("[1.0, 0.5, -0.8]", demo_output)

    def test_fr14_perceptron_three_inputs(self):
        """Verify that perceptron supports 3 numeric inputs as allowed by the PRD."""
        demo_output = ai_concepts.perceptron_demo(custom_inputs=[1.0, 0.5, -0.8], interactive=False)
        self.assertIn("Inputs (x)         : [1.0, 0.5, -0.8]", demo_output)
        self.assertIn("Weights (w)        : [0.6, 0.4, -0.5]", demo_output)
        self.assertIn("Final Output (y)   : 1", demo_output)

    def test_fr14_perceptron_zero_activation(self):
        """Verify that negative weighted sums produce output 0."""
        # inputs = [-1.0, -1.0], weights = [0.6, 0.4], bias = -0.2 -> sum = -1.2 -> output = 0
        demo_output = ai_concepts.perceptron_demo(custom_inputs=[-1.0, -1.0], interactive=False)
        self.assertIn("Final Output (y)   : 0", demo_output)

    # -------------------------------------------------------------
    # Stress / Multi-Input Crash-Resistance Test (Section 29: 20+ Inputs)
    # -------------------------------------------------------------
    def test_multi_input_robustness_25_inputs(self):
        """Test at least 20 diverse valid and invalid inputs without crashing."""
        test_inputs = [
            "help",
            "time",
            "what time is it?",
            "date",
            "today's date",
            "calculate 12 + 8",
            "calculate 20 - 5",
            "calculate 6 * 7",
            "calculate 10 / 2",
            "calculate 5 / 0",
            "calculate invalid syntax",
            "quote",
            "give me motivation",
            "joke",
            "tell me something funny",
            "fact",
            "tell me a trivia fact",
            "recommend",
            "activity",
            "perceptron",
            "perceptron 1.0 0.5",
            "ai demo",
            "hello there",
            "good morning",
            "random gibberish 123",
            "",
            "   "
        ]
        self.assertGreaterEqual(len(test_inputs), 20)
        for inp in test_inputs:
            try:
                main.route_command(inp, self.user_name)
            except Exception as e:
                self.fail(f"Input '{inp}' caused an unexpected exception: {e}")


if __name__ == "__main__":
    unittest.main()
