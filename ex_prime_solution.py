"""
Your task: Check if a given number is a prime number

"""


def check_prime(number):
    """
    Return True, if prime number, otherwise return False
    """
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

if __name__ == '__main__':
    print(check_prime(12))  # not prime number
    print(check_prime(15))  # not prime number
    print(check_prime(3))  #  prime number
