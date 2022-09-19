def largest(arr, n):
    # if n = 0 means whole array
    # has been traversed
    if n == 1:
        return arr[0]
    return max(arr[n - 1], largest(arr, n - 1))


mylist = [3, 5, 9, 0, 15]
size = len(mylist)

result = largest(mylist, size)
print(result)





# Online Python - IDE, Editor, Compiler, Interpreter
def recursiveMax(a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] if a[0] > recursiveMax(a[1:]) else recursiveMax(a[1:])

l1 = [1, 2, 15, 6, 3, 2, 9]
l2 = [98, 2, 1, 1, 1, 1, ]

print(recursiveMax(l1))
print(recursiveMax(l2))


def Max(list):
    """Finding a maximum value in a list."""
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

result = Max(l1)
print(result)


def maximum2(a, n):
    if n == 1:
        return a[0]
    x = maximum2(a[n//2:], n - n//2)
    return x if x > a[0] else a[0]
def maximum(a):
    return maximum2(a, len(a))

maximum(range(99999))


def findMaxRec(A, n):
 
    # if n = 0 means whole array
    # has been traversed
    if (n == 1):
        return A[0]
    return A[n - 1] if A[n -1] > findMaxRec(A, n - 1) else findMaxRec(A, n - 1)
