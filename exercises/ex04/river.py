"""File to define River class."""

__author__: str = "730652862"


from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River where aninmals live."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Gets ride of old animals."""
        b: int = 0
        while b < len(self.bears):
            if self.bears[b].age > 5:
                self.bears.pop(b)
                b += 1
            else:
                b += 1

        f: int = 0
        while f < len(self.fish):
            if self.fish[f].age > 3:
                self.fish.pop(f)
                f += 1
            else:
                f += 1
        return None

    def bears_eating(self):
        """Bears eats so it gets ride of 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Check Hunger Score of Bear."""
        gr: int = 0
        while gr < len(self.bears):
            if self.bears[gr].hunger_score < 0:
                self.bears.pop(gr)
                gr += 1
            else:
                gr += 1
        return None

    def repopulate_bears(self):
        """Every pair of bears you get one baby."""
        new_bears = len(self.bears) // 2
        count = 0
        while count < new_bears:
            self.bears.append(Bear())
            count += 1
        return None

    def repopulate_fish(self):
        """Each pair of fish gets 4 baby fishy."""
        new_fish = (len(self.fish) // 2) * 4
        count = 0
        while count < new_fish:
            self.fish.append(Fish())
            count += 1
        return None

    def view_river(self):
        """Current View of the River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulating a Week in the River by run one_river_day 7 times."""
        days_passed: int = 0
        while days_passed < 7:
            self.one_river_day()
            days_passed += 1
        return None

    def remove_fish(self, amount: int):
        """Remove Fish from River."""
        while amount > 0 and self.fish:
            self.fish.pop(0)
            amount -= 1
        return None
