'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import numpy as np


def AND(x1, x2,th):
    x = np.array([x1, x2])
    #w = np.array([1, 1])
    y = np.sum(x)
    if y >= th:     #th is 2 bez when both x and y are 1 then it gives 1
        return 1
    else:
        return 0

def OR(x1, x2,th):
    x = np.array([x1, x2])
    #w = np.array([1, 1])
    y = np.sum(x)
    if y >= th:  #th is one value btw x and y is one then th is 1
        return 1
    else:
        return 0

def NOR(x1, x2,th):
    x = np.array([x1, x2])
    #w = np.array([2, 2])
    y = np.sum(x)
    if y == th:
        return 1
    else:
        return 0

def NAND(x1, x2,th):
    x = np.array([x1, x2])
    #w = np.array([2, 2])
    y = np.sum(x)
    if y <= th:
        return 1
    else:
        return 0
        

def NOT(x,th):
    if x == th:
        return 1
    else:
        return 0




if __name__ == '__main__':
    input = [(0, 0), (1, 0), (0, 1), (1, 1)]
   # input_not = [0,1]

    print("\nAND")
    for x in input:
        y = AND(x[0], x[1], 2)
        print(str(x) + " -  " + str(y))
    
    print("\nOR")
    for x in input:
        y = OR(x[0], x[1], 1)
        print(str(x) + " -  " + str(y))
    
    print("\nNAND")
    for x in input:
        y = NAND(x[0], x[1], 1)
        print(str(x) + " -  " + str(y))

    print("\nNOR")
    for x in input:
        y = NOR(x[0], x[1], 0)
        print(str(x) + " -  " + str(y))
        
        
    print("\nNOT")
    y = NOT(0,0);
    print(str(0) + " - " + str(y))
    y = NOT(1,0);
    print(str(1) + " - " + str(y))



