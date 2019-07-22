
# Note : We are using 'cimport' here instead of normal import , becuase we are importing from C library.
cimport libc.math                   # Using math header file from C library
from libc.stdlib cimport malloc, free      # C-importing the required functions for memory management.
# Note : We are using 'cimport' here instead of normal import , becuase we are importing from C library.

# cython -a c_functions.pyx : Will generate the HTML doc explaining python interactions of this code.

# Cython function which takes an int argument and returns the answer in python object, after calling the sin function from math library in C.
def csin(double x):
    sin_function = libc.math.sin        # Make the function python callable
    return sin_function(x)


def square_sin(double x):
    # The below line creates a C type variable , we can create a python object(variable) too here, but C is faster.
    cdef double x_square = x * x        
    sin_function = libc.math.sin        # Make the function python callable
    return sin_function(x_square)

# This function uses the C - malloc and free for allocating memory on HEAP
# Remember, python automatically handles memory manangement for you via reference counting but in case of 'C' you have to do it manually. - So don't forget to 'free' the 'malloced' memory.
def allocMemoryAndPrint():

    # LHS : Creating an integer pointer to hold the allocated memory
    # RHS : malloc'ing memory for 10 integer variables and typecasting it ( cython uses '<>' for typecasting unlike C which uses '()') into integer.
    cdef int* c_memory_pointer = <int *>malloc( 10 * sizeof(int))

    # Checking if memory allocated succesfully or not
    if not c_memory_pointer:
        raise MemoryError()     # It's all good, we can raise python exceptions from Cython code because ALL PIECE OF PYTHON CODE IS A VALID CYTHON CODE.
    
    # Keep in mind that we are writing Cython thus we can write python and C as per our requirement.
    try:
        # Cython syntax for accessing first 2 indexes the 'c_memory_pointer' array 
        c_memory_pointer[:2] = [11,12]
        print ("Elements in the C-type int pointer are : {} and {}".format(c_memory_pointer[0] , c_memory_pointer[1]))

        # Remember to ALWAYS FREE the 'malloced' memory 
    finally:
        free (c_memory_pointer)
    return


# This function simply print all the 'key-value' pairs of a dictionary,  where the data-type of the variable i.e 'dictionary' is defined.
def defined_Dictionary():
    cdef dict pyDictDefinedVariable = {}        # defining that this variable will always be a python dictionary.
    cdef int i = 0                              # Statically defined int variable
    cdef str value = "Hello, I am a C string"   # Statically defined string    
    cdef list data = [1,2,3,4,5,6,7,8,9,0]      # Statically defined list
    for i in data:
        pyDictDefinedVariable[i] = str(i)

    print ("The Dictionary(whose type is statically defined) is : ")
    for itr in pyDictDefinedVariable:
        print (itr , " : " , pyDictDefinedVariable[itr])

    print (value)
