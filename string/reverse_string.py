def reverse_string(s: str) -> str:
    """
    Swap chars from begining and end of string, all the way
    till the middle.
    """
    s = [ c for c in s ]
    i, j = 0, len(s)-1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i, j = i+1, j-1
    return ''.join(s)

if __name__ == '__main__':
    print(f' reverse_string "": { reverse_string("") } ')
    print(f' reverse_string "abc": { reverse_string("abc") } ')
    print(f' reverse_string "abbc": { reverse_string("abbc") } ')