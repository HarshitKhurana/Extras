"""
    Provided data-type of argument.
    Provided data-type of return value.
    Provided data-type of local variable being used.

    This should run way faster than sumToN_C2 sumToN_C2 , simply because in this we have type defined the variable whose data-types is actually being calculated for a ot of times namelu 'ans' and 'i'.
"""
cpdef int mainFunc(int n):
    cdef int ans = 0 
    cdef int i = 0
    for i in range(n):
        ans += i
    return ans

