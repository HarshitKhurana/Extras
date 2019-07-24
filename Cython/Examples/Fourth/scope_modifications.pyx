
# Extension Type example

cdef class Student:
    # cdef block containing attributes of the class.
    # Note : All attributes must be declared at compile-time only (since it internally uses C-structs)
    cdef: 
    # data-type variableName
        cdef public str _name               # Accessible in python code - readable/writable
        cdef readonly int _rollNumber       # Accessible in python code - readable only cannot modify
        str _favSubject
        int _age
        
    # Creating object with the before-mentioned attributes 
    def __init__ ( self , str name , str favSubject , int age , int rollNumber):
        self._name = name
        self._favSubject = favSubject
        self._age = age
        self._rollNumber = rollNumber

# In the python code we can access only 2 attributes i.e '_name' and '_rollNumber' with the access level as mentioned above.

# For using this class in `student.py` a simple python module, import as :
    #   cimport student                                                                                                                                                      
    #   import student                                                                                                                                                      
