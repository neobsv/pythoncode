from typing import List

def plusOne(digits: List[int]) -> List[int]:
    """
    Reverse the array, and add digit by digit. Emulate a carry adder, 
    which uses two variables, sum and carry, initially set carry=1 (to emulate the +1) 
    and if the current digit sum is greater than 9, set carry to s//10, otherwise set 
    carry to 0. Proceed till the end of the array.
    """
    digits = digits[::-1]
    
    s = 0
    c = 1
    for i in range(len(digits)):
        s = digits[i] + c 
        if s>9:
            digits[i] = s%10
            c = s//10
        else:
            digits[i] = s
            c = 0
    
    if c > 0:
        digits.append(c)
        return digits[::-1]
    else:
        return digits[::-1]

if __name__ == '__main__':
    print(f' add one [9, 9, 9]: { plusOne([9, 9, 9]) } ')
    print(f' add one [1, 0, 1]: { plusOne([1, 0, 1]) } ')
    print(f' add one [9, 9]: { plusOne([9, 9]) } ')
    print(f' add one [0, 9]: { plusOne([0, 9]) } ')