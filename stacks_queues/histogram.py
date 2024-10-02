from typing import List

def largest_rectangle_histogram(heights: List[int]) -> int:
    """
    The indices of each bar of the histogram are pushed onto the stack, and on each iteration, 
    the left and right boundaries of the histogram at the current index are popped, and the area 
    under the histogram is calculated. Maximize this area across the entire histogram.
    """
    max_area = 0
    stack = []


    for i in range(len(heights)):
        # print(f"i: { i } heights: { heights } stack: { stack }  ")
        while ( len(stack) > 0 ) and ( heights[stack[-1]] >= heights[i] ):
            
            if len(stack) > 0:
                left_b, right_b = stack.pop(), stack[-1]
                max_area = max(max_area, heights[left_b] * ( i - 1 - right_b ) ) 
            else:
                left_b = stack.pop()
                max_area =  max(max_area, heights[left_b] *  i)
            # print(f"max_area: { max_area }")
        stack.append(i)

    while len(stack) > 0:
        if len(stack) > 0:
            left_b, right_b = stack.pop(), stack[-1]
            max_area = max(max_area, heights[left_b] * ( len(heights) - 1 - right_b )  )
        else:
            left_b = stack.pop()
            max_area = max(max_area, heights[left_b] * ( len(heights) ) )
        # print(f"stack: { stack } max_area: { max_area }")

    return max_area


if __name__ == '__main__':
    print(f" largest_rectangle_histogram [2, 1, 5, 6, 2, 3]: { largest_rectangle_histogram([2, 1, 5, 6, 2, 3]) } ")