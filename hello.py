#!/usr/bin/env python3
"""
A robust script that responds to various forms of "hello" input.
Features:
- Case insensitive input matching
- Multiple hello variations
- Exit commands
- Input validation
- Error handling
"""

import sys
import re
from typing import Optional

def normalize_input(user_input: str) -> str:
    """Normalize user input by stripping whitespace and converting to lowercase."""
    if user_input is None:
        return ""
    return user_input.strip().lower()

def is_hello_command(input_text: str) -> bool:
    """Check if input matches various hello patterns."""
    hello_patterns = [
        r'^hello$',
        r'^hi$',
        r'^hey$',
        r'^hello there$',
        r'^good morning$',
        r'^good afternoon$',
        r'^good evening$',
        r'^greetings$',
        r'^salutations$',
        r'^hola$',
        r'^bonjour$',
        r'^hallo$',
        r'^ciao$',
        r'^namaste$'
    ]

    normalized = normalize_input(input_text)

    for pattern in hello_patterns:
        if re.match(pattern, normalized, re.IGNORECASE):
            return True

    return False

def is_exit_command(input_text: str) -> bool:
    """Check if user wants to exit."""
    exit_commands = ['exit', 'quit', 'q', 'bye', 'goodbye', 'stop', 'end']
    normalized = normalize_input(input_text)
    return normalized in exit_commands

def is_help_command(input_text: str) -> bool:
    """Check if user wants help."""
    help_commands = ['help', '?', 'commands', 'info', 'usage']
    normalized = normalize_input(input_text)
    return normalized in help_commands

def show_help() -> None:
    """Display help information."""
    print("\n" + "="*50)
    print("HELLO RESPONSE SCRIPT - HELP")
    print("="*50)
    print("\nThis script responds to various greeting forms.")
    print("\nCommands:")
    print("  Greetings: hello, hi, hey, hello there, good morning,")
    print("            good afternoon, good evening, greetings,")
    print("            salutations, hola, bonjour, hallo, ciao, namaste")
    print("  Help:      help, ?, commands, info, usage")
    print("  Exit:      exit, quit, q, bye, goodbye, stop, end")
    print("\nThe script is case-insensitive and handles extra spaces.")
    print("="*50 + "\n")

def show_greeting(input_text: str) -> None:
    """Display appropriate greeting response."""
    normalized = normalize_input(input_text)

    responses = {
        'hello': "Hello! Welcome!",
        'hi': "Hi there! Nice to see you!",
        'hey': "Hey! How's it going?",
        'hello there': "Hello there! General Kenobi... 😉",
        'good morning': "Good morning! Rise and shine!",
        'good afternoon': "Good afternoon! Hope you're having a great day!",
        'good evening': "Good evening! How was your day?",
        'greetings': "Greetings and salutations!",
        'salutations': "Salutations! A pleasure to meet you!",
        'hola': "¡Hola! Bienvenido!",
        'bonjour': "Bonjour! Comment allez-vous?",
        'hallo': "Hallo! Wie geht's?",
        'ciao': "Ciao! Piacere di conoscerti!",
        'namaste': "Namaste! 🙏"
    }

    # Find matching response
    response = responses.get(normalized, "Hello! Great to see you!")
    print(f"\n🌟 {response} 🌟\n")

def get_user_input() -> Optional[str]:
    """Safely get user input."""
    try:
        return input("Enter something (or 'help' for commands): ")
    except (EOFError, KeyboardInterrupt):
        print("\n\nGoodbye!")
        return None
    except Exception as e:
        print(f"\nError reading input: {e}")
        return None

def main():
    """Main program loop."""
    print("\n" + "="*50)
    print("🚀 HELLO RESPONSE SCRIPT - ENHANCED VERSION 🚀")
    print("="*50)
    print("\nType 'hello' (or variations) to get a response!")
    print("Type 'help' for available commands or 'exit' to quit.\n")

    try:
        while True:
            user_input = get_user_input()

            if user_input is None:
                break

            if not user_input.strip():
                print("Please enter something. Type 'help' for commands.\n")
                continue

            if is_exit_command(user_input):
                print("\nThank you for using the Hello Response Script! 👋")
                print("Goodbye!\n")
                break

            if is_help_command(user_input):
                show_help()
                continue

            if is_hello_command(user_input):
                show_greeting(user_input)
            else:
                print(f"\nYou entered: '{user_input}'")
                print("Try typing 'hello' or similar greetings! Type 'help' for more options.\n")

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye! 👋")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)
# execute this main method to start programmer
if __name__ == "__main__":
    main()