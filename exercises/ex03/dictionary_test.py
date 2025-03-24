"""Test Functions Here"""

__author__: str = "730652862"


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert_blank() -> None:
    # What happens when there is a blank dictionary
    assert invert({}) == {}


def test_invert_two() -> None:
    # What happens when there is two items
    assert invert({"a": "apple", "b": "banana"}) == {"apple": "a", "banana": "b"}


def test_invert_three() -> None:
    # What happens when there is 3 items
    assert invert({"a": "apples", "b": "banana", "c": "carrots"}) == {
        "apples": "a",
        "banana": "b",
        "carrots": "c",
    }


def test_count_blank() -> None:
    # What happens with a blank list
    assert count([]) == {}


def test_count_two() -> None:
    # What totals with two items
    assert count(["red", "red"]) == {"red": 2}


def test_count_mult_total() -> None:
    assert count(["red", "blue", "red", "orange", "blue"]) == {
        "red": 2,
        "blue": 2,
        "orange": 1,
    }


def test_favorite_color_blank() -> None:
    assert favorite_color({}) == "N/A"


def test_favoite_color_doubles() -> None:
    assert (
        favorite_color(
            {
                "Bobby": "red",
                "Jeff": "blue",
                "Jane": "red",
                "Tom": "orange",
                "Buzz": "blue",
            }
        )
        == "red"
    )


def test_favorite_color_norm() -> None:
    assert (
        favorite_color(
            {
                "Bobby": "red",
                "Jeff": "blue",
                "Jane": "red",
            }
        )
        == "red"
    )


def test_bin_len_blank() -> None:
    assert bin_len([]) == {}


def test_bin_len_one_cate() -> None:
    assert bin_len(["red", "bae", "two"]) == {3: {"red", "bae", "two"}}


def test_bin_len_two_cate() -> None:
    assert bin_len(["red", "bae", "two", "five", "lips"]) == {
        3: {"red", "bae", "two"},
        4: {"five", "lips"},
    }
