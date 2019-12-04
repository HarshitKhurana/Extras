### [\*] Smart Pointers

* Smart Pointers are simply there to manage memory automatically and not let the developer worry about allocating and de-allocating memory and focus on the business logic, to simply put it the handle automatic deletion of pointer.
* Smart Pointers is a wrapper class over ****raw pointers*** with operators `*` and `->` overloaded.
* `#include <memory>` for using smart pointers.

#### Types: 
***1. Unique Pointer***

* As the name suggests , these pointers are unique and ***cannot be copied***.
* Which also means at any given time there will only be 1 owner of the underlying raw pointer.

```bash
unique_ptr<int> ptr1 (new int);   # Creating a unique pointer of int.

unique_ptr<int> ptr2 = ptr1;      # Error : can't copy uniqure_ptr
```

* What if you want to change the ownership of that pointer ?
  * unique\_ptr can be moved using the move semantic i.e `std::move()`, function to transfer the ownership of the contained pointer to another unique\_ptr.

```bash
unique_ptr<int> ptr1 (new int);   # Creating a unique pointer of int.

unique_ptr<int> ptr2 =  std::move(ptr1);      
```

```bash
// Example of unique_ptr
#include<memory>
#include<iostream>

int main()
{
  std::unique_ptr<int> a(new int(5));                 // Not safe , if the constructor throws an exception
  std::unique_ptr<int> a = std::make_unique<int>();   // This handles the exceptions and won't result in returning a dangling pointer-memory leak.
}
```
* The reason we can only 1 owner of unique\_ptr is becuase , internally it creates an object on heap and as soon as the object of unique\_ptr goes out of scope it's destructor gets deleted and thus the memory gets de-allocated, if it has more than 1 owners/references to the same object then even when 1 object's destructor has been called the other owner/reference will still be pointing to that same memory address and thus dangling pointer.


***2. Shared Pointer***
* With unique pointers we can only have one owner of the pointer, so when you want to share it then use **shared\_ptr**.
* Mostly **shared\_ptr** are maintained using reference counting.
  * Basically in reference counting , the **shared\_ptr** object/class maintains the total number of references you have to that object.
  * When the total reference count gets deleted then only the actual object is deleted.
  * Ex : There are 2 references to the same pointer , then one the first one goes out of scope the reference count is decremented and one then next one goes out of scope then ref count is again decremented, and now that it reaches 0 , the memory is actually de-allocated.

```bash
// Shared_ptr example

#include<iostream>
#include<memory>

int main()
{
  //std::shared_ptr<int> s (new int());   // Don't do this because it has to maintain ref count in the control block. # read below
  
  std::share_ptr<int> copy_ptr;
  std::shared_ptr<int> s  = std::make_shared<int>();

  copy_ptr = s;   // This increments the reference count.
```

* The reason why we should not use `new` with the `std::shared\_ptr` is because , when called it creates a `new` control block for reference counting, and thus when you explicitly use `new` and creates object using that by passing the reference to newly created object then it has to create another object for maintaining the reference counting, whereas if you use `std::make_shared<int>()` it constructs them together and thus is more faster.


***3. Weak Pointer***
* In shared pointers the refernce count is used to maintain the life of the pointer.
* Weak pointers are used with shared pointers only.
  * When a weak pointer is assigned a shared\_ptr value then although it does copy it but it *doesn't increments it's reference count*.

```bash
// Weak_ptr

#include<memory>
#include<iostream>

int main()
{
  std::weak_ptr<int> wk_ptr;
  std::shared_ptr<int> shrd_ptr = std::make_shared<int>();
  wk_ptr = shrd_ptr;      // This copies the shared pointer but doesn't increments the reference count.
}
```
* We require *weak\_ptr* specially when there is a cyclic dependency in the shared\_ptr i.e class A has a shared\_ptr to class B and vice-versa, in this the reference count would never reach 0, thus we can use weak\_ptr to solve it.


***4. Auto Pointer***
* They were pre-decessor of unique\_ptr.
* They are deprecated.
  * It was very much like a scoped pointer, except that it also had the "special" dangerous ability to be copied — which also unexpectedly transfers ownership.
* It was deprecated in C++11 and removed in C++17, so you shouldn't use it.

```bash
std::auto_ptr<MyObject> p1 (new MyObject());
std::auto_ptr<MyObject> p2 = p1; // Copy and transfer ownership. 
                                 // p1 gets set to empty!
p2->DoSomething(); // Works.
p1->DoSomething(); // Oh oh. Hopefully raises some NULL pointer exception.
```
