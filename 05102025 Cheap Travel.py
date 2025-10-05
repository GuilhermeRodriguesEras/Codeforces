def fixEntry(txt : str) -> list[int]:
    """
    For a string entry then have ints separeded by " ", split then and return a list with all of then
    """
    vals = txt.split()
    
    return list(map(int, vals))

vals = fixEntry(input())
n, m, a, b = vals[0], vals[1], vals[2], vals[3]

finalsum = 0

dense = b/m
if(dense > a):
    finalsum = a*n
else:
    lenght = n//m
    finalsum += b * lenght
    n = n % m
    if(a*n <= b):
        finalsum+=a*n
    else: 
        finalsum+=b

print(finalsum)