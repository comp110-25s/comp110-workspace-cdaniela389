"""My Second Exercise in COMP 110"""

__author__: str = "730653862"


def main_planner(guests: int) -> None:
    """Entrypoint of program"""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost:",
        "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        ),
    )
    return None


def tea_bags(people: int) -> int:
    """To calculate number of tea bags!"""
    return 2 * people


def treats(people: int) -> int:
    """Calculate number of treats!"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate cost of tea bags and treats!"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
