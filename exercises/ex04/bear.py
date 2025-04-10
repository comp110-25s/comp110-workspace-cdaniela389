"""File to define Bear class."""


class Bear:
    """Bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initulizing Bears."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Bears getting 1 day older."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bears eating to not be hungry."""
        self.hunger_score += num_fish
        return None
