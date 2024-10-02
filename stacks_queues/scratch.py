from typing import List

def nearestGreater(a: List[int]) -> List[int]:
    res = []
    for i in range(len(a)):
        cand = []
        j, k = i-1, i+1
        while ( j >= 0 ):
            if ( a[j] > a[i] ):
                cand.append(( a[j], j ))
                break
            j -= 1
        while ( k < len(a) ):
            if ( a[k] > a[i] ):
                cand.append(( a[k], k ))
                break
            k += 1
        cand = sorted(cand, key=lambda x: x[0])
        print(f"key: { a[i] } cand: { cand } ")
        if len(cand) > 0:
            res.append(cand[0][1])
        else:
            res.append(-1)
    return res

if __name__ == '__main__':
    print(f" nearestGreater [1, 4, 2, 1, 7, 6] : { nearestGreater([1, 4, 2, 1, 7, 6]) } ")