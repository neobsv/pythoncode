def convert(s: str, numRows: int) -> str:
    """
    Keep a counter that controls whether you increment or decrement, so when 
    you are at index '0' then set it to increment, so you go down toward the bottom 
    row. Then when you hit the bottom row, set the counter to decrement, so it goes 
    back up to the top row. The direction of the 'step' counter takes care of 
    generating the zig zag pattern.
    """
    if ( numRows == 1 ) or ( numRows >= len(s) ):
        return s
    
    mat = [""]*(numRows)
    index, step = 0, 1
    for c in s:
        mat[index] += c
        if index == 0:
            step = 1
        elif index == numRows-1:
            step = -1
        index += step
    
    return ''.join(mat)

if __name__ == '__main__':
    print(f' zigzag "PAYPALISHIRING": { convert("PAYPALISHIRING", 4) } ')