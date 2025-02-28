"""My third Excerise in COMP110"""

__author__: str = "730652862"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_count: int = 0
    expected_length: int = len(secret)
    while turn_count < 6:
        turn_count += 1
        print(f"=== Turn {turn_count}/6 ===")
        guess = input_guess(expected_length)
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            print(f"You won in {turn_count}/6 turns!")
            return
    print(f"X/6 - Sorry, try again tomorrow!")


def contains_char(search_here: str, target: str) -> bool:
    """To Search for target within search"""
    assert len(target) == 1, f"len('{target}') is not 1"
    index = 0
    while index < len(search_here):
        if search_here[index] == target:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    """Checking for letters from the guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    result = ""
    index = 0

    while index < len(guess):
        if secret[index] == guess[index]:
            result += GREEN_BOX
        elif secret[index] != guess[index]:
            if contains_char(secret, guess[index]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        index += 1
    return result


def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word:")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    return guess


if __name__ == "__main__":
    main(secret="codes")
