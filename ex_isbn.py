"""
Your task: Check if a given ISBN number is valid. For this, see if the check digit it right.

The check digit (tenth digit) of the ISBN number is calculated as follows:
Multiply the first digit by one, the second digit by two, the third digit by three, and so on until the ninth digit,
which is multiplied by nine.
Add up the products and divide the sum by 11, rounding down to the nearest whole number.

The remainder of the division is the check digit.
If the remainder is 10, the check digit is represented by the letter X.

"""

def check_isbn(isbn):
    return False

if __name__ == '__main__':
    check_isbn('3741611301')  # valid ISBN
    check_isbn('3741611309')  # invalid ISBN
