cimport student_extensionType_decleration
# Extension Type example

# Definition i.e implementation of what is defined in the header file is here, same as the ".c/.cpp" for corresponding ".h" files in C/C++

cdef class Student:
        
    # Creating object with the attributes defined in student_extensionType_decleration.pxd
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
    #   from student_extensionType_segregated cimport student

