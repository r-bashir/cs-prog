"""
Solutions to module 2 - A calculator
Student: Rabia Bashir
Mail: rabia.bashir.9649@student.uu.se
Reviewed by:
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


## ----- User-defined Functions
def mean (l1):
    """Computes mean of elements of a list."""
    if len(l1) == 0:
        raise EvaluationError("The list is empty.")
    else:
        return (sum(l1)/len(l1))

def log(n):
    """Computes log of a positive number"""
    if n <= 0:
        raise EvaluationError("The log() requires a positive number.")
    else:
        return math.log(n)

def fac(n):
    """Computes dactorial of a positive number"""
    if n < 0:
        raise EvaluationError("The fac() requires a positive number.")
    elif n==0:
        return 1
    else:
        return n*fac(n-1)


def fib (n):
    """Fabonacci Function with Memorization"""
    
    if n < 0:
        raise EvaluationError("The fib() requires a positive number.")
    
    # No exception, continue...
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:    
        memory = {0:0, 1:1}
        def fib_mem (n):
            if n not in memory :
                memory[n] = fib_mem(n - 1) + fib_mem(n - 2)
            return memory [n]

        return fib_mem (n)


## ----- Global Function Dicts
function_1 = {"sin": math.sin,
              "cos": math.cos,
              "tan": math.tan,
              "exp": math.exp,
              "log": log,
              "fib": fib,
              "fac": fac,
              "sqrt": math.sqrt
             }

function_n = {"sum": sum,
              "max": max,
              "min": min,
              "mean": mean         
             }


## ----- Arglist Function
def arglist (wtok, variables):
    """Get function argument as a list"""
    
    result = []
    result.append(assignment(wtok, variables))
    
    while wtok.get_current() == ',':
        wtok.next()
        result.append(assignment(wtok, variables))
    
    if wtok.get_current() == ')':
        wtok.next()
    else:
        raise SyntaxError("Expected ')'")
        
    return result

    
## ----- Exception Classes    
class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)
        
class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)     


## ----- Recursive Descent
def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok,variables)
    if not wtok.is_at_end():
        raise SyntaxError("is not at the end of the line")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    
    while wtok.get_current() == "=":
      wtok.next()
      if wtok.is_name(): 
         variables[wtok.get_current()] = result
      else:
           raise SyntaxError("Assignment operator require a variable.")
      wtok.next()

    return result

    
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
            temp = factor(wtok, variables)
            
            if temp == 0:
                raise EvaluationError("Divide by Zero.")
            else:
                result = result / temp
            
    return result

   
def factor(wtok, variables):
    """ See syntax chart for factor"""
    
    # 1: Handle Parentheses
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    
    # 2: Handle Numbers
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()           
    
    # 3: Handle Variables (Dict)
    elif wtok.get_current() in variables.keys():
        result = variables[wtok.get_current()]
        wtok.next()
    
    # 4: Handle Function_1 (Dict)
    elif wtok.get_current() in function_1.keys():
        
        Func = function_1[wtok.get_current()]       # Get the function
        wtok.next()                                 # Bypass function      
        
        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")
        else:
            wtok.next() 
        
        result = Func(assignment(wtok, variables))  # Fetch Args
        wtok.next()

    # 5: Handle Function_n   (Dict)
    elif wtok.get_current() in function_n.keys():
        
        Func = function_n[wtok.get_current()]       # Get the function
        wtok.next()                                 # Bypass function
        
        if wtok.get_current() != '(':
            raise SyntaxError("Expected '('")
        else:
            wtok.next()
        
        result = Func(arglist(wtok, variables))     # Fetch Args
        wtok.next()
    
    # 6: Handle Uniray Operator
    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)
    
    # 7: Handle Name
    elif wtok.is_name():
       raise EvaluationError("Undefined function or variable")
           
    else:
        raise SyntaxError(
            "Expected number or '('")
    
    return result


## ----------- The Main FUNCTION         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """ 
    print("Numerical calculator\n")
    
    # Variable Dict
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit' or wtok.get_current() == 'q' :
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            print(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"*** The error occurred at token '{wtok.get_current()}' just after token '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()
