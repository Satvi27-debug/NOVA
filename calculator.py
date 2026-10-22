"""
calculator.py
=============
Module responsible for parsing basic arithmetic expressions and performing
calculations without using dangerous functions like eval().

PRD Compliance:
- FR-05: Perform basic arithmetic (add, subtract, multiply, divide) on request.
- Handles division by zero gracefully.
- Rejects non-numeric/malformed input without crashing.
"""

import re
from typing import Tuple, Optional


def calculate(num1: float, operator: str, num2: float) -> str:
    """
    Performs the basic arithmetic operation between two numbers.

    Args:
        num1 (float): The first operand.
        operator (str): Arithmetic operator (+, -, *, /).
        num2 (float): The second operand.

    Returns:
        str: Formatted result string or error message.
    """
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "I can't divide by zero -- try a different number."
        result = num1 / num2
    else:
        return f"Unsupported operator '{operator}'. Please use +, -, *, or /."

    # Format result: convert 20.0 to 20 for cleaner display
    if isinstance(result, float) and result.is_integer():
        formatted_result = int(result)
    else:
        formatted_result = round(result, 4)

    return f"The result is {formatted_result}"


def _extract_operands_and_operator(text: str) -> Optional[Tuple[float, str, float]]:
    """
    Safely extracts two numbers and an operator from text without using eval().
    Supports integers, decimals, and negative numbers.
    Example valid formats: '12 + 8', '-5 * 3.5', '100 / 4', '5-2'

    Returns:
        Tuple[float, str, float] if valid, None otherwise.
    """
    # Regex to capture: (number) (operator) (number)
    # Number can be positive or negative, integer or float.
    pattern = r"^\s*([+-]?\d+(?:\.\d+)?)\s*([\+\-\*\/])\s*([+-]?\d+(?:\.\d+)?)\s*$"
    match = re.match(pattern, text)
    if match:
        try:
            n1 = float(match.group(1))
            op = match.group(2)
            n2 = float(match.group(3))
            return n1, op, n2
        except ValueError:
            return None
    return None


def parse_expression(expr_str: str) -> str:
    """
    Parses user calculation command or arithmetic expression and computes result.

    Args:
        expr_str (str): Input string, e.g. 'calculate 12 + 8' or '12 + 8'.

    Returns:
        str: Assistant response message.
    """
    cleaned = expr_str.strip()

    # Remove leading 'calculate' or 'calc' command prefix if present
    lower_cleaned = cleaned.lower()
    if lower_cleaned.startswith("calculate"):
        cleaned = cleaned[len("calculate"):].strip()
    elif lower_cleaned.startswith("calc"):
        cleaned = cleaned[len("calc"):].strip()

    # If the user only typed "calculate", prompt interactively
    if not cleaned:
        import sys
        if not sys.stdin.isatty():
            return "Assistant: Please specify an expression, e.g., 'calculate 12 + 8'."
        try:
            cleaned = input("Assistant: Enter calculation (e.g., 12 + 8): ").strip()
        except (EOFError, KeyboardInterrupt):
            return "Assistant: Calculation canceled."
        if not cleaned:
            return "Assistant: No expression entered. Try something like 'calculate 12 + 8'."

    parsed = _extract_operands_and_operator(cleaned)
    if parsed is None:
        return (
            "Assistant: Invalid calculation format. "
            "Please provide two numbers and an operator (+, -, *, /), e.g., 'calculate 12 + 8'."
        )

    num1, operator, num2 = parsed
    result_message = calculate(num1, operator, num2)
    return f"Assistant: {result_message}"
