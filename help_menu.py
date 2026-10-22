"""
help_menu.py
============
Module responsible for formatting and displaying the help menu
listing all commands supported by NOVA.

PRD Compliance:
- FR-10: Display a help menu listing all supported commands.
"""


def get_help_text() -> str:
    """
    Returns the formatted text listing all supported commands and their descriptions.

    Returns:
        str: Multiline help guide.
    """
    help_lines = [
        "Assistant: Supported commands:",
        "  - time            show current time",
        "  - date            show current date",
        "  - calculate       perform basic arithmetic (+, -, *, /)",
        "  - quote           return a motivational quote",
        "  - joke            tell a humorous programming/general joke",
        "  - fact            share an interesting tech/science fact",
        "  - game            play the number guessing game (1-20)",
        "  - recommend       get a rule-based activity recommendation",
        "  - perceptron      demonstrate an artificial neuron calculation",
        "  - help            display this help menu",
        "  - exit            quit the assistant cleanly",
    ]
    return "\n".join(help_lines)


def print_help() -> None:
    """
    Prints the formatted help menu to standard output.
    """
    print(get_help_text())
