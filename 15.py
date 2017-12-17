def get_next_val(n, n_factor, multiple):
    "Helper function to find next valid number"
    n = (n*n_factor) % 2147483647
    while n%multiple != 0:
        n = (n*n_factor) % 2147483647
    return n

def dec15a(a, b, a_factor, b_factor):
    """
    Args:
        input_hash (str): input hash
    """
    count = 0
    for _ in range(40000000):
        a = (a*a_factor) % 2147483647
        b = (b*b_factor) % 2147483647
        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1

    return count


def dec15b(a, b, a_factor, b_factor, a_multiple, b_multiple):
    """
    Args:
        input_hash (str): input hash
    """
    count = 0
    for _ in range(5000000):
        a = get_next_val(a, a_factor, a_multiple)
        b = get_next_val(b, b_factor, b_multiple)
        if bin(a)[-16:] == bin(b)[-16:]:
            count += 1

    return count
