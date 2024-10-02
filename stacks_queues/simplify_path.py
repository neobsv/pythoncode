def simplifyPath(path) -> str:
    """
    use a stack!!!, then mark duplicates for deletion
    """
    # tokenize the path using '/'
    tokens = list(filter(lambda x: x != '', path.split('/') ))
    token_stack = []
    
    for token in tokens:
        if token == '.':
            continue
        elif token == '..' and len(token_stack) > 0:
            token_stack.pop()
        else:
            if token not in set(['.', '..']):
                token_stack.append(token)

    print(f'tokens: {tokens}')
    print(f'token_stack: {token_stack}')
    
    res = "/"
    for token in token_stack:
        res += token + '/'
    
    # scan for double slash in res, and mark them for deletion
    mark = []
    for i in range(len(res)):
        if res[i-1] == '/' and res[i] == '/':
            mark.append(i)
    res = ''.join([ res[i] for i in range(len(res)) if i not in mark ])
    
    return '/' + res[:-1]

if __name__ == '__main__':
    print(f' simplify_path "/home/a/./x/../b//c/" : { simplifyPath("/home/a/./x/../b//c/") }  ')