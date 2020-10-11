
### [\*] Decorators & Closures

#### [\*] **Decorators**: 
* A decorator is a callable that takes another function as argument (the decorated func‐tion).
*  The decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object. 
* Eg: 

```python
>>> def f1(func):
...     def wrapper():
...             print ("Startef")
...             func()
...             print ("Ended")
...     return wrapper
... 
>>> def f():
...     print ("Hello")
... 
>>> f()
Hello
>>> f = f1(f)
>>> f()
Startef
Hello
Ended

# The above is same as
>>> def f1(func):
...     def wrapper(*args, **kwargs):
...             print ("Startef")
...             func(*args, **kwargs)
...             print ("Ended")
...     return wrapper
... 
>>> @f1     # Decorator
... def f():
...     print ("Hello")
>>> f()
Startef
Hello
Ended
```
* The end result is the same: at the end of either of these snippets, the target name does not necessarily refer to the original target function, but to whatever function is re‐turned by decorate(target) .

---
> IMP: While using decorator function always use \***args** and \*\***kwargs **, because the developer of decorator function doesn't know the argument or number/type of 
 argument passed to the original function.

---

  * Decorator functions are executed at import/compile-time i.e when the module is loaded.
  * If multiple decroators are applied then the order of execution while be from bottom to top.
```python
>>> def d1(func):
...     def inner():
...         print ("D1")
...         func()
...     return inner
... 
>>> def d2(func):
...     def inner():
...         print ("D2")
...         func()
...     return inner
... 
>>> def f1():
...         print ("F1")
... 
>>> f1 = d1(d2(f1))
>>> f1()
D1
D2
F1
>>> 
>>> 
>>> @d1
... @d2
... def f2():
...         print("F2")
... 
>>> f2()
D1
D2
F2
```



#### [\*] **Closures**
* It is a technique in which the data gets attached to the function.

```python
>>> def outer():
...     outer_variable = "I am outer variable"
...     def _inner_function():
...             print ("Inside inner function")
...             print (outer_variable)
...     print ("inner id: " , id(_inner_function))
...     return _inner_function
... 
>>> func = outer()
inner id:  140195599572776
>>> id(func)
140195599572776
>>> func.__name__
'_inner_function'
>>> func()
Inside inner function
I am outer variable
>>> func()
Inside inner function
I am outer variable
>>> func.__code__.co_freevars
('outer_variable',)     # outer_variable is called a *Free Variable* i.e a variable which is not bounded in the local scope.

```
* In the above example, the *outer_variable* which is part of the outer function gets attached to the `_inner_function` and when we call the `func()` which holds the reference to the `inner\_function` it is still able to access the *outer_variable*, this is called closure as this *outer_variable* is now attached with the `inner_function itself.`

* Pitfall : What if we want to assign to the **free variable** (mentioned above)?
```python
>>> def out():
...     a = "abcd"
...     def inner():    
...             a += "xyz"
...             print (a)
...     return inner
... 
>>> x = out()
>>> x
<function out.<locals>.inner at 0x7f81d4e940d0>
>>> x()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in inner
UnboundLocalError: local variable 'a' referenced before assignment
```
  * The issue here is that `a += "xyz"` simply means `a = a + "xyz"` , so basically we are assigning here which makes it a local variable and thus the error.
  * FIX: Use `nonlocal`
```python
>>> def out():  
...     a = "abcd"
...     def inner():
...             nonlocal a
...             a += "xyz"
...             print (a)
...     return inner
... 
>>> x = out()
>>> x()
abcdxyz
```

