### [\*] General Notes on python :

---
> Note: Instead of using global variables, create a seperate class and make class members.
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

**7. Generators** :  Generators are iterators, a kind of iterable you can **only iterate over once**. Generators do not store all the values in memory, they generate the values on the fly , and once iterated over the values are gone. (Lazy Evaluation)
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

```

**8. yield** : It is a keyword which acts like return, except that the function returns a generator.
  * When you call the function, the code you have written in the function body does not run. The function only returns the generator object.


```python
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0x7fe4c7b8d9a038>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

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
  * The error occurs because when assigning to a variable in a scope, that variable is automatically considered by Python to be local to that scope and shadows any similarly named variable in any outer scope.
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
# Legacy MRO
>>> class A():
...     def hi(self):
...             print ("Hi! from A")
... 
>>> class B(A): pass
... 
>>> class C():
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
>>> class A(object):
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
# MRO : class D -> class B -> class A -> class C - > class A(not mentioned though) -> Object Class
```
  * In new-style MRO a **class comes into resolution order only once and that too after all of its subclasses are covered**, this is so as to ensure that if their is a sub-class that has over-rided the functionality of the parent class then it's handled in the ordering path.


