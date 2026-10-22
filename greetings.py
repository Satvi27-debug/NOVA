"""
greetings.py
============
Module responsible for user greeting, identity presentation,
and session-level user name capture.

PRD Compliance:
- FR-01: Greet the user on startup and ask for their name.
- FR-02: Remember user's name for session duration and use in responses.
- Section 4: Project Identity (NOVA).
"""

PROJECT_NAME = "NOVA"
FULL_NAME = "Natural Offline Virtual Assistant"
TAGLINE = "Simple Commands. Smart Responses. Zero Internet."


def get_banner() -> str:
    """
    Returns the formatted ASCII banner presenting NOVA's identity.
    """
    divider = "=" * 62
    banner = (
        f"{divider}\n"
        f"         {PROJECT_NAME} -- {FULL_NAME}\n"
        f"       {TAGLINE}\n"
        f"{divider}"
    )
    return banner


def get_user_name() -> str:
    """
    Greets the user on startup and requests their name.
    If the user enters an empty name or only whitespace,
    defaults gracefully to 'Friend'.

    Returns:
        str: The sanitized user name.
    """
    print(get_banner())
    print(f"Assistant: Hi! I'm {PROJECT_NAME} ({FULL_NAME}). What's your name?")
    try:
        raw_name = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAssistant: Session interrupted. Defaulting name to Friend.")
        return "Friend"

    if not raw_name:
        name = "Friend"
        print(f"Assistant: No name entered! I will call you {name} for this session.")
    else:
        name = raw_name
    return name


def build_greeting(user_name: str) -> str:
    """
    Constructs a personalized welcome message for the user.

    Args:
        user_name (str): The name captured for the current session.

    Returns:
        str: Welcoming message with a hint to type 'help'.
    """
    return (
        f"Assistant: Nice to meet you, {user_name}! Type 'help' to see what I can do."
    )
