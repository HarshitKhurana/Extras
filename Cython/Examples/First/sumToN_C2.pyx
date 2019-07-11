"""
    Provided data-type of argument and modified function definition to cpdef.
"""
cpdef mainFunc(int n):
    ans = 0 
    for i in range(n):
        ans += i
    return ans

