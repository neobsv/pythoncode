from typing import List

def word_break(s: str, word_dict: List[str]) -> bool:
    """
    For each index i, run another index j from 0..i to check if each word s[j..i] is in the 
    given list of words or not, if it is, then add its index to the list of breaks (signifying 
    the last successful word that was formed. T[i] would then be the AND of T[j] && (s[j..i] is a word?).
    If it is, then append the index to the list of breaks as well, so that ‘j’ can traverse the array quicker.
    """

    T = [ False for i in range(len(s) + 1) ]
    T[0] = True
    breaks = [0]

    for i in range(1, len(s) + 1):
        for j in reversed(breaks):
            is_word = True if s[j:i] in word_dict else False
            T[i] = T[j] and is_word
            if is_word == True:
                breaks.append(i)
                break
    return T[-1]

if __name__ == '__main__':
    print(f" word_break '', []: { word_break('', []) } ")
    print(f" word_break ' ', []: { word_break(' ', []) } ")
    print(f" word_break 'catsanddog', []: { word_break('catsanddog', []) } ")
    print(f" word_break 'catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']: { word_break('catsanddog', ['cats', 'dog', 'sand', 'and', 'cat']) } ")
    print(f" word_break 'applepenapple', ['apple', 'pen']: { word_break('applepenapple', ['apple', 'pen']) }")
    print(f" word_break 'leetcode', ['leet', 'code']: { word_break('leetcode', ['leet', 'code']) } ")