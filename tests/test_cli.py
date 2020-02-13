import re

import pytest
import typer

from roll_the_dice.cli import roll_string, roll_num


def test_roll_from_str(capsys):
    roller = roll_string(dice_str="2D6", rolls=True)
    stdout = capsys.readouterr().out

    regex = re.compile(
        r"rolling (\d+D\d+)!\n\nyour roll: (\d+)\n\nmade up of (\[[\d, ]+\])"
    )

    roll_str, total, individuals = re.search(regex, stdout).groups()
    assert roll_str == "2D6"
    assert int(total) in range(1, 13)
    assert individuals


def test_roll_bad_str(capsys):
    with pytest.raises(typer.Exit) as e:
        _ = roll_string(dice_str="foo")


def test_roll_num(capsys):
    # need to provide these kwargs to override the `typer.Option` fields
    roller = roll_num(num_dice=1, sides=20)
    stdout = capsys.readouterr().out

    regex = re.compile(r"rolling (\d+D\d+)!\n\nyour roll: (\d+)")

    roll_str, total = re.search(regex, stdout).groups()
    assert roll_str == "1D20"
