### Tips for writing  faster python ( CPython) :

---
> Note : Always profile and benchmark your code first.
---


0. Always prefer use **builtin functions**, because most of the time they are way too faster as being implemented in C. (for cpython)

1. Use **sets instead of lists**, as it provides much faster lookups. 

2. Code snippet :

```python
for i in range(100):
    doSomethingWithX()    # Much slower

map(doSomethingWithX() ,  xrange(0,100))        # Much Faster , because interpreter only have to resolve the function name once.
```

3. **try'ing** is cheap, **if'ing** is expensive , when the chances of getting into the `exception` are less (execution inside `except` block is slower).

```python
# Slower
if (type(a) == str):
  a = int(a)

# Faster : python eafp https:#stackoverflow.com/questions/11360858/what-is-the-eafp-principle-in-python
try: 
  a  = int(a)
except:
  pass
```

4. For generating a long string ( 'str\_generated' ) in python  :  

```python
# Slower
str_generated = ""
for x in list:
    str_generated += some_function(x)

# Faster
slist = [some_function(x) for x in somelist]
str_generated = "".join( slist )

Reason :  python strings are immutable so everytime you do '+=' it everytime creates new string.
```

5. Use **generators over iterators**.(It is memory efficient, but doesn't effect the speed of execution)

6. Global import statements are faster than local import statements ( import written inside a function), this is the behaviour of python interpreter.

7. **Function call overhead in Python is relatively high**, (especially compared with the execution speed of a builtin function), This strongly suggests that wherever appropriate, functions should handle data aggregates.

8.  How to find double of a number (say 'num') ? 

```python
a. num = num + num
b. num = num*2
c. num = num<<2

Expected performance : a (worst) < b < c (Best, as it's a bit shift)
Observed performance : a (Best)
The reason we expect 'c' to be best is because the compiler(in C++,java etc) converts it into 1 machine instruction, whereas python doesn't have that concept.
```

9.  For infinite loop `while 1` is better than `while True` the reason being that `while 1` is converted into a **single jump operation** , this is in `python2` only , for `python3` it's the same. The reason for this being in `python2` `True` is not listed as a keyword, so everytime the interpreter has to fetch it's value and the evaluate whereas in `python3` `True` is listed as a keyword and thus it doesn't have to fetch everytime.

10. List comprehensions are better than `for` loop
 
11. Avoid global variables as much as possible (not a good pratice too) , python lookup in global space is too time consuming as compared to local variables.

12. **Avoid unwanted loops** (shouldn't be saying this though)

```python
For finding common element in 2 lists 'a' and 'b' : 
for x in a:
    for y in b:
        if x == y:
            c.append(x)
return c

return set(a) & set(b) # Obv this is faster
```

13. Keep your python code **small and tight**, don't forget python is **interpreted** after-all.

14. Use numpy incase of arrays mathematical computation etc. after all it's in cython and thus much faster. For more speed port to cython.


#### Resources/References :
* https://wiki.python.org/moin/PythonSpeed/PerformanceTips
* https://www.techbeamers.com/python-code-optimization-tips-tricks/
* https://www.monitis.com/blog/7-ways-to-improve-your-python-performance/
