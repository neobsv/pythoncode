def genperms(s):
    if len(s) == 1:
        return [s]
    res = []
    for perm in genperms(s[:-1]):
        for i in range(len(perm)+1):
            res.append(perm[:i] + [s[-1]] + perm[i:])
    return res

if __name__ == '__main__':
    s = "abc"
    print(genperms([x for x in s]))
