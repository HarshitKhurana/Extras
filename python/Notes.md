### [\*] General Notes on python :


**1.** The inbuilt `hash()` in python, returns the hash value of the arg : 
  * This `hash()` is used in the hashing for `dictionaries` too.

```bash
>>> hash(5) == hash (5.0)
True                        # Since 5.0 is actualy 5 only
```


**2.** `staticmethod` vs `classmethod` : 
  * The `@staticmethod` is not inherited in the child-class from the parent class.
  * The `staticmethod` is directly callable i.e it doesn't require the class itself or any instance of class , unlike the `@classmethod` and functions defined in the class resp.

```bash

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

```bash
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

```bash
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

**5.** Lambda Functions : Anonymous functions.
  * To simply put it, `lambda` functions are the functions which don't start with the usual `def ` keyword. 
  * Lambda function syntax: 

  ```bash
  >>> KeyWord input_Arguments semi-colon return_Value
  >>> lambda  x,y             :          x+y            # Lambda function to return sum of 2 numbers.
  ```
  * Example : 

  ```bash
  >>> lambda x: x+1   # A lambda function which takes input `x` and returns output `x+1`.

  >>> func = lambda (x: x**2)   # Lambda function which returns square
  >>> func(9)
  81

  >>> full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
  >>> full_name('guido', 'van rossum')
  'Full name: Guido Van Rossum'
  ```

**6.** `Map` function  : This function takes input a function and a list, and then that function is called with all the items in the list and a new list with  output values in returned.

```bash
>>> aList = [i for i in range(10)]
>>> outList = list(map( (lambda x:x+x), aList))
>>> aList
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> outList
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

```

**7.** Generators :  Generators are iterators, a kind of iterable you can **only iterate over once**. Generators do not store all the values in memory, they generate the values on the fly , and once iterated over the values are gone. (Lazy Evaluation)
  * Benefits :
    *  When the value returned by function is to be only used once and not again.
    *  Use less memory as , the actual values are generated only when using the generator, not before.
  * Drawback : 
    * Cannot perform random access via indexes as possible with list.
    * While using `join()` with generators it performs poor aas compared to lists.

```bash
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

**8.** `yield` : It is a keyword which acts like return, except that the function returns a generator.
  * When you call the function, the code you have written in the function body does not run. The function only returns the generator object.


```bash
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

