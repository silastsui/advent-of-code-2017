def dec1a(num):
    """
    Args:
        num (str): input number
    """
    
    return sum(int(num[x]) for x in range(-1, len(num)-1) if num[x] == num[x+1])

def dec1b(num):
    """
    Args:
        num (str): input number
    """

    k = len(num)//2
    return 2*sum(int(num[x]) for x in range(k) if num[x] == num[x+k])
