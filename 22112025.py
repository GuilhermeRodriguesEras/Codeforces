import numpy
# https://codeforces.com/problemset/problem/2043/G    - Never end 

def calcOriginalVariable(val, last, n):
    return ((val + last) % n)
 
def op1(array, p, x):
    array[p] = x
    return array
 
def Combination2n(n):
    return (n*n - n)/2
 
def op2(array, l, r):
    array = array[l:(r+1)]
    array = numpy.unique(array)
 
    return Combination2n(array.size)
 
n = int(input())
arr = list(map(int, input().split()))
 
nparray = numpy.array(arr)
last = 0
 
for i in range(int(input())):
    operation = list(map(int, input().split()))
 
    if(operation[0] == 1):
        p = int(calcOriginalVariable(operation[1], last, n))
        x = int(calcOriginalVariable(operation[2], last, n))
        nparray = op1(nparray, p, x)
 
    else:
        l = int(calcOriginalVariable(operation[1], last, n))
        r = int(calcOriginalVariable(operation[2], last, n))
        if l > r:
            l, r = r, l
        last = op2(nparray, l, r)
 
        print(last, end= " ")
print() 