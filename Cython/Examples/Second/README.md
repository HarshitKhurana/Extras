## [\*] Example & data-types

##### -> This documents in this folder focuses more on the data-types which can be used in Cython.
##### -> This folder contains a Cython example of the Python code. ( <a href="https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html#the-basics-of-cython">Taken from Documentation </a>), along with it's explaination.
&nbsp; &nbsp; -> Cython code for finding prime numbers upto a number `nb_primes`, and returning a python list.

-> Available as  prime\_code.pyx
```
  1. def primes(int nb_primes):                                                                                                                              
  2.     cdef int n, i, len_p
  3.     cdef int p[1000]
  4.     if nb_primes > 1000:
  5.         nb_primes = 1000
  6.
  7.     len_p = 0  # The current number of elements in p.
  8.     n = 2
  9.     while len_p < nb_primes:
 10.         # Is n prime?
 11.         for i in p[:len_p]:
 12.             if n % i == 0:
 13.                 break
 14.
 15.         # If no break occurred in the loop, we have a prime.
 16.         else:
 17.             p[len_p] = n
 18.             len_p += 1
 19.         n += 1
 20.
 21.     # Let's return the result in a python list:
 22.     result_as_list  = [prime for prime in p[:len_p]]
 23.     return result_as_list
```
---
> **NOTE:**  Since we are declaring the variable as C-types , we need to keep in mind that all of these variables will be created on the stack, and since we have a limitation on the size of variables we can create on stack thus **WE CANNOT CREATE LARGE ARRAYS** in this manner.</br>
> **Alternate : Use numpy arrays or Typed MemoryViews.**
---

### -> Code Explaination :

| LineNumber  | Purpose                                                                      |
|-------------|:------------------------:                                                    |
| 0.          | This is a python function defined using `def` statement which returns a `python object`.|
| 1.          | The function definition tells that it is a *`normal python function`*.|
| 1.          | The argument `nb_primes` is declared of type `int`, which means that it should/will be converted to `C-Type integer`(by cython compiler), else a **TypeError** will be raised if I can't  be. |
| 2.          | The `cdef` statement is used to define `C-Type` variables.|
| 3.          | The `cdef` statement is used to define an `array in C-type`, In `C` , we need to know the size of array before-hand and thus the size of array p is `1000`.  |
| 4-5         | Done to easily fit into Stack size and not throw a SegFault|
| 7-8         | Initialising the value of C-type variables. |
| 9.          | Looping over to find prime numbers. |
| 11-12       | Iterating over the `C-Type` array and dividing it's content with `i`, since no `python object/variable` is referred t here, the entire loop will be converted to `C-Code` and thus run faster. (Slicing of C-Array is done in order to not loop over 1000 elements.)|
| 16-19       | If the number `i` is divisible by no element which is present in the `C-Type array : p` then the number is prime thus add it to the `C-Type Array` and increment it's size |
| 21.         | Creating a `Python List` of the prime numbers from `C-Type Array` |
| 22.         | Returning the `python list`, Since we have not sprecified any `type` with `result_as_listresult_as_list` variable it defaults to `python-Type object`. |


### Automatic Type Conversions :

|	C types			                                     | From Python types	   | To Python types	          |
|--------------------------------------------------|:--------------------:|----------------------------:|
|[unsigned] char, [unsigned] short, int, long      |  int, long           |  int                        |
|unsigned int, unsigned long, [unsigned] long long |  int, long           |  long                       |
| float , double , long double                     |  int, long, float    |  long                       |
| char \*                                          |  str/bytes           | str(python2)|bytes(python3) |
| C array                                          |  iterable            | list                        |
| struct, union                                    |  -                   | dict                        |

---
> **NOTE:** Make sure that you know the length of C Array at compile time, else it will fail(becuase in C we need the length of array before-hand).</br>
---

---
> **NOTE:** Try to ensure that the return type for all functions is a python object only **(much easier to manage)**.</br>
---

#### -> Cython easily supports all python data structures which means we can statically define the data-types of all python objects/variables.
```
# We are only defining the data-type of the python objects/variable so that the python interpreter doesn't have to look it up again and again.

cdef int i = 0                                              # For int, long, float, double , bint. char

# Below are some of the higher-level data-types (python based), that cython supports
# In this case Cython will use typed-C structures.

cdef str s = "Hello I am a string"                          # For str, bytes, unicode, char*
cdef dict data = {}                                         # For set ,dict
cdef list dataList = []                                     # For set ,dict
cdef list dataTuple = ()                                    # For set ,dict 


# Some of the low-level data-types (C/C++ based), these will squeeze out more performace gain (comparitiviely complex to manage)

cdef int data[5] , *ptr                                     # Array , raw pointers
cdef Color color                                            # enum, struct, union
cdef vector[int] data                                       # C++ STL (vector , map etc)
cdef int[:,:,:] data                                        # memory views, numpy arrays etc.
```


