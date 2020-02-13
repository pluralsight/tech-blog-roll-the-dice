import typer

from .dice import roll, roll_from_string

app = typer.Typer()


@app.command("hello")
def hello_world():
    """our first CLI with typer!
    """
    typer.echo("Opening blog post...")
    typer.launch(
        "https://pluralsight.com/tech-blog/python-cli-utilities-with-poetry-and-typer"
    )


@app.command("roll-str")
def roll_string(
    dice_str: str,
    rolls: bool = typer.Option(
        False, help="set to display individual rolls", show_default=True
    ),
):
    """Rolls the dice from a formatted string.

    We supply a formatted string DICE_STR describing the roll, e.g. '2D6'
    for two six-sided dice.
    """
    try:
        rolls_list, total, formatted_roll = roll_from_string(dice_str)
    except ValueError:
        typer.echo(f"invalid roll string: {dice_str}")
        raise typer.Exit(code=1)

    typer.echo(f"rolling {formatted_roll}!\n")
    typer.echo(f"your roll: {total}\n")
    if rolls:
        typer.echo(f"made up of {rolls_list}\n")


@app.command("roll-num")
def roll_num(
    num_dice: int = typer.Option(
        1, "-n", "--num-dice", help="number of dice to roll", show_default=True, min=1
    ),
    sides: int = typer.Option(
        20, "-d", "--sides", help="number-sided dice to roll", show_default=True, min=1
    ),
    rolls: bool = typer.Option(
        False, help="set to display individual rolls", show_default=True
    ),
):
    """Rolls the dice from numeric inputs.

    We supply the number and side-count of dice to roll with option arguments.
    """
    rolls_list, total = roll(num_dice=num_dice, sides=sides)

    typer.echo(f"rolling {num_dice}D{sides}!\n")
    typer.echo(f"your roll: {total}\n")
    if rolls:
        typer.echo(f"made up of {rolls_list}\n")


def main():
    app()
