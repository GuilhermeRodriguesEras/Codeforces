def fixEntry(txt : str) -> list[int]:
    """
    For a string entry then have ints separeded by " ", split then and return a list with all of then
    """
    vals = txt.split()
    
    return list(map(int, vals))

def array_james(n : int) -> list[int]:
    """
    Create the james array used on problem
    """
    return_array = []
    for i in range(1, n+1):
        auxarray = list(range(1,i+1))
        return_array.extend(auxarray)

    return return_array

def count_subarrays(array : list[int], sub_array : list[int]) -> int:
    """
    Return Number of ocorences of a subarray on array 
    """
    count = 0
    i = 0
    cond = True
    while(i < len(array)):
        dx = 0
        cond = True

        for j in range(len(sub_array)):
            dx += 1 
            if(sub_array[j] != array[i + dx - 1]):
                cond = False
                break

        if(cond):
            count+=1
        i += dx 
        
    return count

for i in range(int(input())):
    vals = fixEntry(input())
    favorityNumber = fixEntry(input())

    JamesArray = array_james(vals[0])

    num_subarrays = count_subarrays(JamesArray, favorityNumber)
    print(num_subarrays)
