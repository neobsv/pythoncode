def numDecodings(s: str) -> int:
    """    
    If the current char is zero, reset the current result to zero else 
    copy the prev. result (i-1th) into the current result.
    
    If the prev. char of the string is 1, then add the i-2th
    answer along with the i-1th answer, and also if the prev. char
    is 2 then verify if the current char is less than '6' and add
    the i-2th result to the current result as well.
    
    """
    T = [ 1 for i in range(len(s)+1) ]
    
    if ( len(s) == 0 ) or ( s[0] == '0' ):
        return 0
   
    for i in range(2, len(s)+1):
        x = i-1

        if s[x]=='0':
            T[i] = 0
        else:
            T[i] = T[i-1]

        if ( s[x-1] == '1' ) or ( ( s[x-1] == '2' ) and ( s[x] <= '6' ) ):
            T[i] += T[i-2]
    
    return max(T)

if __name__ == '__main__':
    print(f' num_decodings "": { numDecodings("") } ')
    print(f' num_decodings "0": { numDecodings("0") } ')
    print(f' num_decodings "12": { numDecodings("12") } ')
    print(f' num_decodings "226": { numDecodings("226") } ')
    print(f' num_decodings "1241442230": { numDecodings("1241442230") } ')