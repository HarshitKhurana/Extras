
# Extension Type example

cdef class Student:
    # cdef block containing attributes of the class.
    # NOTE : All attributes must be declared at compile-time only (since it internally uses C-structs)
    cdef: 
    # data-type variableName
        str _name
        str _favSubject
        int _age
        int _rollNumber
        
    # Creating object with the before-mentioned attributes 
    def __init__ ( self , str name , str favSubject , int age , int rollNumber):
        self._name = name
        self._favSubject = favSubject
        self._age = age
        self._rollNumber = rollNumber

    @property
    def get_name(self):
        return self._name

    @property
    def get_favSubject(self):
        return self._favSubject

    @property
    def get_age(self):
        return self._age

    # Note : since we haven't declared a property for `_rollNumber` thus it won't be accessible in the python space.

# For using this class in `student.py` a simple python module, import as :
    #   from student cimport student                                                                                                                                                      
