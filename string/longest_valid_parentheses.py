def longestValidParentheses(s: str) -> int:
    """
    For a given string, push and pop the opening and closing parentheses. 
    When the length of the stack becomes zero, right after popping it at 
    some index, calculate the length of the sequence that was just 
    """
    stack = [-1]
    maxlen = 0
    for i,c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) > 0:
                maxlen = max(maxlen, i - stack[-1] )
            else:
                stack.append(i)
    return maxlen

if __name__ == '__main__':
    print(f' longestValidParentheses "": { longestValidParentheses("") } ')
    print(f' longestValidParentheses "(()": { longestValidParentheses("(()") } ')
    print(f' longestValidParentheses "(()())" { longestValidParentheses("(()())") } ')