
<h2><center>HowDoesItWork ?</center></h2>

-> Things mentioned here are specific to Cpython and may differ for different implementations of python.<br>
->  Every python object instance has a corresponding C-Type instance.<br>
-> <a id="heap">Python memory manager uses a <u><b><i>special heap</i></b></u> to keep all objects and data structures in memory.</a><br>

<h3> * Python runs it's BYTECODE in a VIRTUAL MACHINE. </h3> 

  <b>  WTF ?</b><br>
<p>
 &emsp; &emsp; <strong>Ques.1:</strong> Really <b> ByteCode </b>? isn't a compiled language like Java generates bytecode ? and iirc python is an interpreted language then why bytecode , what are you saying ?<br><br>
 &emsp; &emsp; <strong>Ques.2:</strong> What has a <b>Virtual Machine</b> got to do with python ? <br>
</p>
<b> Let me Explain....</b><br><br>
 &emsp; &emsp; <strong>Ans.1:</strong>    Yeah ByteCode , python actually first compiles the source code and generates the intermediatory bytecode (seen in a .pyc file) which is finally interpreted by the interpreter.

<img src="./CodeExecution.png">
<br>
&emsp; &emsp; &emsp;  <strong>-> Need for ByteCode? </strong><br>
&emsp; &emsp; &emsp; &emsp; &emsp;-> It improves the startup time i.e the speed with which they are loaded (<a href="https://docs.python.org/3/tutorial/modules.html#compiled-python-files">but has no affect on execution time</a>).
<br>
  &emsp; &emsp; &emsp; -> Python's <a href="#dis">'dis' (disassembler)</a> module can help in better understanding of python bytecode.
<br>
 &emsp; &emsp; &emsp; -> To simply see the corresponding bytecode of a function we can use some python builtins.<br>

```python
>>> tempVariable=10
>>> def printFunction():
...     print ("Value of tempVariable is : " , tempVariable)
>>> printFunction.__code__.co_code
b't\x00\x00d\x01\x00t\x01\x00\x83\x02\x00\x01d\x00\x00S'
```
&emsp; &emsp; <strong>Ans.2:</strong> Here the word 'Virtual Machine' refers to a 'process based Virtual Machine' & not 'system based virtual machine' like (VMWare, Vbox etc).<br>
&emsp; &emsp; &emsp;-> <strong>But why VirtualMachine ? </strong>
<br>
&emsp; &emsp; &emsp; &emsp;  &emsp; * Platform Independency i.e write once and run anywhere , it also means that not only the '.py' file but also the compiled bytecode i.e '.pyc' on 1 platform can easily run on the same python version of another platform.
<br><br>
 &emsp; &emsp; &emsp; -> Python is a <a href="https://en.wikipedia.org/wiki/Stack_machine">stack based virtual machine</a> i.e both the interpreter part and the VM part is present in the <a href="#heap">heap</a>(special heap which contains everything.
</br>
&emsp; &emsp; &emsp; -> The Virtual Machine part is responsible for executing the bytecode.
<br> 
 &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; <img src="./pythonExecutable.png">
<br>
&emsp; &emsp; &emsp; -> The CPython uses 3 different types of stack internally for it's bytecode execution.<br><br>
&emsp; &emsp; &emsp; &emsp;1. <b>Call Stack</b> : This stack primarily holds the control flow of the entire program , which also means that at entry of program this stack will always be empty. For every function call a 'frame' corresponding to that particular function is pushed in this stack and as soon as the function returns that 'frame' is popped off.
<br><br>
&emsp; &emsp; &emsp; &emsp;2. <b>Evaluation Stack</b> : In each frame, there's an evaluation stack (also called the data stack). This stack is where execution of that function occurs, and executing Python code consists mostly of pushing things onto this stack, manipulating them, and popping them back off.
<br><br>
&emsp; &emsp; &emsp; &emsp;3. <b>Block Stack</b>
Also in each frame, there's a block stack. This is used by Python to keep track of certain types of control structures: loops, try/except blocks, and with blocks all cause entries to be pushed onto the block stack, and the block stack gets popped whenever you exit one of those structures. This helps Python know which blocks are active at any given moment so that, for example, a continue or break statement can affect the correct block.
<br>
&emsp; &emsp; &emsp; <img src="./pythonStack.png">
<br>

<h4 id="dis"> Dis - disassembler </h4>
&emsp; &emsp;-> TOS : Top of Stack<br>
&emsp; &emsp;-> TOS1 : Seconds on Top of Stack<br>
&emsp; &emsp;-> TOS2 : Thirdon Top of Stack<br><br>
&emsp; &emsp;-> Walking through python bytecode using 'dis module'
<br><br>

```python
>>> import dis
>>> def result(a,b,c):                           # ---> line number 1
...     return a+b*c                             # ---> line number 2 
... 
>>> dis.dis(result)
  2           0 LOAD_FAST                0 (a)   # ---> push value of 'a' on stack , here '0' is the argument number
              3 LOAD_FAST                1 (b)   # ---> push value of 'b' on stack
              6 LOAD_FAST                2 (c)   # ---> push value of 'c' on stack
              9 BINARY_MULTIPLY                  # ---> multiply the numbers on TOS & TOS1 and store it in TOS
             10 BINARY_ADD                       # ---> add the numbers on TOS & TOS1 and store it in TOS
             11 RETURN_VALUE                     # ---> return TOS
>>>
>>> bcode=dis.Bytecode(result)
>>> for i in bcode:
...     print(i)
... 
Instruction(opname='LOAD_FAST', opcode=124, arg=0, argval='a', argrepr='a', offset=0, starts_line=2, is_jump_target=False)
Instruction(opname='LOAD_FAST', opcode=124, arg=1, argval='b', argrepr='b', offset=3, starts_line=None, is_jump_target=False)
Instruction(opname='LOAD_FAST', opcode=124, arg=2, argval='c', argrepr='c', offset=6, starts_line=None, is_jump_target=False)
Instruction(opname='BINARY_MULTIPLY', opcode=20, arg=None, argval=None, argrepr='', offset=9, starts_line=None, is_jump_target=False)
Instruction(opname='BINARY_ADD', opcode=23, arg=None, argval=None, argrepr='', offset=10, starts_line=None, is_jump_target=False)
Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=11, starts_line=None, is_jump_target=False)
>>> 
```
&emsp; &emsp;-> Explaining an instruction.<br>
&emsp; &emsp;&emsp; &emsp; * <b>opcode        </b> : numeric code for operation.<br>
&emsp; &emsp;&emsp; &emsp; * <b>opname        </b> : human readable name for operation<br>
&emsp; &emsp;&emsp; &emsp; * <b>arg           </b> : numeric argument to operation (if passed/required), otherwise None<br>
&emsp; &emsp;&emsp; &emsp; * <b>argval        </b> : resolved arg value (if known), otherwise same as arg<br>
&emsp; &emsp;&emsp; &emsp; * <b>argrepr       </b> : human readable description of operation argument<br>
&emsp; &emsp;&emsp; &emsp; * <b>offset        </b> : index of operation within bytecode sequence<br>
&emsp; &emsp;&emsp; &emsp; * <b>starts_line   </b> : line started by this opcode (if any), otherwise None<br>
&emsp; &emsp;&emsp; &emsp; * <b>is_jump_target</b> : True if other code jumps to here, otherwise False<br>

&emsp; &emsp;-> The '2' in the first line of output of `dis.dis(result)` refers to line number 2 of result().<br>
&emsp; &emsp;-> Using 'dis module' we can exactly see the opcode for every instruction that is being executed.<br>
&emsp; &emsp;-> Lets analyse the bytecode for if-else blocks and loops.<br>

```python
>>> import dis
>>> count=5
>>> def function():
...     for i in range(count):
...         if (i %2 == 0): 
...             pass
...         elif (i%3 == 0): 
...             print ("divisible by 3")
...         elif (i%4 == 0): 
...             continue
...         elif i == 5:
...             break
>>>
>>> dis.dis(function)
  2           0 SETUP_LOOP             103 (to 106) # --> Pushes a block for loop on block stack , ( to 106) means that this loop exists till instruction 105 only i.e POP_BLOCK
              3 LOAD_GLOBAL              0 (range)  # --> load global function 'range' onto stack 
              6 LOAD_GLOBAL              1 (count)  # --> load global variable 'counter' onto stack
              9 CALL_FUNCTION            1 (1 positional, 0 keyword pair)  # --> Calls the function range by creating another frame on stack and destroys that frame as soon as the function returns
             12 GET_ITER
        >>   13 FOR_ITER                89 (to 105)  # --> Now since TOS is an iterator calls it's next and push it on TOS(next instruction), incase iterator is empty pop TOS and increment byte counter so basically this will help us escape the loop when the iterator is exhausted.
             16 STORE_FAST               0 (i)   # --> Store TOS in another structure named 'co_varnames' which references local variables(here 'i')  

  3          19 LOAD_FAST                0 (i)   # --> Push reference of 'i' from structure 'co_varnames' to TOS.
             22 LOAD_CONST               1 (2)   # --> Push constant value '2' onto TOS
             25 BINARY_MODULO                    # --> TOS = TOS1 % TOS  i.e TOS = i%2
             26 LOAD_CONST               2 (0)   # --> Load constant value '0' on TOS. 
             29 COMPARE_OP               2 (==)  # --> peforms comparison operation i.e TOS = TOS1 == TOS i.e i%2 == 0
             32 POP_JUMP_IF_FALSE       38       # --> If TOS is False then set byteCode counter to 38 i.e jump to instruction 38 and pop TOS  

  4          35 JUMP_ABSOLUTE           13       # --> else if TOS is True Set byteCode counter to 13 i.e jump to instruction 13 (this step is basically if i%2==0 simply pass i.e jump back to next iteration)

  5     >>   38 LOAD_FAST                0 (i)   # --> Push reference of 'i' from structure 'co_varnames' to TOS.
             41 LOAD_CONST               3 (3)   # --> Push constant value '3' onto TOS
             44 BINARY_MODULO                    # --> TOS = TOS1 % TOS  i.e TOS = i%3
             45 LOAD_CONST               2 (0)   # --> Load constant value '0' on TOS. 
             48 COMPARE_OP               2 (==)  # --> peforms comparison operation i.e TOS = TOS1 == TOS i.e i%3 == 0
             51 POP_JUMP_IF_FALSE       67       # --> If TOS is False then set byteCode counter to 67 i.e jump to instruction 67 and pop TOS  

  6          54 LOAD_GLOBAL              2 (print)  # --> else if TOS is True then load global function 'print' onto the stack 
             57 LOAD_CONST               4 ('divisible by 3') # --> Load constant string 'divisible by 3'
             60 CALL_FUNCTION            1 (1 positional, 0 keyword pair) # --> Calls the print function and all the argument present in stack before function name are arguments to that function, when print function returns it's existence from stack is also removed.
             63 POP_TOP                          # --> POP TOS i.e remove the output of 'i%3 == 0' from stack.
             64 JUMP_ABSOLUTE           13       # -->  Set byteCode counter to 13 i.e jump to instruction 13 (now since that we have printed it's time for next iteration)

  7     >>   67 LOAD_FAST                0 (i)   # --> Push reference of 'i' from structure 'co_varnames' to TOS. 
             70 LOAD_CONST               5 (4)   # --> Push constant value '4' onto TOS  
             73 BINARY_MODULO                    # --> TOS = TOS1 % TOS  i.e TOS = i%4
             74 LOAD_CONST               2 (0)   # --> Load constant value '0' on TOS. 
             77 COMPARE_OP               2 (==)  # --> peforms comparison operation i.e TOS = TOS1 == TOS i.e i%4 == 0
             80 POP_JUMP_IF_FALSE       89       # --> If TOS is False then set byteCode counter to 89 i.e jump to instruction 89 and pop TOS  

  8          83 JUMP_ABSOLUTE           13   # --> else if TOS is True Set byteCode counter to 13 i.e jump to instruction 13 (this step is basically if i%4==0 continue )
             86 JUMP_ABSOLUTE           13   # --> idk why is this line repeated ? probably something to do with how 'continue' works ? 

  9     >>   89 LOAD_FAST                0 (i)   # --> Push reference of 'i' from structure 'co_varnames' to TOS. 
             92 LOAD_CONST               6 (5)   # --> Push constant value '5' onto TOS 
             95 COMPARE_OP               2 (==)  # --> peforms comparison operation i.e TOS = TOS1 == TOS i.e i%5 == 0
             98 POP_JUMP_IF_FALSE       13       # --> If TOS is False then set byteCode counter to 13 i.e jump to instruction 13 and pop TOS  

 10         101 BREAK_LOOP                       # --> else if TOS is True then break the loop due to encountered 'break' statement
            102 JUMP_ABSOLUTE           13       # --> Set byteCode counter to 13 i.e jump to instruction 13 i.e if the number is not divisible by 2,3,4,5 then simply skip it
        >>  105 POP_BLOCK                        # --> Remove one block from the block stack from frame, as the block stack contains blocks for try-catch , loops etc.
        >>  106 LOAD_CONST               0 (None) # --> Load constant value 'None' on TOS
            109 RETURN_VALUE                     # --> return TOS i.e 'None' to caller.
>>> 


```

<hr>
<h3> Resources|References</h3>

&emsp;--> <a href="https://opensource.com/article/18/4/introduction-python-bytecode">Python ByteCode/Virtual Machine</a><br>
&emsp;--> <a href="https://troeger.eu/files/teaching/pythonvm08.pdf">Python guide tour pdf</a><br>
&emsp;--> <a href="https://cs263-technology-tutorial.readthedocs.io/en/latest/">Python VM internals documentation</a><br>
&emsp;--> <a href="https://docs.python.org/3.4/library/dis.html">Python 'dis' module documentation</a><br>
&emsp;--> <a href="https://github.com/python/cpython/blob/master/Lib/opcode.py">Python opcode list</a><br>

