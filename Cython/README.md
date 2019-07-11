### Cython

##### -> Cython is basically Python with C data types, which exists to provide C-like performance.
##### -> The Cython compiler simply converts parts of python program into C code.
##### -> One can simply get performance gains just by defining data-types of functions/variables/iterators. \n Ex:
```
x = 12               # loosely typed variable 
int y = 12           # Strictly typed variable in C
cdef int z = 12      # Strictly typed variable in Cython
```
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;-> The reason for above gain is that since we have not defined the data-type of `x` variable , python has to internally look up for it everytime `x` is used, whereas in case of `y` it simply knows.

##### -> Different types of definitions : 

|S.No| Type    | Explaination                                                                                                                                               |
|----|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------:|
|1.  | def     | regular python function, calls from Python only.                                                                                                           |
|2.  | cdef    | cython only functions, can't access these from python-only code, must access within Cython, since there will be no C translation to Python for these.      |
|1.  | cpdef   | C and Python. Will create a C function and a wrapper for Python. Why not *always* use cpdef? In some cases, you might have C only pointer, like a C array. |


##### -> Can also use C++ with Cython by using the corresponding compiler-directive `# distutils: language=c++` , which tells the cython compiler code to C++.
##### -> Refer to Examples directory for code examples.
##### -> 

### [\*] Requirements
##### -> Cython : `pip install cython`.
##### -> C/C++ Compiler.
