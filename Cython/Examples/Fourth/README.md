### [\*] Cython Extension Types


##### -> These are also known as `cdef classes`.
---
> **NOTE:** Python classes can inherit from `cdef classes` but not the other way.</br>
---

##### -> These are generally more memory efficient and faster than generic Python classes, but they do come with some restrictions.
###### &nbsp; &nbsp; -> The reason they are memory efficient and faster is becuase it internally uses C-struct , instead of python dictionary, and thus access fields and methods directly at C-level, instead of python dictionary lookup.

##### -> Benefits of `cdef classes` : 
* Consume less memory, since they use C-struct type (internally).
* Faster attribute lookup , method access etc.
* Can be called/inherited directly from Python. (but only methods available in the python space are the ones with @property defined)
* Can be used as a valid type for static typing i.e (this cdef class now can be itself used as a valid data-type)

##### -> characteristics of `cdef classes` : 

* All attributes must be pre-declared at compile-time (since it uses C-struct internally and not python dictionary)
* Attributes are by default only accessible from Cython (typed access).
* Properties can be declared to expose dynamic attributes to Python-space.  (using @property)

##### -> Similar to the concept of `header files` (.h) in C/C++, cython also has similar structure for segregating the definition and decleration of classes/functions.
###### &nbsp; &nbsp; &nbsp; -> Example :
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -> Decleration in `student_extensionType_segregated.pxd` and definition in `student_extensionType_segregated.pyx`.
</br>
OR
</br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -> Both clubbed together in `student_extensionType.pyx` .

##### -> In the above mentioned code examples , we have use '@property' in order to use the value of attribute outside Cython i.e in the python code, but there are more scoping available i.e increasing/limiting the scope, refer to  'scope\_modification.pyx'.

### [\*] Resources

* <a href="https://cython.readthedocs.io/en/latest/src/userguide/extension_types.html"> Cython Extension Types</a>

