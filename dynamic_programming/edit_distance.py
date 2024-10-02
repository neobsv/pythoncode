
def edit_distance(s1: str, s2: str) -> int:
    T = [ [ 0 for i in range(len(s1) + 1)  ] for j in range(len(s2) + 1)  ]

    for i in range(len(s1) + 1):
        T[0][i] = 1

    for j in range(len(s2) + 1):
        T[j][0] = 1

    T[0][0] = 0
    
    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            if s2[i-1] == s1[j-1]:
                # The cost a no-op is 0, so propagate the same value across the principal diagonal.
                T[i][j] = T[i-1][j-1]
            else:
                # The cost of an insert, delete and replace is 1 plus the min 
                # cost operation needed to transform s1 to s2.
                T[i][j] = 1 + min(T[i-1][j], T[i][j-1], T[i-1][j-1])

    return T[-1][-1]

if __name__ == '__main__':
    print(f"edit_distance : { edit_distance('horse', 'ros') } ")
    print(f"edit_distance : { edit_distance('intention', 'execution') } ")