# Recursive Python3 program to
# find sum of digits of a number
 
# Function to check sum of
# digit using recursion
def sum_of_digits( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digits(int(n / 10)))
 
# Driven code to check above
num = 12345
result = sum_of_digits(num)
print("Sum of digits in",num,"is", result)
