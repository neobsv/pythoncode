def reverse_vowels(s: str) -> str:
    indices, s = [], [ c for c in s ]

    for i in range(len(s)):
        if s[i] in "aeiou":
            indices.append(i)

    indices.reverse()

    i, j = 0, len(indices) - 1
    while i < j:
        s[indices[i]], s[indices[j]] = s[indices[j]], s[indices[i]]
        i, j = i+1, j-1

    return ''.join(s)

if __name__ == '__main__':
    print(f' reverse_vowels "hello": { reverse_vowels("hello") } ')
    print(f' reverse_vowels "prolific": { reverse_vowels("prolific") } ')