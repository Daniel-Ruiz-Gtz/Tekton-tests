"""Prints 'Hello World' greetings in multiple languages."""

from __future__ import annotations


def main() -> None:
    """Print greetings in multiple languages."""
    greetings = [
        "Hello World",        # English
        "Hola Mundo",         # Spanish
        "Bonjour le monde",   # French
        "Hallo Welt",         # German
        "こんにちは世界",        # Japanese
    ]

    for message in greetings:
        print(message)


if __name__ == "__main__":
    main()
