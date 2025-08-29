"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40  # constant representing the expected bake time in minutes


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return max(0, EXPECTED_BAKE_TIME - elapsed_bake_time)


def preparation_time_in_minutes(layers):
    """Calculate the preparation time.

    :param layers: int - number of layers in the lasagna.
    :return: int - total preparation time in minutes.

    Function that takes the number of layers in the lasagna as an argument
    and returns the total preparation time in minutes. Each layer takes 2 minutes to prepare.
    """
    return layers * 2


def elapsed_time_in_minutes(layers, time):
    """Calculate the elapsed time.

    :param layers: int - number of layers in the lasagna.
    :param time: int - total time spent on preparation and baking.
    :return: int - total elapsed time in minutes.

    Function that takes the number of layers in the lasagna and the total time spent
    on preparation and baking as arguments and returns the total elapsed time in minutes.
    """
    preparation_time = preparation_time_in_minutes(layers)
    return preparation_time + time
