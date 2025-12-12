def possibilidades(num):
    
    if(num % 2 == 1):
        return 0
     
    return (num//4) + 1
    




for t in range(int(input())):
    num = int(input())

    print(f"{possibilidades(num):.0f}")