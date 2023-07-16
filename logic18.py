def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """ #1 2 3 4 5
    return a%10 > a//10%10 > a//100%10 > a//1000%10 > a//10000
print(main(75421))
print(main(12347))