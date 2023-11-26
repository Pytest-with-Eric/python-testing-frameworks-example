def check_number(num: str):
    """
    Function to check if the number is negative or positive.
    """
    num = float(num)
    if num >= 0:
        if num == 0:
            return "Zero"
        else:
            return "Positive"
    else:
        return "Negative"

