from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Prefix and suffix products, meaning, prefix: output[i] = … A[i-3]*A[i-2]*A[i-1] which is stored in ‘p’. 
    Then do a reverse pass with output[i] = A[i+1]*A[i+2]* …  
    This gives us, output[i] = … A[i-3]*A[i-2]*A[i-1]*A[i+1]*A[i+2]* … 

    """
    output = [1]*len(nums)
    
    p = 1
    for i in range (len(nums)):
        output[i] = output[i]*p
        p= p*nums[i]
    
    p  = 1
    for i in range(len(nums)-1, -1,-1):
        output[i] = output[i]*p
        p= p*nums[i]
    
    return output

if __name__ == '__main__':
    print(f'  product_except_self [1, 2, 3, 4]: { productExceptSelf([1, 2, 3, 4]) } ')