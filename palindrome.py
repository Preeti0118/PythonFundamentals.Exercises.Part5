from audioop import reverse


def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    var_rev = value[::-1]

    if value == var_rev:
        return True
    else:
        return False

