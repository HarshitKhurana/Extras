
1. Python API convention: functions or methods that change an object in place should return None to make it clear to the caller that the object itself was changed
2. Default Arguments should have a non-mutable default value.
3. Module references: 
  * `bisect` : Binary Search. Inserting in sorted array
  * `pickle` : Serialising/de-serialising data for disk storage.
4. Mutable = not hashable.
5. Use **\_\_setitem\_\_** and **\_\_getitem\_\_** in order to provide **object[key]** functionality.
6. Access object attributes:
```python
>>> dir (int)
```
7. `functools.lru_cache(maxsize=128, typed=False)` for memoizing the code, much beneficial when fetching info from web or when storing previous results would be helpful.
    * maxsize = Max number of call results stored.
    * typed = stores output of diff. argument types seperately, Eg: 1(int) and 1.0(float)
    * Note: It stores everything in a dictionary, with key= \*args/\*\*kwargs made in the function call.
8. `__del__` is only for interpreter and not developer, as the interpreter calls it and end for cleanup, if you need to do something at clearn up sue `atexit`  module.
