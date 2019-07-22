#!/usr/bin/python2.7

import c_functions      # this imports the shared object and not the ".pyx" file.

def main():
    x  = 10
    print ("Sin function on {} is : ".format(x) , c_functions.csin(x))
    print ("Square_Sin function on {} is : ".format(x) , c_functions.square_sin(x))
    c_functions.allocMemoryAndPrint()
    c_functions.defined_Dictionary()

if __name__ == "__main__":
    main()
