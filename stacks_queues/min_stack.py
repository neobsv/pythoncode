from typing import List

class MinStack:
    """
    Maintain a separate min stack which holds the smallest element seen so far. 
    Then the min command can return only the top of this min stack.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, x: int):
        if len(self.min_stack) > 0:
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)
        self.stack.append(x)
    
    def pop(self) -> int:
        if len(self.stack) > 0 and len(self.min_stack) > 0: 
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
                return self.stack.pop()
            else:
                return self.stack.pop()
        elif len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1
    
    def min(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return -1

def minimumOnStack(operations: List[str]) -> List[int]:
    ms = MinStack()
    res = []
    for op in operations:
        if op[:4] == "push":
            num = int(op[5:])
            ms.push(num)
        elif op == "pop":
            ms.pop()
        elif op == "min":
            res.append(ms.min())
    return res

if __name__ == '__main__':
    operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]
    print(f'min stack ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]: { minimumOnStack(operations) } ')


