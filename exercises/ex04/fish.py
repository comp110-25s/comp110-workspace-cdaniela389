"""File to define Fish class."""


class Fish:
    """Fishes in river."""

    age: int

    def __init__(self):
        """Initulizing Fishes in river."""
        self.age = 0

    def one_day(self):
        """Fishes get one day older."""
        self.age += 1
        return None
