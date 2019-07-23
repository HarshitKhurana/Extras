## Calling C/C++ Functions from Cython

##### -> This directory contains `c_functions.pyx`, a cython file which internally calls C functions.
##### -> Compile `c_functions.pyx` as :
```
user@localhost:/application# python setup.py build_ext --inplace
```

##### -> The usage of `c_functions Shared Object` is implemented in `c_functionsUsage.py`.
##### -> This also contains an example for  `Memory Management` via 'malloc/free' functions of C standard library i.e `libc.stdlib`.
##### -> Run directly i.e `python c_functionsUsage.py` or in python interpreter as : 
```
user@localhost:/application# python

Python 3.7.3 (default, Mar 27 2019, 23:40:30) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import c_functions
>>> c_functions.allocMemoryAndPrint()
Elements in the C-type int pointer are : 11 and 12
>>> c_functions.csin(10)
-0.5440211108893698
>>> c_functions.square_sin(10)
-0.5063656411097588
>>> 

```
OR
```
user@localhost:/application# python c_functionsUsage.py 
Sin function on 10 is :  -0.5440211108893698
Square_Sin function on 10 is :  -0.5063656411097588
Elements in the C-type int pointer are : 11 and 12
The Dictionary(whose type is statically defined) is : 
(1, ' : ', '1')
(2, ' : ', '2')
(3, ' : ', '3')
(4, ' : ', '4')
(5, ' : ', '5')
(6, ' : ', '6')
(7, ' : ', '7')
(8, ' : ', '8')
(9, ' : ', '9')
(0, ' : ', '0')
Hello, I am a C string
user@localhost:/application# rm -rf build/

```
---
> **NOTE:** While converting variables from `python Objects` to C-types , keep in mind that you make sure that the variable doesn't go `Out of Bounds`, i.e a python object if converted to C-Type variable then it must not exceed the limit of C-type variable (4byte, 2 byte whatever based on data type and underlying system).</br>
```
def Anotherfunction(x=9999999999):
  cdef unsigned int c_type_variable = x    # DONT DO, WILL THROW ERROR ON MOST SYSTEMS(32-bit)
  # THE ERORR WILL BE BECAUSE OF BOUNDS, i.e on a 32 bit system the max value of unsigned integer can be 2**32-1, and the value '9999999' is way beyond that.

```
---
> **NOTE:** Rather use 'size\_t' data-type which automatically  tries to fit the size of variable based on system.
---

###### ->  The file `cpp_functions.pyx` contains a few examples in C++ (contains comments adn are self-explanatory), it must contains `# distutils: language=c++` directive.

### RESOURCES :

* <a href="https://www.youtube.com/watch?v=4xpeJYWvbuU"> Cython To speed up Python</a>


