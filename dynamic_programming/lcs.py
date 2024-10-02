

def longest_common_subsequence(s1: str, s2: str) -> int:
    T = [ [ 0 for i in range(len(s2) + 1) ] for j in range(len(s1) + 1) ]

    if ( len(s1) == 0 ) or ( len(s2) == 0 ):
        return 0

    if len(s1)==1 and len(s2)==1:
        return 1 if s1[0]==s2[0] else 0
        
    if len(set(s1))==1 and len(set(s2))==1:
        return len(s1) if s1[0]==s2[0] else 0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])

    return T[-1][-1]

if __name__ == '__main__':
    print(f"  longest_common_subsequence 'abcd', 'abxy': { longest_common_subsequence('abcd', 'abxy')  }")
    print(f"  longest_palindromic_subsequence 'cbbd': { longest_common_subsequence('cbbd', 'dbbc')  }")
    print(f"  longest_palindromic_subsequence 'bbbab': { longest_common_subsequence('bbbab', 'babbb')  }")