#!/usr/bin/env python
# coding: utf-8

students = ["Rabia", "Amina", "Ali"]
for x in students:
       print(x)

student = "Rabia"
for x in student:
       print(x)

students = ["Rabia", "Sara", "Amina", "Ali"]
for x in students:
        print(x)
        if x=="Amina":
          break

students = ["Rabia", "Sara", "Amina", "Ali"]
for x in students:
       if x == "Amina":
              break
       print(x)

students = ["Rabia","Sara","Amina","Ali"]
for x in students:
       if x == "Amina":
          continue
       print(x)


for x in range(6):
       print(x)
else:
    print("Finally ended!")



for x in range(6):
     print(x)
     if x == 3:
            break
else:
     print("Finally finished")



for x in range(6):
   if x == 3:
     break
   print(x)
else:
    print("finished")


set_1 = ("sara", "ali", "nida")
set_2 = (1, 2, 3)
for x in set_1:
    for y in set_2:
        print(x,y)

def my_func(fname):
    print(fname +  " pass")
my_func("Rabia")
my_func("Sara")

def greet_user(name1, name2):
    print(f'Hi {name1}! Hi {name2}!')
    print("Welcome aboard")
print("Start")
greet_user("Rabia", "Mehreen")
print("Finished")



def greet_name(fname,lname):
    print(fname+lname)
greet_user("Rabia","Bashir")

for x in range(-10,0,2):
    print(x)

for x in range(5):
    print(x)
else:
    print("done!")




#result = 1
#num = int(input("number to find factorial:"))
#if num < 0:
    #print("Sorry, fcatorial not exist ")
#elif num == 0:
    #print("Factorial of 0 is 1")
#else:
    #for i in range(1,num+1):
       # result *= i
    #print("The fac of number",num ,"is ", result)


def factorial(n):
    if n == 1:
      return 1
    elif n < 0:
        print("doent exist")
    elif n == 0:
        print("fac is 1")
    else:
      return (n*factorial(n-1))

num = int(input("Enter the number:"))
result = factorial(num)
print("the factorial of", num, "is", result)



list = [4,5,6,7]
reverse(list[])