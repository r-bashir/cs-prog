"""
A very small calculator that only handles +, * and ( )

Note that it will give the correct priority to the operations.
Also note the usage of next! Missing call (or to many call)
to next is probbaly the most common problem students have with
the assignment.

You can use the program to see whats happens with incorrect
expressions.

"""

from MA2tokenizer import TokenizeWrapper

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()
        
        if wtok.get_previous() == '+':
            result = result + term(wtok, variables)
        if wtok.get_previous() == '-':
            result = result - term(wtok,variables)
            
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        wtok.next()
        
        if wtok.get_previous() == '*':
            result = result * factor(wtok, variables)
        if wtok.get_previous() == '/':
            result = result * factor(wtok, variables)
            
    return result


def factor(wtok,variables):
    while wtok.get_current() == '(' or wtok.get_current() == 'number':
        if wtok.get_current() == '(':
           wtok.next()                  
           result = expression(wtok,variables)
           wtok.next()      
        else wtok.get_current() == 'number':                           
           result = float(wtok.get_current())
           wtok.next() 
    
    return result


def main():
    print("Very simple calculator")
    while True:
        line = input("Input : ")
        wtok = TokenizeWrapper(line)
        if wtok.get_current() == "quit":
            break
        else:
            print("Result: ", expression(wtok))
            
    print("Bye!")
  
if __name__ == '__main__':
    main()
