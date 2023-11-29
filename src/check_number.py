def check_number(num: str):
    """
    Function to check if the number is negative or positive.
    >>> check_number(-2)
    'Negative'
    >>> check_number(0)
    'Zero'
    """
    num = float(num)
    if num >= 0:
        if num == 0:
            return "Zero"
        else:
            return "Positive"
    else:
        return "Negative"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
