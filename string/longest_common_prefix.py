from typing import List

def longestCommonPrefix(strs: List[str]) -> int:
    for i in range(len(strs)):
        first = strs[0][i]
        for j in range(len(strs)):
            if (i + 1) > len(strs[j]):
                return i
            if strs[j][i] != first:
                return i if i != 0 else -1
    return -1

if __name__ == '__main__':
    print(f' longestCommonPrefix ["flower","flow","flight"]: { longestCommonPrefix(["flower","flow","flight"]) } ')
    print(f' longestCommonPrefix ["dog","racecar","car"]:  {  longestCommonPrefix(["dog","racecar","car"]) } ')