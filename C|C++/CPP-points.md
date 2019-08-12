
---
> Note: This file just contains some points/tips regarding C/C++, which should increase understanding and code quality.
---

<b>Ques 1</b> : Diff between structs and classes.</br>
<b>Ans</b>  : Nothing, except the fact that by default member in struct are public whereas in class are private. 

<b>Ques 2</b> : When to use class vs when use struct ?</br>
<b>Ans</b>  : When creating a new data-type only (and no function is to be created ) then use structs, when need to create functions too then use class. Basically think of class as a data-type which will act as an object whereas struct is just another user-defined data-type.

<b>Ques 3</b> : Diff between structs in C and C++?</br>
<b>Ans</b>  : In C, in order to have functions in 'struct' the <a href="https://stackoverflow.com/questions/12642830/can-i-define-a-function-inside-a-c-structure">only way is function pointers</a>, whereas in C++ we can have <a href="https://stackoverflow.com/questions/13125944/function-for-c-struct">functions as a part of struct</a>.

<b>Ques 4</b> : Type of constructors ?</br>
<b>Ans</b>  : Default , Parameterised , Copy Constructor.

<b>Ques 5</b> : Do you think constructors create objects ?</br>
<b>Ans</b>  : <a href="https://www.learncpp.com/cpp-tutorial/85-constructors/">No they don't, the compiler sets up the memory allocation for the object prior to the constructor call.</a> So though it seems that the constructor calling creates the object but in fact the first step is the object creation and second is the constructor calling and not vice-versa.

<b>Ques 6</b> : Diff ways to initialise variables ?</br>
<b>Ans</b>  : There are 3 ways :
* Copy Initialisation `int a = 4;`
* Direct Initialisation `int a(4);`
* Uniform Initialisation `int a{4};`

<b>Ques 7</b> : What is the use of these keywords : `explicit` and `delete` in constructor definition? </br>
<b>Ans</b>  : The uses are as follows: 
* The keyword `delete` in a constructor definition means that any use of this constructor will be an error.

```
class A{
  A(int a) = delete;  // Type-safety to ensure that no object is created with an integer argument as parameter i.e we can't create ab object using this constructor.
}
```

* The keyword `explicit` in a constructor definition means that type conversion won't work with that impicit constructor.

```
class A {
  string s;
  public:
    A(int x)  {     // On-passing a char as argument to this constructor would work because it's implicitly converted
      s.resize(x)
  }

# constructor re-defined
explicit A (int x)  {   // But this won't compile as we have mentioned explicit thus compiler would look for exact call matching definition . which it won't find and thus throw an error.
  s.resize(x);
}
```

<b>Ques 8</b> : How to gte `Late Binding` in C++  ? </br>
<b>Ans</b>  : Use Function Pointers.
```
int add (int x , int y) { return x+y; }
int main()  { 
  int (*fPtr)(int , int) = add ;    // function pointer to add function, which returns an integer
  cout << "Sum of 4 adn 5 is : " << (fptr)(4,5)<<endl;
}
```


<b>Ques 9</b> : What does `= delete` in a function definition means in C++11 and above ? </br>
<b>Ans</b>  : The ` = delete ` inside the function definition means that the function is in-accessible, i.e compiler will throw a run-time error we try to use it.

```
class A {
  int m_a;
  public:
    A(int x) { m_a = x; cout << "A"<<endl;  }
    void getName(){ cout << "A::getName() "<<endl;
}
class B : public A {
  public:
    B(int x) : A(x)
      {}
    void getName()  = delete;   // Function marked as in-accessible
      { cout << "B::getName() "<<endl;
}
int main()  { 
  B b;
  b.getName();      // Will throw an error because the function is marked as in-accessible using the 'delete' keyword.
  b.A::getName();   // Will work because it isn't marked in-accessible in the parent Class.
}

OUTPUT: 
A::getName()
```

<b>Ques 10</b> : Can we have a constant object of a class ? </br>
<b>Ans</b>  : Yes. In constant object of a class we won't be able to modify any member variable refered to by that object of that class.  
* Also note that if a function returns constant then it's decleration must contain 'const'.
* Moreover we can do function overloading using 'const' i.e only 'const' objects can call 'const' functions.

<b>Ques 11</b> : What all operators can we overload ? </br>
<b>Ans</b>  : First, almost any existing operator in C++ can be overloaded. The exceptions are: conditional (?:), sizeof, scope (::), member selector (.), and member pointer selector (.\*).


<b>Ques 12</b> : Should I use exit() in my code ? </br>
<b>Ans</b>  : If you use the exit() function, your program will terminate and no destructors will be called. Be wary if you’re relying on your destructors to do necessary cleanup work (e.g. write something to a log file or database before exiting).


<b>Ques 13</b> : What does the `const` keyword in the end of function decleration(in a class) mean and how is it diff from `const` in the begining ? </br>
<b>Ans</b>  : The `const` keyword in the begining of the function decleration means that this function returns a `const` value (the value itself, cant be changed), whereas the `const` keyword in the end of function decleration(in a class) means that this function is a **read-only** function i.e this function cannot write to any of the class members and can only read from it, writing inside this function will result in a compile-time error.
Also this `const` keyword can change the function definition and thus differ in function overloading/over-riding.


<b>Ques 14</b> : How does object creation work in multi-level Inheritance in C++ ? </br>
<b>Ans</b>  : C++ constructs derived classes in phases, starting with the most-base class (at the top of the inheritance tree) and finishing with the most-child class (at the bottom of the inheritance tree). As each class is constructed, the appropriate constructor from that class is called to initialize that part of the class.
```
class A { 
  public:
    int m_a;
    A() { cout << "A "; } 
};
class B : public A  { 
  public:
    int m_b;
    B() { cout << "B "; } 
};
class C : public B  { 
  public:
    int m_c;
    C() { cout << "c "; } 
};
class D : public C  { 
  public:
    int m_d;
    D() { cout << "D "<<endl; } 
};
class E : A {     // No access-specifier defaults to 'private'.
  public:
    int m_d;
    E() { cout << "E "<<endl; } 
};

int main()  {
  D d;
}
Output : 
A B C D
```
<b>Ques 15</b> : How to call constructor of parent class in case of inheritance ? </br>
<b>Ans</b>  : While calling the constructor of Parent during `inheritance` Always use **Initialisation List** and never explicitly call the constructor.
```
The Base object is constructed first using the appropriate Base constructor. If no base constructor is specified, the default constructor will be used.
class A {
  int m_a;
  public: 
    A(int a) { m_a = a; }
}
class B {
  int m_b;
  public: 
    B(int b) : A(b)   # Use initialisation List like this
    { m_b = b; }
    B(int b) 
    {
      A (b);    # Don't Do this  
      m_b = b;
     }
}
```


<b>Ques 16</b> : Can I call a constructor from another constructor ? </br>
<b>Ans</b>  : Yes, Constructor delegating (calling constructor from constructor) is possible from C++11 on, Call it in the member initialisation list only.
```
class Hello {
  int a;
  Hello() { 
    cout <<"hello non-parameterised constructor"<<endl;
  } 
  Hello(int a) 
    : a {a},    // Value init
    : Hello()   // Constructor called
  {} 
```

<b>Ques 17</b> : Explain \*this ?  </br>
<b>Ans</b>  :  The compiler does the following for you :
```
// Thats what we call
obj.setId(12);      

// What compiler does
setID(&obj, 12);    // note that 'obj' has been changed from an object prefix to a function argument!
```


<b>Ques 18</b> : How to use initialisation list in Classes ?</br>
<b>Ans</b>  : See code below:
```
#Before initialisation list
class hello
{
  int a;
  char b;
  hello(int a , char b) {
    a=a;
    b=b;
  }
};

# After Initialisation list
class hello
{
  int a;
  char b;
  hello(int a , char b) 
   : a{a} ,
     b{b}     //  direct initialisation of variables.
  {
    cout <<"Hello Constructor called" <<endl;
  }
};
```  

-> Const and reference variables) must be initialized on the line they are declared because they cannot be assigned afterwards. (Obv.) This means : 
```
class hello {
  const int a ;
  hello()   {
    a = 5;      // ERROR - Cannot assign to a constant
  }
};


# But
class hello {
  const int a ;
  hello() :   a {5}     // Works - because we are not assigning here, we are using initialisation list , which is cool.
};
```

-> Static members are not associated with class objects , nor are static functions.
```
class Hello {
  static int a;
  int val;
  static getVal(){  return val; }
};

int main()  {
  Hello::a  = 2;
  Hello::getVal();
}
Note : Cannot have static constructors though.
```

-> C++11 introduced new keyword constexpr, which ensures that a constant must be a compile-time constant:
```
constexpr double gravity { 9.8 }; // ok, the value of 9.8 can be resolved at compile-time
```

-> Note that making a specific member function a friend requires the full definition for the class of the member function to have been seen first. Keep in mind that a `friend function` is not a member function.

-> Use chrono for timing your code.

-> When overloading the stream operators i.e input-stream (istream) for `cin` or output-stream(ostream) for `cout` ,  always return a reference to `left-hand` parameter becuase it helps in chaining , which won't be possible incase the overloaded function returns `void`.

-> By default, C++ internally provides copy constructor and assignment operator, but they do `shallow copy` , thus when dealing with `dynamic memory allocation` always create your own versions of these operators and constructors.

-> In case of inheritance, if we have called a function then by default the compiler first looks for the function definition in the derived class and then walks up the inheritance chain and uses the first one it finds.


<b>Ques 19</b> : How to call a function of parent from reference of derived class object stored in parent class ? </br>
<b>Ans</b>  : Code-snippet : 
```
class Base {
  public:
    void getName(){ cout << "Base class"<<endl; }
}
class Derived {
  public:
    void getName(){ cout << "Derived class"<<endl; }
}
int main()  {
  Derived d;
  Base &b = d;  // Reference of derived class stored in base class.
  b.getName();  
}

Output : 
Base class
```

<b>Ques 20</b> : What are virtual functions when do we need one ?</br>
<b>Ans</b>  : Virtual functions are special type of function that when called , resolves to the most derived-version of the function that exists between the base and derived class (Polymorphism).
In simple words it helps to call function of derived class from reference of derived class object stored in parent class i.e what if what we want is this : a function will always exist in base class, incase someone want to modify it then **over-ride** it in the child class.

NOTE : 

  * Virtual functions work by `function over-riding` and thus the function definition should be an exact match in the base and child classes.
  * Never call virtual functions from constructors or destructors because maybe that part of the object in the derived class isn't created yet ( because in object creation , the constructor of parent is created first, and thus don't call a virtual function from parent constructor).
  * Virtual functions are slow to resolve( doubt : slow during compile time only right ? not at run-time na ? ).

```
class A{
  public:
    virtual void getName(){ cout << "A class"<<endl; }
}
class B : public A  {
  public:
    virtual void getName(){ cout << "B class"<<endl; }
}
class C : public B  {
  public:
    virtual void getName(){ cout << "C class"<<endl; }
}
class D : public C  {
  public:
    virtual void getName(){ cout << "D class"<<endl; }
}
int main()  {
  C c;
  A &a = c;  // Reference of derived class stored in base class.
  a.getName();  
}

#Output : 
C class 
  # solely because of virtual function.
``` 

<b>Ques 21</b> : How does `virtual functions` work ?</br>
<b>Ans</b>  : Virtual functions works using the `virtual table`, it's basically a table for every class (from top-most base class to bottom-most derived class), which contains the function pointer to the function, which should be actually executed when the function is called. The compiler creates the virtual table.<a href="https://www.learncpp.com/cpp-tutorial/125-the-virtual-table/">explained</a>.


<b>Ques 22</b> : What is the use of the identifier `override` ?</br>
<b>Ans</b>  : In case of inheritance when using `virtual functions`, let's say we want the derived class to over-ride a function of base class and due to some typo or implicit type-conversion, the function definition get's modified, then it won't over-ride (and we will blindly be looking out for reason what happened ), here the `override` identifier comes into place, when the compiler sees this identifier in the derived class it knows that it should over-ride and if the function doesn't over-ride the base class function the compiler will flag the function as error.

```
class A
{
public:
	virtual const char* getName1(int x) { return "A"; }
	virtual const char* getName2(int x) { return "A"; }
	virtual const char* getName3(int x) { return "A"; }
};
 
class B : public A
{
public:
	virtual const char* getName1(short int x) override { return "B"; } // compile error, function is not an override
	virtual const char* getName2(int x) const override { return "B"; } // compile error, function is not an override
	virtual const char* getName3(int x) override { return "B"; } // okay, function is an override of A::getName3(int)
 
};
 
int main()
{
	return 0;
}
```

<b>Ques 23</b> : What is the use of the identifier `final` ?</br>
<b>Ans</b>  : In the case where we want to restrict the user from overriding a function, the final specifier is used in the same place the `override` specifier is. the syntax is as :

```
// okay, overrides A::getName(), but it's child class cannot over-ride this function.
virtual const char\* getName1() override final { return "B"; } 
```

<b>Ques 24</b> : What happens if we store a derived class object in a \**ptr*  of parent class , when the member variables are dynamically created ? </br>
<b>Ans</b>  : In this case when calling destructor on the \*ptr , then it will call the destructor of parent only and not the derived class, thus woudl need to make the destructor as virtual.
Rule: Whenever you are dealing with inheritance, you should make any explicit destructors virtual.


<b>Ques 26</b> : What are and how to use pure virtual functions , abstract classes and interface classes ? </br>
<b>Ans</b>  : 
* **Interface Classes** : These are the classes that only contain all virtual functions only and no member variable and are made for the sole purpose of being inherited.
* **Abstract  Classes** : These are the classes which can only be inherited and we cannot an object of this class. Any class containing even 1 `pure virtual function` is an abstract class.
* **Pure Virtual functions** :  These are the functions that are though declared in the Parent class, but still mandatorilly needs to be over-ridden in the derived class , for their implementation. These ensure that the developer of the class wants the user of the class to necessarily `over-ride` this functionality.
But still we can provide a default behaviour to `pure virtual function` just don't define it `inline` i.e at the same place where it is declared, use a scope-resolution to define it.

```
class Base    // Abstract class
{ 
  public: 
    virtual string getName()  =  0; // '0' means that this function is a pure virtual function and thus this class is an abstract class.
}

// Providing the pure virtual function with a default behaviour.
string Base::getName()  { return string("default"); }

```


<b>Ques 27</b> : What is object slicing in c++ ? </br>
<b>Ans</b>  : The assigning of a Derived class object to a Base class object is called object slicing (or slicing for short)

```
class Base  {}
class Derived : public Base {}
int main()  {
  Derived d;
  Base &bRef = d;   // here we can still call the over-ridden functions of the derived class, obv if they are virtual declared.

  Base b = d;   // But What now ? becuase here we simply assigned the dervied class object to Base class type.
}
```
&nbsp; &nbsp; 


<b>Ques 28</b> : Why use Exception Handling in C++ ? </br>
<b>Ans</b>  : Exception handling provides a mechanism to decouple handling of errors or other exceptional circumstances from the typical control flow of your code. This allows more freedom to handle errors when and how ever is most useful for a given situation, alleviating many (if not all) of the messiness that return codes cause.

Example : 
```
#include <iostream>
#include <string>
 
int main()
{
    try
    {
        // Statements that may throw exceptions you want to handle go here
        throw -1; // here's a trivial example
    }
    catch (int x)
    {
        // Any exceptions of type int thrown within the above try block get sent here
        std::cerr << "We caught an int exception with value: " << x << '\n';
    }
    catch (double) // no variable name since we don't use the exception itself in the catch block below
    {
        // Any exceptions of type double thrown within the above try block get sent here
        std::cerr << "We caught an exception of type double" << '\n';
    }
    catch (const std::string &str) // catch classes by const reference
    {
        // Any exceptions of type std::string thrown within the above try block get sent here
        std::cerr << "We caught an exception of type std::string" << '\n';
    }
 
    std::cout << "Continuing on our merry way\n";
 
    return 0;
}
```

<b>Ques 29</b> : Does exception raised propogates to the caller function if not handled in the called function ?</br>
<b>Ans</b>  : If the exception is not handled in the called function then it does proogates to the caller function (stack unwinding) and incase it propogates to the `main()` and is still not handed there , then in that case it it exit's the program.

* The way to handle generic exceptions is as :-

```
#include <iostream>
 
int main()
{
  try
  {
    throw 5; // throw an int exception
  }
  catch (double x)
  {
    std::cout << "We caught an exception of type double: " << x << '\n';
  }
  catch (...) // catch-all (exceptions) handler
  {
    std::cout << "We caught an exception of an undetermined type\n";
  }
}
```


<b>Ques 30</b> : How to re-throw an exception in C++ ?</br>
<b>Ans</b>  : For re-throwing the same exception in C++ , simply use the `throw` keyword without any argument.

```
#include <iostream>
class Base
{
public:
    Base() {}
    virtual void print() { std::cout << "Base"; }
};
 
class Derived: public Base
{
public:
    Derived() {}
    virtual void print() { std::cout << "Derived"; }
};
 
int main()
{
    try
    {
        try
        {
            throw Derived();
        }
        catch (Base& b)
        {
            std::cout << "Caught Base b, which is actually a ";
            b.print();
            std::cout << "\n";
            throw; // note: We're now rethrowing the object here
        }
    }
    catch (Base& b)
    {
        std::cout << "Caught Base b, which is actually a ";
        b.print();
        std::cout << "\n";
    }
 
    return 0;
}

OUTPUT : 
Caught Base b, which is actually a Derived
Caught Base b, which is actually a Derived

```

<b>Ques 31</b> : How is CPP code compiled ?</br>
<b>Ans</b>  : CPP <a href="https://github.com/chrislgarry/cpp-compilation">code compilation</a> explained. 

