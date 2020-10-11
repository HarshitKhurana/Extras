
### [\*] OOPS :

* Support the built-in functions that produce alternative object representations (e.g., repr() , bytes() , etc).
* Provide read-only access to attributes.
* Make an object hashable for use.
* Save memory with the use of __slots__ .

---
SideNote: 
 * ```repr()``` : Return a string representing the object as the developer wants to see it.
 * ```str()```  : Return a string representing the object as the user wants to see it.
---

```python
class Pair(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __getitem__(self, key):
        if key in self.__dict__:
            return self[key]
        else:
            return -1

    @property
    def x(self):
        """ Marking it as read-only attribute"""
        return self._x 

    @property
    def y(self):
        """ Marking it as read-only attribute"""
        return self._y

    def __iter__(self):
        """Returns a generator containing all attributes"""
        return (i for i in (self._x, self._y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self._x, self._y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        """
        For an object to be hashable it must be immutable & 
        __eq__ method must also be present for hash comparison
        """
        return hash(self._x) ^ hash(self._y)
```
* The __iter__ built-in function:
1. Checks whether the object implements __iter__ , and calls that to obtain an iterator.
2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates an iterator that attempts to fetch items in order, starting from index 0 (zero).
3. If that fails, Python raises TypeError , usually saying “C object is not iterable,” where C is the class of the target object.

* **@Classmethod** vs **@staticmethod**: 
    * classmethod changes the way the method is called, so it receives the class itself as the first argument, instead of an instance.
    * Static method is just like a plain function that happens to live in a class body, instead of being defined at the module level.

* **\_\_slots\_\_**:
    * By defaults the object attributes of a class are stored in a dict in python, which has a huge memory impact. Therefore to counter it, the developer can specifically ask the interpreter to use tuple instead of dict by defining **\_\_slots\_\_**.

```python
>>> class Student:
...     __slots__ = ('name', 'cls', 'roll', 'student_id')
...     def __init__(self, name, cls, roll, student_id):
...         self.name = name
...         self.cls = cls
...         self.roll = roll
...         self.student_id = student_id 
...         
... 
>>> s = Student("ABC",5,123,"XyZZy")
>>> s.__slots__
('name', 'cls', 'roll', 'student_id')
>>> s.__dict__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__dict__'
```
* Note: When slots are defined, no other attribute other than what are defined in the slots will be allowed.
* Drawbacks: 
    1. You must remember to redeclare __slots__ in each subclass, because the inherited attribute is ignored by the interpreter.
    2. Instances will only be able to have the attributes listed in __slots__ , unless '__dict__' is included in __slots__ (which will negate the memory savings).
    3. Instances cannot be targets of weak references unless you remember to include '__weakref__' in __slots__ .
