def strStr(haystack: str, needle: str) -> int:
    """
    Check if haystack[i:i+len(needle)] == needle, at which point we
    return i, to indicate the presence of the word needle in haystack.
    """
    if ( needle == haystack ):
        return 0
    
    if ( len(haystack) == 0 ) or ( len(needle) == 0 ):
        return 0
    
    res = -1
    for i in range(len(haystack)):
        if needle == haystack[i:i+len(needle)]:
            return i

    return res

if __name__ == '__main__':
    print(f' strStr "hello", "ll": { strStr("hello", "ll") }  ')
    print(f' strStr "aaaaaa", "bba": { strStr("aaaaaa", "bba")}  ')