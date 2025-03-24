"""Function skeletions"""

__author__: str = "730652862"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        value: str = input_dict[key]
        if value in inverted_dict:
            raise KeyError("Duplicate keys!")
        inverted_dict[value] = key
    return inverted_dict


def count(sample: list[str]) -> dict[str, int]:
    result_dict: dict[str, int] = {}
    for item in sample:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    colors: list[str] = []
    for key in names_and_colors:
        colors.append(names_and_colors[key])

    color_count: dict[str, int] = count(colors)
    fav_color: str = "N/A"
    max_count: int = 0

    for color in color_count:
        total = color_count[color]
        if total > max_count:
            fav_color = color
            max_count = total
    return fav_color


def bin_len(statement: list[str]) -> dict[int, set[str]]:
    length_bins: dict[int, set[str]] = {}

    for key in statement:
        length: int = len(key)
        if length not in length_bins:
            length_bins[length] = set()
        length_bins[length].add(key)
    return length_bins
