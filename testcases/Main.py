"""Simple interactive example program."""

from __future__ import annotations


def ask_name() -> str:
    """Prompt the user for their name and return it."""
    return input("What is your name? ").strip()


def ask_integer(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Please enter a valid integer.")


def double(n: int) -> int:
    """Return twice the given number."""
    return n * 2


def main() -> None:
    """Run the interactive flow."""
    print("Hello, welcome to this example program.")
    name = ask_name()
    print(f"Nice to meet you, {name}!")

    number = ask_integer("Give me a number and I will double it: ")
    print(f"Double of {number} is {double(number)}")

    # Keep as plain strings to avoid 'f-string-without-interpolation' warning
    print("NEW CHANGE 2")
    print("PR AND PUSH TO MAIN")
    print("Testing Updating PR")
    print("MAKE FILE TEST V5")


if __name__ == "__main__":
    main()
