#!README.md

-> This is CPython specific and may be irrelevant for other implementations of python.
->  Cpython Garbage Collection source code.(https://github.com/python/cpython/blob/master/Modules/gcmodule.c)

[*] Notes

    ->  Python works on names instead of variables.
    ->  Python memory manager uses a special heap to keep all objects and data structures.
    ->  Python uses reference-count + Generational for garbage collection.
    ->  Since reference-Count are not thread safe, thus python requires/uses GIL i.e Global Interpreter Lock so that 1 thread is run by an interpreter at 1 time therefore there is no true Multi-threading in python.


[*] Ways for garbage collection -> 

    A. Tracing - Mark and sweep (beneficial for cyclical dependencies & runs when a threshold is achieved in number of objects rpesent in memory.) 

        1. Mark all reachable objects , by starting at root node and mark all live references. 

        2. When marking is done , sweep will simply remove the dead objects including cyclic.

    B. Reference-Count - If refeernce count of any object/variable reaches 0 remove it from memory.

    C. Generational - Most objects die young(works on this theory)


[*] Reference-count Garbage Collection

    -> Every time  a variable is used it's refcount is increase by 1 and everytime a variable goes out of scope or 'del' is called on a variable/object it's ref-count is decremented, once the ref-count reaches 0 the variable/object is deleted from the memory.

          ```python
            >>> a = 200
            >>> b = 200
            >>> c = 201
            >>> id(a) == id(b)
                True
            >>> id(c) == id(b+1)
                True
          ```   
                   
    -> This is beacause python only creates a single object in the memory with value 200 of type integer and whenver a variable is asigned that value it simply add references to that object in the memory.

    -> Now as soon as one of the variable value is modified, then it checks if any object is already present in the memory of that same type and having the same value as modified variable, if yes then it decrease the ref-count of the previous object to which the modified variable was earlier pointing to and increases the ref-count to the object to which the modified object is now pointing at.

    -> In case of cyclic references like doubly Link list , Graphs etc if we rely on reference count we would never be able to delete the object from memory and would always be occupying space in memory therefore  for these python uses Generational mechanism.
    
    -> 'del x' , only decrements the reference count of x and not actually deletes it , the variable is only deleted when it's ref-Count reaches 0.

    -> Reference count = 0 means immediate clean up.

    -> It is not thread safe.


[*] Generational Garbage Collection
        
   ## These lists are internal to python runtime only (obv.)
     ### Generation0 = [] -- Short Lived : All newly created objects are placed here. 
     ### Generation1 = [] -- Medium Lived  
     ### Generation2 = [] -- Long Lived

    -> It is a periodic process and incase we have a cycle to clean up we would need to wait for GC i.e it can slow down program.

    -> In this python keeps 3 lists for storing every object based on it's generation & at a given time an object can only be a part of 1 generation.

    -> It only stores container objects(list, dictionary, tuples etc) with reference-count > 0(i.e only alive objects) in these lists.

    -> A Generational GC algo whenver runs on a generation it runs on the generation equal to or less than that generation i.e if GC algo runs on generation2 it implicitly means it will run on generation1 & generation0 as well.

    -> Once a threshold on count of number of objects is reached on that generation then a Generational Garbage Collection algo is run on generations equal to or less than that generation , this threshold value can vary across generations.
        
            ```python
              >>> import gc
              >>> gc.get_threshold()
            ```
    
    -> Generation GC cycle algo -

        * ObjectsToDiscard = []

        * Refernce Cycle detection algo(https://github.com/python/cpython/blob/7d6ddb96b34b94c1cbdf95baa94492c48426404e/Modules/gcmodule.c#L902)
                
        * ObjectsToDiscard.append(Objects having no external reference)

        * Once cycle is completed just free the objects on discard list.

    -> An object in 1 generation is promoted to a higher generation if it survives a garbage collection round, this also means that objects in Generation2 will stay for the program execution.


## Another good thing to remember

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
    
    -> Dictionary is way to heavy than list or tuple.


