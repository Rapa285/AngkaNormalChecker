def champernowne_constant(n):
    """
    Generate the first n digits of Champernowne's constant in base 10.
    
    :param n: Number of digits to generate.
    :return: A string representing the first n digits of Champernowne's constant.
    """
    constant = ''
    # i = 1
    # while len(constant) < n:
    #     constant += str(i)
    #     i += 1
    for i in range(n):
        constant += str(i)
    return constant