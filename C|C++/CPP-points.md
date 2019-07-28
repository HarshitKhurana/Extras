
---
> Note: This file just contains some points/tips regarding C/C++, which should increase understanding and code quality.
---

<b>Ques</b> : Diff between structs and classes.</br>
<b>Ans</b>  : Nothing, except the fact that by default member in struct are public whereas in class are private. 

<b>Ques</b> : When to use class vs when use struct ?</br>
<b>Ans</b>  : When creating a new data-type only (and no function is to be created ) then use structs, when need to create functions too then use class. Basically think of class as a data-type which will act as an object whereas struct is just another user-defined data-type.

<b>Ques</b> : Diff between structs in C and C++?</br>
<b>Ans</b>  : In C, in order to have functions in 'struct' the <a href="https://stackoverflow.com/questions/12642830/can-i-define-a-function-inside-a-c-structure">only way is function pointers</a>, whereas in C++ we can have <a href="https://stackoverflow.com/questions/13125944/function-for-c-struct">functions as a part of struct</a>.

<b>Ques</b> : Type of constructors ?</br>
<b>Ans</b>  : Default , Parameterised , Copy Constructor.

<b>Ques</b> : Do you think constructors create objects ?</br>
<b>Ans</b>  : <a href="https://www.learncpp.com/cpp-tutorial/85-constructors/">No they don't, the compiler sets up the memory allocation for the object prior to the constructor call.</a> So though it seems that the constructor calling creates the object but in fact the first step is the object creation and second is the constructor calling and not vice-versa.

<b>Ques</b> : Diff ways to initialise variables ?</br>
<b>Ans</b>  : There are 3 ways :
* Copy Initialisation `int a = 4;`
* Direct Initialisation `int a(4);`
* Uniform Initialisation `int a{4};`

<b>Ques</b> : What is the use of these keywords : `explicit` and `delete` in constructor definition? </br>
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


<b>Ques</b> : Can we have a constant object of a class ? </br>
<b>Ans</b>  : Yes. In constant object of a class we won't be able to modify any member variable refered to by that object of that class.  
* Also note that if a function returns constant then it's decleration must contain 'const'.
* Moreover we can do function overloading using 'const' i.e only 'const' objects can call 'const' functions.

<b>Ques</b> : What all operators can we overload ? </br>
<b>Ans</b>  : First, almost any existing operator in C++ can be overloaded. The exceptions are: conditional (?:), sizeof, scope (::), member selector (.), and member pointer selector (.\*).


<b>Ques</b> : Should I use exit() in my code ? </br>
<b>Ans</b>  : If you use the exit() function, your program will terminate and no destructors will be called. Be wary if you’re relying on your destructors to do necessary cleanup work (e.g. write something to a log file or database before exiting).


<b>Ques</b> : Can I call a constructor from another constructor ? </br>
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

<b>Ques</b> : Explain \*this ?  </br>
<b>Ans</b>  :  The compiler does the following for you :
```
// Thats what we call
obj.setId(12);      

// What compiler does
setID(&obj, 12);    // note that 'obj' has been changed from an object prefix to a function argument!
```


<b>Ques</b> : How to use initialisation list in Classes ?</br>
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
