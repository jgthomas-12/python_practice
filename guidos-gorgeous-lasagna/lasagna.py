"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time





def preparation_time_in_minutes(number_of_layers):
    """Calculate the prep time.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - total prep time (in minutes) derived from PREPERATION_TIME

    Function that takes the number of layers in the lasagna as an argument and returns
    the total amount of minutes needed for preparation time based on the
    'PREPARATION_TIME'.
    """
    total_prep_time = PREPARATION_TIME * number_of_layers
    return total_prep_time






def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """"Calculate the elapsed cooking time in minutes.

    :param number_of_layers: int - the number of layers in the lasgna.
    :param elapsed_bake_time: int - amount of time the lasagna's been cooking.
    :return: int - total elapsed cooking time based on total prep time and elapsed bake time

    Function that takes the total preparation time, by using the preparation_time_in_minutes()
    function with number_of_layers as an argument and adds the elapsed bake time to return the
    total amount, in minutes, of time the lasagna's been cooking.
    """
    total_prep_time = preparation_time_in_minutes(number_of_layers)
    elapsed_time = total_prep_time + elapsed_bake_time
    return elapsed_time