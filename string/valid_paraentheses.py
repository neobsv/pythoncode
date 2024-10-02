
def is_valid(s: str) -> bool:
    stack = []
    match = {')':'(', ']':'[', '}':'{'}

    for c in s:
        if c in ('(', '[', '{'):
            stack.append(c)
        elif c in (')', ']', '}'):
            if len(stack) > 0 and stack[-1] == match[c]:
                stack.pop()
            else:
                return False
        else:
            return False

    return False if len(stack) > 0 else True

if __name__ == '__main__':
    print(f' is_valid: { is_valid(str("")) }  ')
    print(f' is_valid: { is_valid(str("{[(()]}")) }  ')
    print(f' is_valid: { is_valid(str("{[(())]}")) }  ')