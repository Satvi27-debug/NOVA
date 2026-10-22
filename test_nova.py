"""
test_nova.py
============
Comprehensive automated test suite for NOVA (Natural Offline Virtual Assistant).
Validates all Functional Requirements (FR-01 through FR-14), acceptance criteria,
and non-functional reliability requirements.
"""

import unittest
from datetime import datetime
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
        # Check for AM or PM
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
    # FR-09: Number Guessing Game Logic
    # -------------------------------------------------------------
    def test_fr09_game_bounds(self):
        """Verify game settings conform to PRD (1 to 20 range, 5 attempts)."""
        import inspect
        sig = inspect.signature(game.play_guessing_game)
        self.assertEqual(sig.parameters['max_attempts'].default, 5)
        self.assertEqual(sig.parameters['lower_bound'].default, 1)
        self.assertEqual(sig.parameters['upper_bound'].default, 20)

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
    # FR-11: Graceful Exit
    # -------------------------------------------------------------
    def test_fr11_graceful_exit(self):
        """Test that exit commands return False to signal loop termination."""
        for exit_word in ("exit", "quit", "bye", "goodbye"):
            should_continue = main.route_command(exit_word, self.user_name)
            self.assertFalse(should_continue, f"Command '{exit_word}' should signal exit.")

    # -------------------------------------------------------------
    # FR-12: Fallback on Unrecognized Input
    # -------------------------------------------------------------
    def test_fr12_fallback_handling(self):
        """Verify unrecognized inputs do not crash and keep the loop running."""
        fallback_inputs = [
            "asdkfj",
            "what is the meaning of life",
            "123456xyz",
            "play music",
            "!@#$%^&*"
        ]
        for bad_input in fallback_inputs:
            should_continue = main.route_command(bad_input, self.user_name)
            self.assertTrue(should_continue, f"Input '{bad_input}' should not stop the loop.")

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
    # FR-14: Perceptron Demonstration (DL Concept)
    # -------------------------------------------------------------
    def test_fr14_perceptron_calculation(self):
        """Test that perceptron correctly computes forward pass and activation."""
        # Test step activation
        self.assertEqual(ai_concepts.step_activation(1.5), 1)
        self.assertEqual(ai_concepts.step_activation(-0.5), 0)
        self.assertEqual(ai_concepts.step_activation(0.0), 0)

        # Test single neuron calculation
        # inputs = [1.0, 1.0], weights = [0.5, 0.5], bias = -0.8
        # dot_product = 0.5 + 0.5 = 1.0; sum = 1.0 - 0.8 = 0.2 -> output = 1
        res = ai_concepts.calculate_neuron([1.0, 1.0], [0.5, 0.5], -0.8)
        self.assertEqual(res["output"], 1)

        # Test perceptron demo string generation
        demo_output = ai_concepts.perceptron_demo(custom_inputs=[1.0, 0.5, -0.8], interactive=False)
        self.assertIn("Artificial Neuron (Perceptron)", demo_output)
        self.assertIn("Step Function", demo_output)
        self.assertIn("Final Output", demo_output)
        self.assertIn("Hidden Layer Analogy", demo_output)

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
