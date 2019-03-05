def conv_to_cels(fahr):
    """ (number) -> float

    Return the number of celsius degree to fahrenheit degrees

    """
    return (fahr - 32)*5/9


def conv_to_fahr(cels):
    """ (number) -> float

    Return the number of fahrenheit degree to celsious degrees

    """
    return cels*1.8 + 32
