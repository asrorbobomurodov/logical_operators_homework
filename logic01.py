def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    if b>a and b<c:
        return True
    else:
        return False
    
print(main(4,5,6))
print(main(6,4,5))
    