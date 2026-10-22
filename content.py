"""
content.py
==========
Module containing predefined collections of motivational quotes, jokes,
and interesting facts, with functions to retrieve random entries.

PRD Compliance:
- FR-06: Return a random motivational quote from a predefined list.
- FR-07: Return a random joke from a predefined list.
- FR-08: Return a random fact from a predefined list.
- Acceptance Criteria: When repeated 5+ times, returns varying items confirming randomness.
"""

import random
from typing import List

QUOTES: List[str] = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "It always seems impossible until it is done. - Nelson Mandela",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Small daily improvements over time lead to stunning results. - Robin Sharma",
    "Failure is simply the opportunity to begin again, this time more intelligently. - Henry Ford",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
]

JOKES: List[str] = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "How do you comfort a JavaScript bug? You console it.",
    "Why was the computer cold? It left its Windows open!",
    "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
    "Why do Python programmers have low self-esteem? Because they're constantly comparing self to others.",
    "Real programmers count from 0.",
]

FACTS: List[str] = [
    "The first computer bug was an actual real moth found trapped inside the Harvard Mark II computer in 1947.",
    "The term 'Artificial Intelligence' was officially coined by John McCarthy at the Dartmouth Conference in 1956.",
    "The Python programming language was named after the British comedy troupe Monty Python, not the snake.",
    "The world's first programmer was Ada Lovelace, who wrote an algorithm for Charles Babbage's Analytical Engine in 1843.",
    "The Apollo 11 guidance computer that landed astronauts on the Moon in 1969 had only 4 KB of RAM.",
    "The first artificial neural network model, the Perceptron, was invented by Frank Rosenblatt in 1958.",
    "The entire internet was once mapped onto a single sheet of paper by ARPANET engineers in 1973.",
    "QWERTY keyboard layout was originally designed in the 1870s to prevent mechanical typewriter jams by spacing out common letter pairs.",
]


def get_random_quote(user_name: str = "") -> str:
    """
    Selects and formats a random motivational quote.

    Args:
        user_name (str, optional): User's name to personalize the response.

    Returns:
        str: Formatted motivational quote response.
    """
    quote = random.choice(QUOTES)
    if user_name and user_name.lower() != "friend":
        return f"Assistant: Here is an inspiring quote for you, {user_name}:\n  \"{quote}\""
    return f"Assistant: Here is your motivational quote:\n  \"{quote}\""


def get_random_joke() -> str:
    """
    Selects and formats a random joke.

    Returns:
        str: Formatted joke response.
    """
    joke = random.choice(JOKES)
    return f"Assistant: {joke}"


def get_random_fact() -> str:
    """
    Selects and formats a random interesting fact.

    Returns:
        str: Formatted fact response.
    """
    fact = random.choice(FACTS)
    return f"Assistant: Did you know? {fact}"
