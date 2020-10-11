### [\*] General Notes on python :

---
> Note: 
> 1. Instead of using global variables, create a seperate class and make class members.
> 2. ```my_list = [[]] * 3``` will result in a list with three references to the same inner list,
>     Use: ```my_list = [[] for i in range(3)]```
> 3. Do not put mutable objects in non-mutable structure, Eg: don't put list in tuple
> ```python
>>> t = (1,2,[30,40])
>>> t[2] += [50,60]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
> ```
---



**1.** The inbuilt `hash()` in python, returns the hash value of the arg : 
  * This `hash()` is used in the hashing for `dictionaries` too.

```python
>>> hash(5) == hash (5.0)
True                        # Since 5.0 is actualy 5 only
```


**2.** `staticmethod` vs `classmethod` : 
  * The `@staticmethod` is not inherited in the child-class from the parent class.
  * The `staticmethod` is directly callable i.e it doesn't require the class itself or any instance of class , unlike the `@classmethod` and functions defined in the class resp.

```python

class A:
  def func(self):
    print ("function with self argument")

  @classmethod
  def class_func(cls):
    print ("class function with class argument")

  @staticmethod
  def static_func(cls):
    print ("static function with No argument")
```

**3.** `all()` vs `any()`
  * `all()` returns True , when every element in the iterable is True.
  * `any()` returns True , when any element in the iterable is True.

```python
def all(list_arg):
  for i in list_arg:
    if bool(i) == False:
      return False
  return True

def any(list_arg):
  for i in list_arg:
    if bool(i) == True:
      return True
  return False
```

**4.** *deepCopy* vs *shallowCopy* : 
  * In `deepCopy` every element of the iterable is individually copied.
  * In `shallowCopy` only the reference to the original iterable is copied.

```python
# Shallow Copy
>>> a = [i for i in range(10)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = a
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> id(a)
139632274549896
>>> id(b)
139632274549896

# Same ID's as `b` is just the reference to `a`.


# Deep Copy
>>> a = [i for i in range(10)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b = []
>>> for i in a:
...     b.append(i)
... 
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> id(a)
139632274556744
>>> id(b)
139632274557064

# Different ID's as 2 seperate objects

```

**5. Lambda Functions** : Anonymous functions.
  * To simply put it, `lambda` functions are the functions which don't start with the usual `def ` keyword. 
  * Lambda function syntax: 

  ```python
  >>> KeyWord input_Arguments semi-colon return_Value
  >>> lambda  x,y             :          x+y            # Lambda function to return sum of 2 numbers.
  ```
  * Example : 

  ```python
  >>> lambda x: x+1   # A lambda function which takes input `x` and returns output `x+1`.

  >>> func = lambda (x: x**2)   # Lambda function which returns square
  >>> func(9)
  81

  >>> full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
  >>> full_name('guido', 'van rossum')
  'Full name: Guido Van Rossum'
  ```

**6. Map** function  : This function takes input a function and a list, and then that function is called with all the items in the list and a new list with  output values in returned.

```python
>>> aList = [i for i in range(10)]
>>> outList = list(map( (lambda x:x+x), aList))
>>> aList
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> outList
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```
**7. yield** : It is a keyword which acts like return, except that the function returns a generator.
  * When you call the function, the code you have written in the function body does not run. The function only returns the generator object.


```python
>>> def createGenerator():
...     for i in range(3):
...             yield i*i
...     return
... 
>>> my_gen = createGenerator()
>>> type(my_gen)
<class 'generator'>
>>> next(my_gen)
0
>>> next(my_gen)
1
>>> next(my_gen)
4
>>> next(my_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```

**8. Generators** :  Generators are iterators, a kind of iterable you can **only iterate over once**. Generators do not store all the values in memory, they generate the values on the fly , and once iterated over the values are gone. (Lazy Evaluation)
  * Benefits :
    *  When the value returned by function is to be only used once and not again.
    *  Use less memory as , the actual values are generated only when using the generator, not before.
  * Drawback : 
    * Cannot perform random access via indexes as possible with list.
    * While using `join()` with generators it performs poor aas compared to lists.

```python
>>> myGenerator = (i for i  in range(5))
>>> myGenerator
<generator object <genexpr> at 0x7fe2e1baf3b8>
>>> for i in myGenerator:
...     print (i)
... 
0
1
2
3
4
>>> myGenerator
<generator object <genexpr> at 0x7fe2e1baf3b8>
>>> for i in myGenerator:
...     print (i)
... 
>>> 


# Making a class iterable
class Sentence1(object):
    def __init__(self, line):
        self.line = line
    
    def __next__(self):
        """ This makes the class itself an iterator"""

    def __iter__(self):
        """ Makes this class iterable & instantiates a new iterator every time"""
        for word in self.line.split(' '):
            yield word
        return 
>>> for i in Sentence("Hello! This is a test program"):
...     print (i)
... 
Hello!
This
is
a
test
program


# Making class iterator

 # With Iterator
class Sentence2(object):
    def __init__(self, line):
        self.line = line
        self.index = 0
    
    def __next__(self):
        """ This makes the class itself an iterator"""
        if self.index < len(self.line.split(' ')):
            word = self.line.split(' ')[self.index]
            self.index += 1
            return word     # since returning thus it's an iterator
        raise StopIteration

    def __iter__(self):
        """ Makes this class iterable & instantiates a new iterator every time"""
        return self

s = Sentence2("Hello! This is a test program")
>>> next(s)
'Hello!'
>>> next(s)
'This'
>>> next(s)
'is'
>>> next(s)
'a'
>>> next(s)
'test'
>>> next(s)
'program'
>>> next(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "test.py", line 110, in __next__
    raise StopIteration
StopIteration


 # With generator
class Sentence2(object):
    def __init__(self, line):
        self.line = line
    
    def __next__(self):
        """ This makes the class itself an iterator"""
        for word in self.line.split(' '):
            yield word  # Since yield'ing thus it's a generator

    def __iter__(self):
        """ Makes this class iterable & instantiates a new iterator every time"""
        return self

>>> s = Sentence2("Hello! This is a test program")
>>> iterator = next(s)
>>> next(iterator)
'Hello!'
>>> next(iterator)
'This'
>>> next(iterator)
'is'
>>> next(iterator)
'a'
>>> next(iterator)
'test'
>>> next(iterator)
'program'
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

```
 * It may be tempting to implement __next__ in addition to __iter__ in the Sentence class, making each Sentence instance at the same time an iterable and iterator over itself. But this is a terrible idea
 * Any Python function that contains the yield keyword is a generator function. In the above code snippet, the __iter__() is  generator function.



**9. Default Argument** : The default value for a function argument is only evaluated once, at the time that the function is defined and thus it's only initialised once and on future calls use the same object.
    * Only when default argument is of mutable type.


```python
>>> def foo(a=[]):
...     a.append(1)
...     return a
... 
>>> l = foo()
>>> l
[1]
>>> l = foo()
>>> l       # Expected: [1]
[1, 1]      

# FIX
>>> def foo(a=None):
...     if not a:
...             return [1]
... 
>>> foo()
[1]
>>> foo()
[1]
```


**10. Scoping** : Python scope resolution is based on the LEGB rule, which is shorthand for **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in. 

```python
>>> x = 1
>>> def foo():
...     print (x)
...     if False:
...             x = 1 
... 
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in foo
UnboundLocalError: local variable 'x' referenced before assignment
```
  * The error occurs because when assigning to a variable in a scope, that variable is automatically considered by Python to be local to the scope(and shadows any similarly named variable in any outer scope).
  * Any other assignment operation would throw same error, whereas non-assignment function would work fine.

```python
>>> x = []
>>> def foo():
...     print (x)
...     if False:
...             x.append(1) # Non-assignment operation
... 
>>> foo()
[]
```


**11. Class Variables** : Python follows MRO (Method Resolution Order) for handling access of parent class members.

```python
# Only parent class has attribute 'x' with value 1
>>> class A():
...     x = 1
... 
>>> class B(A):
...     pass
... 
>>> class C(A):
...     pass
... 
>>> print (A.x, B.x, C.x)
1 1 1
>>> A.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None, 'x': 1, '__weakref__': <attribute '__weakref__' of 'A' objects>, 
                '__dict__': <attribute '__dict__' of 'A' objects>})
>>> B.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None})

>>> C.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None})

>>> B.x = 2     # Adds an attribute named 'x' in the object of B
>>> B.__dict__
mappingproxy({'__module__': '__main__', 'x': 2, '__doc__': None})
>>> print (A.x , B.x, C.x)
1 2 1

>>> A.x = 3
>>> A.__dict__
mappingproxy({'__module__': '__main__', '__doc__': None, 'x': 3, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__dict__': <attribute '__dict__' of 'A' objects>})
>>> print (A.x, B.x, C.x)
3 2 3
```

  * The above is as such bcoz python stores the object/class properties inside a dictionary.
  * What is <a href="https://docs.python.org/3.8/library/weakref.html"> \_\_weakref\_\_ </a> ? 

**12. MRO (Method Resolution Order)** : It defines the order in which the functions are searched inside the parent classes in-case of multiple inheritance.
  * For python, it is also applicable on other attributes as well.

```python
# Legacy MRO : DEPRECATED
>>> class A():
...     def hi(self):
...             print ("Hi! from A")
... 
>>> class B(A): pass
... 
>>> class C(A):
...     def hi(self):
...             print ("Hi! from C")
... 
>>> class D(B, C): pass
... 
>>> D().hi()
Hi! from A
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)
# MRO : class D -> class B -> class A -> class C - > class A(not mentioned though) -> Object Class


# New-Style MRO
>>> class A(object):    # Only diff is here
...     def hi(self):
...             print ('Hi! from A')
... 
>>> class B(A): pass
... 
>>> class C(A): 
...     def hi(self):
...             print ('Hi! from C')
... 
>>> class D(B,C): pass
... 
>>> D().hi()
Hi! from C
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# MRO : class D -> class B -> class C - > class A -> Object Class
```
  * In new-style MRO a **class comes into resolution order only once and that too after all of its subclasses are covered**, this is so as to ensure that if their is a sub-class that has over-rided the functionality of the parent class then it's handled in the ordering path.

**12. Named Tuples**: It is a class which provides the ability for the tuples to have names associated with it.
  * Instances of a class that you build with namedtuple take exactly the same amount of memory as tuples because the field names are stored in the class. They use less memory than a regular object because they don’t store attributes in a per-instance `__dict__` .

```python
>>> from collections import namedtuple
>>> City = namedtuple ('City','name country population coordinates')
>>> tokyo = City('Tokyo', 'JP' , '36.933' , (1234,5678))
>>> tokyo
City(name='Tokyo', country='JP', population='36.933', coordinates=(1234, 5678))
>>> tokyo.name
'Tokyo'
>>> tokyo.country
'JP'
>>> tokyo.coordinates
(1234, 5678)
``` 
  * It supports nesting.

**13. Slice Naming** : The ability to name a slice.
  * Helpful in case of string parsing.

```python
>>> a = "JPYINR20JAN100CE"
>>> cur_pair = slice(0,6)
>>> expiry = slice(6,11)
>>> strike = slice(11,-2)
>>> optn_type = slice (-2,None)
>>> a[cur_pair]
'JPYINR'
>>> a[expiry]
'20JAN'
>>> a[strike]
'100'
>>> a[optn_type]
'CE'
>>> 
```

**14. Context Manager** : These help the developer to properly manage resources so as to be able to exactly specifiy what to setup and what to tear down
  * It is helpful when developer want to perform some action for which developer need access to certain resource and once the work is done developer want to free the resource.

```python
>>> class File(object):
...     def __init__(self, file_name, method):
...         self.file_obj = open(file_name, method)
...
...     def __enter__(self):
...         return self.file_obj         # returns file object to caller
...
...     def __exit__(self, excptn_type, excptn_value, excptn_traceback):
...         self.file_obj.close()
... 
>>> with File('demo.txt', 'w') as opened_file:
...     opened_file.write('Hola!')
... 
5
>>> with File('demo.txt', 'r') as opened_file:
...     opened_file.read()
... 
'Hola!'


>>> from contextlib import contextmanager
>>> @contextmanager
... def open_file(name):
...     f = open(name, 'w')
...     try:
...         yield f     # returns file object to caller
...     finally:
...         f.close()
... 
>>> 
>>> with File('demo.txt', 'w') as opened_file:
...     opened_file.write('Hola2')
... 
5
>>> with File('demo.txt', 'r') as opened_file:
...     opened_file.read()
... 
'Hola2'
```
 * In case any exception arises, then it would need to be handle explicitly in the `__exit__()` , if `__exit__()` returns `True` that means everything worked and all exceptions(if arose) were handled successfully.


**15. Coroutines**
 * Coroutines are a special type of function that deliberately yield control over to the caller, but does not end its context in the process, instead maintaining it in an idle state.
 * They benefit from the ability to keep their data throughout their lifetime and, unlike functions, can have several entry points for suspending and resuming execution.

```python
def test():
    while True:
        value = (yield)
        print(value)

try:
    cor = test()
    next(cor)
    cor.close()
    cor.send("So Good")
except StopIteration:
    print("Done with the basics")

Done with the basics    # Since sending value to co-routine after closing
```

**16. Futures**
  * A Future represents an eventual result of an asynchronous operation. Not thread-safe.
  * Future is an awaitable object. Coroutines can await on Future objects until they either have a result or an exception set, or until they are cancelled.

```python
>>> import concurrent.futures
>>> import time
>>> def func():
...     time.sleep
KeyboardInterrupt
>>> def func(x):
...     print ("Sleeping for {}".format(x))
...     time.sleep(x)
...     return "Done"
... 
>>> with concurrent.futures.process
concurrent.futures.process
>>> with concurrent.futures.ProcessPoolExecutor() as executor:
...     future_1 = executor.submit(func, 1)
...     future_2 = executor.submit(func, 1)
...     print ("f1: ".format(future_1.result))
...     print ("f2: ".format(future_2.result))
... 
f1: 
f2: 
Sleeping for 1
Sleeping for 1
```

**17. Asyncio**:
  * It provides the ability to write concurrent code using aync/await syntax.
  * Helpful when waiting on a thread fo I/O.

```python

import time
import asyncio

def is_prime(x):
    return not any(x//i == x/i for i in range(x-1, 1, -1))

async def highest_prime_below(x):
    print('Highest prime below %d' % x)
    for y in range(x-1, 0, -1):
        if is_prime(y):
            print('→ Highest prime below %d is %d' % (x, y))
            return y
        await asyncio.sleep(0.01) # It suspends this function for that specific time and give the control back to the event loop which further uses this time to execute other function
	#time.sleep(0.01)   # this sleeps the thread of execution i.e CPU for that time.
    return None


async def main():
    
    t0 = time.time()
    # await waits for the functions to complete
    await asyncio.wait( [
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
        ] )
    t1 = time.time()
    print('Took %.2f ms' % (1000*(t1-t0)))
    
    
loop = asyncio.get_event_loop() # Creates the event loop
loop.run_until_complete(main()) # Ensures that the loop run untill the main() exists
loop.close()                    # Close the loop once work is done

Highest prime below 1000
Highest prime below 10000
Highest prime below 100000
→ Highest prime below 1000 is 997
→ Highest prime below 100000 is 99991
→ Highest prime below 10000 is 9973
Took 446.42 ms
```


