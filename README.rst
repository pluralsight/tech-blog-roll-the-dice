roll-the-dice
=============

Generate random dice rolls from numeric inputs or DND Player's Guide-style roll strings (e.g., "2D6" for rolling two six-sided dice).
Example code for a small Python package built with `poetry` and incorporating an entrypoint to a small command line utility built with `typer`.

Used for the blog post `Python CLI Utilities with Poetry and Typer <https://pluralsight.com/tech-blog/python-cli-utilities-with-poetry-and-typer>`_.

Features
--------

* Generate random rolls from numeric inputs or formatted strings
* builds a CLI utility installable via `pip` for dice rolls from the command line
* code formatting with `black`, `flake8` and `mypy`
* Dockerized build environment

Command-Line Utility
--------------------

The package also builds a command-line utility, `rtd`, that can be used directly from the terminal once `pip`-installed (alternately, it can be run within the `poetry` environment with `poetry run rtd [OPTIONS] COMMAND [ARGS]`).

`rtd roll-str`
^^^^^^^^^^

A command to roll dice from a formatted string.

.. code-block::

    Usage: rtd roll-str [OPTIONS] DICE_STR

      Rolls the dice from a formatted string.

      We supply a formatted string DICE_STR describing the roll, e.g. '2D6' for
      two six-sided dice.

    Options:
      --rolls / --no-rolls  set to display individual rolls  [default: False]
      --help                Show this message and exit.

`rtd roll-num`
^^^^^^^^^^

A command to roll dice from numeric inputs.

.. code-block::

    Usage: rtd roll-num [OPTIONS]

      Rolls the dice from numeric inputs.

      We supply the number and side-count of dice to roll with option arguments.

    Options:
      -n, --num-dice INTEGER RANGE  number of dice to roll  [default: 1]
      -d, --sides INTEGER RANGE     number-sided dice to roll  [default: 20]
      --rolls / --no-rolls          set to display individual rolls  [default:
                                    False]
      --help                        Show this message and exit.

`make` targets
--------------

This package includes a `Makefile` for package build tasks in the Dockerized build environment.
To use them, simply run `make <target>` from the root of the directory:

======= ===============================================
target  task
======= ===============================================
`build` builds the Docker environment for the package
`shell` runs BASH shell in the package Docker container
`test`  runs `pytest` unit testing
`lint`  runs `black`, `flake8`, and `mypy` linting
`wheel` builds a `wheel` file of the package
======= ===============================================

License
-------

This code is licensed under the `Apache 2.0 license <https://github.com/pluralsight/tech-blog-roll-the-dice/blob/master/LICENSE.md>`_.
