for i in range(int(input())):
    vals=list(map(int,input().split()))

    string = ""

    for j in range(vals[0]):
        if(vals[1] > 0):
            string = string + "1"
            vals[1] -= 1
        else:
            string = string + "0"
    
    print(string)