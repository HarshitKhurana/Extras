
## Cython - First Code BENCHMARKING

-> Running same code in python and cython for sum of `n` numbers and returning it.

|S.No| FileName        | Purpose                                                                      |
|----|:------------    |:------------------------:                                                    |
|1.  | sumToN.py       | Code in python                                                               |
|2.  | sumToN\_C1.pyx  | Changes for Cython , nothing changed same code as python                     |
|2.  | sumToN\_C2.pyx  | Changes for Cython , with some little modifications                          |
|2.  | sumToN\_C3.pyx  | Changes for Cython , with major possible modifications for optimisations     |
|3.  | setup1.py       | To compile cython code , nothing changed same code as python                 |
|4.  | setup2.py       | To compile cython code , with some little modifications                      |
|5.  | setup3.py       | To compile cython code , with major possible modifications for optimisations |


#### Test 1 : No Modification in Code ( .py and .pyx are same )

-> Compile as : 
```
user@localhost:~/$ python setup1.py build_ext --inplace
# This will generate `sumToN_C1.c` , `sumToN_C1.cpython-37m-x86_64-linux-gnu.so` which is basically the C code and it's corresponding compiled shared Object.
# The `.so` file i.e shared object can be directly imported in the interpreter or in the python code as a module.
```

-> In Order to execute the code , do as : 
```
Python 3.7.3 (default, Mar 27 2019, 23:40:30) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sumToN_C1             # This imports the `.so` file and not the `.pyx` file
>>> sumToN_C1.mainFunc(10)       # Calling the function responsible to do task from '.so' file 
45
>>> import sumToN               # This imports the `.py` file  
>>> sumToN.mainFunc(10)         # Calling the function responsible to do task 
45
>>> 

```

-> Analysing how much time the code takes in python vs in cython , **With No Modifications in Code**
```
# With python
user@localhost:/app# python -m timeit -s 'from  sumToN import mainFunc' 'mainFunc(10000000)'
1 loop, best of 5: 828 msec per loop

# With cython
user@localhost:/app# python -m timeit -s 'from  sumToN\_C1 import mainFunc' 'mainFunc(10000000)'
1 loop, best of 5: 321 msec per loop
user@localhost:/app# 

```
**The Gain is around 2.5 times(321/828) and that too without any change**


#### Test 2 : Little Modification in Code ( .pyx is modified a bit )

-> Compile as : 
```
user@localhost:~/$ python setup2.py build\_ext --inplace
# This will generate `sumToN_C2.c` , `sumToN_C2.cpython-37m-x86_64-linux-gnu.so` which is basically the C code and it's corresponding compiled shared Object.
# The `.so` file i.e shared object can be directly imported in the interpreter or in the python code as a module.
```

-> Analysing how much time the code takes in python vs in cython , **With Little Modifications in Code**
```
# With python
user@localhost:/app# python -m timeit -s 'from  sumToN import mainFunc' 'mainFunc(10000000)'
1 loop, best of 5: 828 msec per loop

# With cython
user@localhost:/app# python -m timeit -s 'from  sumToN\_C2 import mainFunc' 'mainFunc(10000000)'
1 loop, best of 5: 319 msec per loop

```
**The Gain is same as the previous i.e around 2.5 times(319/828)**


#### Test 3 : Major Modification in Code ( .pyx is modified )

-> Compile as : 
```
user@localhost:~/$ python setup3.py build\_ext --inplace
# This will generate `sumToN_C3.c` , `sumToN_C3.cpython-37m-x86_64-linux-gnu.so` which is basically the C code and it's corresponding compiled shared Object.
# The `.so` file i.e shared object can be directly imported in the interpreter or in the python code as a module.
```

-> Analysing how much time the code takes in python vs in cython , **With Major Modifications in Code**
```
# With python
user@localhost:/app# python -m timeit -s 'from  sumToN import mainFunc' 'mainFunc(10000000)'
1 loop, best of 5: 795 msec per loop

# With cython
user@localhost:/app# python -m timeit -s 'from  sumToN\_C3 import mainFunc' 'mainFunc(10000000)'
500 loops, best of 5: 672 usec per loop

```

## HOLY SHIT

## The Gain is around 1232 times(828 milliSecond/672 microSecond)


