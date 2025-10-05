def fixEntry(txt : str) -> list[int]:
    """
    For a string entry then have ints separeded by " ", split then and return a list with all of then
    """
    vals = txt.split()
    
    return list(map(int, vals))

def isTprime(n : int) -> bool:
    if n < 4:
        return False
    root = int(n ** 0.5)
    if root * root != n:
        return False
    if root < 2:
        return False
    for i in range(2, int(root ** 0.5) + 1):    
        if root % i == 0:
            return False
    return True

input()
vals = fixEntry(input())
for i in range(len(vals)):
    if isTprime(vals[i]):
        print("YES")
    else:
        print("NO")