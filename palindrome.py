from audioop import reverse


def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    var1 = value.replace(" ", "")
    var1 = var1.lower()
    var_rev = var1[::-1]


    if var1 == var_rev:
        return True
    else:
        return False


#