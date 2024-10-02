def is_palindrome(s: str) -> bool:
    s = [ c.lower() for c in s if c.isalnum() ]
    return s == s[::-1]

if __name__ == '__main__':
    print(f' is_palindrome "": {is_palindrome("")} ')
    print(f' is_palindrome "abba": {is_palindrome("abba")} ')
    print(f' is_palindrome "a011s": {is_palindrome("a011s")} ')
