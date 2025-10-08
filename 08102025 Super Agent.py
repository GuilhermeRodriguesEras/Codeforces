matrix = [input(),input(),input()]

def see(M):
    if(M[0][0] != M[2][2]):
        return False
    if(M[0][1] != M[2][1]):
        return False
    if(M[0][2] != M[2][0]):
        return False
    if(M[1][0] != M[1][2]):
        return False
    return True
    
if(see(matrix)):
    print("YES")
else:
    print("NO")