import re
from typing import Tuple, List
import random


def roll(num_dice: int = 1, sides: int = 20) -> Tuple[List[int], int]:
    """rolls some dice given numeric inputs.

    Args:
        num_dice (optional): number of dice to roll.  Defaults to 1 for a
            single die.
        sides (optional): size of die (e.g, 6 for a D6 die).  Defaults to 20
            rolling a D20.

    Returns:
        sorted (descending) list of individual rolls and their total.
    """
    rolls = sorted(
        [random.choice(range(1, sides + 1)) for _ in range(num_dice)], reverse=True
    )
    return (rolls, sum(rolls))


def parse_dice_string(dice_string: str) -> Tuple[int, int]:
    """parses formatted string to a dice roll, e.g. "2D6" for rolling two
    six-sided dice.

    Args:
        dice_string: formatted string for roll.

    Returns:
        tuple of the count and sides for the roll.

    Raises:
        :py:class:`ValueError`: for bad strings.
    """
    hit = re.search(r"(\d*)[dD](\d+)", dice_string)
    if not hit:
        raise ValueError("bad string")

    count, sides = hit.groups()
    count_int = int(count or 1)
    sides_int = int(sides)
    return (count_int, sides_int)


def roll_from_string(dice_string: str) -> Tuple[List[int], int, str]:
    """rolls dice from a formatted string, e.g. "2D6" for rolling two six-sided
    dice.  Allows skipping the count digit for single rolls, e.g. "D20" and
    "1D20" returns the same.  Will return a cleaned version of the roll s
    string along with the results.

    Args:
        dice_string: formatted string for roll.

    Returns:
        sorted list of dice rolls, their total, and the formatted roll string

    Raises:
        :py:class:`ValueError`: for bad string formats
            (from :py:func:`~roll_the_dice.dice.parse_dice_string`).
    """
    count, sides = parse_dice_string(dice_string)
    rolls, total = roll(num_dice=count, sides=sides)
    return (rolls, total, f"{count}D{sides}")
