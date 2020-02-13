import pytest

from roll_the_dice.dice import roll, roll_from_string, parse_dice_string


def test_roll():
    dice_rolls, dice_roll = roll(num_dice=1, sides=20)
    valid_rolls = range(1, 21)
    assert dice_roll in valid_rolls
    assert all([r in valid_rolls for r in dice_rolls])
    assert len(dice_rolls) == 1


def test_roll_from_string():
    dice_rolls, dice_roll, formatted_str = roll_from_string("1D6")
    valid_rolls = range(1, 7)
    assert dice_roll in valid_rolls
    assert all([r in valid_rolls for r in dice_rolls])
    assert len(dice_rolls) == 1


def test_parse_single():
    assert parse_dice_string("D20") == (1, 20)


def test_parse_multi():
    assert parse_dice_string("2D6") == (2, 6)


def test_parse_more_digits():
    assert parse_dice_string("10D100") == (10, 100)


def test_parse_multi_strings():
    assert parse_dice_string("2D6+2D8") == (2, 6)


def test_parse_lower():
    assert parse_dice_string("d20") == parse_dice_string("D20")


def test_bad_parse():
    with pytest.raises(ValueError):
        parse_dice_string("foo")
