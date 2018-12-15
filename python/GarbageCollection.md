<h2><center>GarbageCollection.md</center></h2>

-> This is CPython specific and may be irrelevant for other implementations of python.
<br>
->  <a href="https://github.com/python/cpython/blob/master/Modules/gcmodule.c"> Cpython Garbage Collection source code.</a>


<h2>Points to Remember</h2>

  ->  Python works on names instead of variables.<br>
  ->  Python memory manager uses a special heap to keep all objects and data structures.<br>
  ->  Python uses reference-count + Generational for garbage collection.<br>
  ->  Since reference-Count are not thread safe, thus python requires/uses <b>GIL</b> i.e <b>Global Interpreter Lock</b> so that 1 thread is run by an interpreter at 1 time therefore there is no true Multi-threading in python.<br>


<h2>Mechanisms for garbage collection</h2>

A. <b>Tracing</b> - Mark and sweep (beneficial for cyclical dependencies & runs when a threshold is achieved in number of objects present in the memory) <br>
1. Mark all reachable objects , by starting at root node and marking all live references. 
<br>
2. When marking is done , sweep will simply remove the dead objects including cyclic references.

B. <b>Reference-Count</b> - If reference count of any object/variable reaches 0 remove it from memory.

C. <b>Generational</b> - Most objects die young(works on this theory)
<hr>

-> The way python does Garbage Collection is as : <br><br>
<b>	1. Reference Count<br></b>
<b>	2. Generational Garbage Collection </b>

<h3>1. Reference-count Garbage Collection</h3><hr>

-> Every time  a variable is used it's <b><i>ref-count is increased by 1</i></b> and every-time a <b><i>variable goes out of scope or 'del' is called on a variable/object it's ref-count is decremented</i></b>, once the ref-count reaches 0 the variable/object is deleted from the memory.

```python
>>> a = 200
>>> b = 200
>>> c = 201
>>> id(a) == id(b)
True
>>> id(c) == id(b+1)
True
```   

-> The above code evaluates to <b>'True'</b>  because python only creates a single object in the memory with value 200 of type integer and whenever a variable is assigned that value it simply add references to that object in the memory.

-> Now as soon as one of the variable value is modified, then it checks if any object is already present in the memory of that same type and having the same value as modified variable, if yes then it decrease the ref-count of the previous object to which the modified variable was earlier pointing to and increases the ref-count to the object to which the modified object is now pointing at.

-> In case of cyclic references like doubly Link list , Graphs etc if we rely on reference count we would never be able to delete the object from memory and that object would always be occupying space in memory therefore for these python uses Generational GC mechanism.

-> `del x` , only decrements the reference count of x and not actually deletes it , the variable is only deleted when it's ref-Count reaches 0.

-> Reference count = 0 means immediate clean up.

-> It is not thread safe.


<h3>2. Generational Garbage Collection</h3><hr>

-> In this python keeps 3 lists for storing every object based on it's generation & at a given time an object can only be a part of 1 generation only.
<h6> &nbsp&nbsp&nbsp&nbsp&nbsp Generation0 = [ ] -- Short Lived : All newly created objects are placed here. <br>
 &nbsp&nbsp&nbsp&nbsp&nbsp Generation1 = [ ] -- Medium Lived<br>
 &nbsp&nbsp&nbsp&nbsp&nbsp Generation2 = [ ] -- Long Lived<br>
</h6 
<u><h5> These lists are internal to python runtime only (obv.)</h5></u>

-> Generational GC is a periodic process and incase we have a cycle to clean up then would need to wait for GC and thus  it can slow down program.

-> It only stores container objects(list, dictionary, tuples etc) with `reference-count > 0` (i.e only alive objects) in these lists.

-> A Generational GC algo whenever runs on a generation it runs on the generation equal to or less than that generation i.e if GC algo runs on generation2 it implicitly means it will run on generation0 & generation1 as well.

-> Once a threshold on count of number of objects is reached on that generation then a Generational Garbage Collection algo is run on generations equal to or less than that generation , this threshold value can vary across generations.

```python
>>> import gc
>>> gc.get_threshold()
  (70,10,10) # This can vary
```

-> Generation GC cycle algorithm -

    * ObjectsToDiscard = []

    * Object reference Cycle detection algo(https://github.com/python/cpython/blob/7d6ddb96b34b94c1cbdf95baa94492c48426404e/Modules/gcmodule.c#L902)

    * ObjectsToDiscard.append(Objects having no external references)

    * Once cycle is completed just free the objects present in discard list.

-> An object in 1 generation is promoted to a higher generation if it survives a garbage collection round, this also means that objects in Generation2 will stay for the program execution.


<h2>Another good thing to remember</h2>

-> Size of data structures : {}.__sizeof__() > [].__sizeof__() > ().__sizeof__().

```python
>>> print ("Size of dictionary : " , {}.__sizeof__() ) 
Size of dictionary : 264

>>> print ("Size of List : " , [].__sizeof__() ) 
Size of List : 40

>>> print ("Size of Tuple : " , ().__sizeof__() ) 
Size of Tuple : 24

>>> {}.__sizeof__() > [].__sizeof__() > ().__sizeof__()
True
```

-> Dictionary is way too heavy than list or tuple.<br><br>


