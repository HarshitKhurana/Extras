## *Cython*

##### -> Cython is basically Python with C data types, which exists to provide C-like performance. 
##### -> The Cython compiler simply converts parts of python program into C code.
##### -> Think of cython as just another compiler (like g++ , clang , javac etc) , which happens to compile the code into python-C API (which in-turn is compiled using C-compilers).
##### -> One can simply get performance gains just by defining data-types of functions/variables/iterators. \n Ex:
```
x = 12               # loosely typed variable 
int y = 12           # Strictly typed variable in C
cdef int z = 12      # Strictly typed variable in Cython
```
&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;-> The reason for above gain is that since we have not defined the data-type of `x` variable , python has to internally look up for it everytime `x` is used, whereas in case of `y` it simply knows.

##### -> Different types of function definitions : 

|S.No| Type    | Explaination                                                                                                                                               |
|----|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------:|
|1.  | def     | regular python function, calls from Python only.                                                                                                           |
|2.  | cdef    | cython only functions, can't access these from python-only code, must access within Cython, since there will be no C translation to Python for these.      |
|3.  | cpdef   | C and Python. Will create a C function and a wrapper for Python. Why not *always* use cpdef? In some cases, you might have C only pointer, like a C array. |

---
> **Note:** Use 'cpdef' when you are calling this function from python code, and use 'cdef'  when you are calling this function from 'Cython' code only. Incase of doubt use 'cpdef' just to be on safe-side.
---

##### -> File Structure : 
|S.No| File Extenstion  | Explaination                                                              |
|----|:-----------------|:-------------------------------------------------------------------------:|
|1.  | \*.py            | Simple Python Code                                                        |
|2.  | \*.pyx           | The Cython Code                                                           |
|3.  | setup.py         | Script to compile the cython code                                         |
|4.  | \*.pxd           | The file containing definitions, similar to `.h` files in C.              |
|5.  | \*.so            | The compiled `shared object` i.e `.so` file generated after compilation.  |

##### -> Compiling the `.pyx` file :
```
# The file setup.py contains the name of the relevant '.pyx' file along with some compilation flags.
user@localhost:~/$ python setup.py build_ext --inplace
# Generates the corresponding '.so' file i.e the shared-object file.
```
##### -> Generating the `.html` file describing `python interactions` of the `.pyx` i.e cython code.
```
# Name of the cython module be : prime_number.pyx
user@localhost:~/$ cython -a prime_number.pyx
# It will generate prime_number.html , document containing info regarding what all lines are using python vs C.
```

##### -> Note : You can also use 'pyximport' module , but it is more clumsy and lacks clarity in docs. So for this guide (as well as usage), we will be sticking with 'setup.py' method only. 

##### -> Can also use C++ with Cython by using the corresponding compiler-directive `# distutils: language=c++` , which tells the cython compiler code to C++.
##### -> Refer to Examples directory for code examples and their respective explainations.

### [\*] How does Cython optimises ?
##### -> The cython compiler optimises based on the type definitions i.e
##### &nbsp; &nbsp; -> If no type is specified for a variable, parameter/argument or return type then it defaults to a Python object.
&nbsp; &nbsp; &nbsp; &nbsp; -> In this case the standard Python for-loop is used in Cython:
```
for i in range(n):
...
```
##### -> If `i` is declared as an integer (cdef int i), then `Cython` will optimize this into a standard *`C based for-loop`*.

##### -> Performance gain is directly proportional to C-level functions/types , the more the functions,variables, data structures used are C-type the more is the performance gain.
```
python_list  = []             # python list data structure
cdef list cython_list = []    # cython - statically defined list
cdef int c_array[10]          # An array in C type  

The Performance for the above data structures will be as :

(Slowest)                       (Fastest)
python_list < cython_list < c_array
```
##### -> Also know that in finally compiling the '.pyx'--to-->'.c'--and then to-->'.so' we can actually add compiler flags to add/modify/remove type-checking , 'gcc'  optimization flags etc.
##### -> Cython has a feature to disable GIL (Global Interpreter Lock) with directive `with nogil` , though it would make the multi-threaded programs run faster, but might add  more things to manage.
##### -> Whatever modules uses 'cdef/cpdef' would have to be compiled.

### [\*] Requirements
##### -> Cython : `pip install cython`.
##### -> C/C++ Compiler.


</br>

### [\*] Resources
->  <a href="https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html#the-basics-of-cython">Cython Documentation </a>

->  <a href="https://wstein.org/wiki/attachments/2008(2f)sageseminar(2f)kantor/slides.pdf">How does Cython Works : More insights into how cython itself works.</a>
