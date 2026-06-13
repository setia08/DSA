def is_palindrome(s):
    length = len(s)

    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False

    return True

def __main__():
    print(is_palindrome("abba"))  # True
    print(is_palindrome("race a car"))  # False

__main__()