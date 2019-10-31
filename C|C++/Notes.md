### [\*] Notes

* Some topics in C++.

* Stack is faster than heap, because no pointer de-referencing which takes time and cache-pipelining.

**1. Mutex :** `std::mutex` provides mutex functionality.

  * Never use lock and unlock() directly.
  * Don't do this.
```c++
#include<mutex>
std::mutex m;
void func(string s)
{
   m.lock();
   cout <<"string is : " << s<<endl;    // What if this line throws error ? will the mutex ever be unlocked ? NO
   m.unlock();
}
``` 

  * Do this
```c++
#include<mutex>
std::mutex m;
void func(string s)
{
   std::lock_guard<std::mutex> guard(m);    // RAII - if this goes out of scope, then mutex is automatically unlocked.
   cout <<"string is : " << s<<endl;    
   m.unlock();
}
``` 


**2. Thread :** It is a smallest sequence of programmed instruction which can be independently managed by the scheduler.

```c++
#include<thread>

void printer(int a)
{
  while (a--)
    cout <<"a is : " << a<<endl;
}
int main()
{
  std::thread t1( printer, 1);   // Passes function pointer internally.
  t1.join();      // If you want to end main only after the printer() finishes.
  t1.detach();    // If you want to end main  irresepctive of whether or not the printer() finishes.
                  // when you don't write either , it will throw an erorr if the main finishes before the printer().
}
 $ g++ -std=c++11 a.cpp -pthread
```


**3. Casting :** It's the type casting i.e simply changing data types.  
  * Implicit Conversion.
  * Explicit Coversion.
    * C Style : ` double x = 10.10 ; int a = (int)x;`
    * C++ Style : basically a syntactical sugar.


**4. Virtual Destructors :** Imp. stuff when using inheritance.
  * Note : There is no such thing as virutal constructor, because (it doesn't make sense) the compiler while creating the object should know that of which class the object should be made in the first place.
  * Need : It is required specially in the case when you have a base class pointer pointing to derived class object and thus if you delete that object, then only the base class destructor will be called (unless it's virtual) and if you happen to have allocated some memory in the child class then it won't be deleted as it's destructor isn't called. thus make it virtual.

```c++
int main()  {
  Base *bp = new Derived();   // This will call the constructor of both base(bcoz of inheritance) and child class.
  delete bp;                  // Only destructor of base will be called unless it's virtual.
```


**5. Lambda functions :** Used to create anonymous functions i.e create a function without actually creating the function(not using the syntax).
  * Quick disposable functions.
  * Uses function pointers.

```c++
void forEach(vector<int> a , void (*func)(int))
{
  for (int value : values)
     func(value);
}

int main()
{
  vector<int> a (5,0);
  auto lambda = [](int value){cout << "value is : " << value<<endl; }
  forEach(a,lambda);
```


**6. Async :** `std::async` accepts a callback function and potentially executes them asynchronously(in a seperate thread, which maybe part of a thread pool - depends on current work Load) and returns a `std::future` that will eventually hold the result of that function call.
  * Only use for functions which can be called of on a seperate thread and doesn't have any requirements.
   

```c++
static std::mutex m;
void asynFunction(int a)
{ 
  std::Lock_guard<std::mutex> lock(m);  // RAII
  cout << a<<endl;
}

void callerFunction(vector<int> &a)
{
  vector<int> ans;
  for (int elem : a)
    ans.push_back(std::async(std::Launch::async , asyncFunction , elem)); 
}
```
