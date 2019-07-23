
# Extension Type example
# Only decleration here, same as ".h" files in C/C++

cdef class Student:
    # cdef block containing attributes of the class.
    # NOTE : All attributes must be declared at compile-time only (since it internally uses C-structs)
    cdef: 
    # data-type variableName
        str _name
        str _favSubject
        int _age
        int _rollNumber
        
