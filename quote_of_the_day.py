#!/usr/bin/env python3
"""Quote‑of‑the‑Day CLI

A tiny script that prints a random inspirational quote.

Usage:
    python quote_of_the_day.py

The script is deliberately minimal – no external packages are required.
"""

import random
from typing import List

# ---------------------------------------------------------------------------
# 🎯 Quote data – feel free to add more!
# ---------------------------------------------------------------------------
QUOTES: List[str] = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Stay hungry, stay foolish. – Steve Jobs",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "The purpose of our lives is to be happy. – Dalai Lama",
    "What we think, we become. – Buddha",
    "The best way to predict the future is to invent it. – Alan Kay",
]


def get_random_quote() -> str:
    """Return a randomly selected quote from the QUOTES list."""
    return random.choice(QUOTES)


def main() -> None:
    """Entry point for the CLI.

    Prints the chosen quote followed by a newline. The function is tiny but
    isolated to make unit‑testing straightforward.
    """
    quote = get_random_quote()
    print(quote)


if __name__ == "__main__":
    # Instant init – run the CLI immediately when the script is executed.
    main()
