from math import ceil

def fixEntry(txt : str) -> list[int]:
    """
    For a string entry then have ints separeded by " ", split then and return a list with all of then
    """
    vals = txt.split()
    
    return list(map(int, vals))

vals = fixEntry(input())
n, k = vals[0], vals[1]

sum_final = sum(list(map(lambda x: ceil(x/k), list(map(lambda x: x*n,[2,5,8])))))

print(sum_final)