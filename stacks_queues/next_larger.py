from typing import List

def nextLarger(a) -> List[int]:
    res = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] > a[i]:
                res.append(a[j])
                break
        else:
            res.append(-1)
    return res

if __name__ == '__main__':
    print(f" nextLarger [6, 7, 3, 8]: { nextLarger([6, 7, 3, 8]) } ")