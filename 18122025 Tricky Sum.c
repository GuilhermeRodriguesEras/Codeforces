#include <stdio.h>

int main(){

    int t;
    scanf("%d", &t);

    for(int i = 0; i < t; i++){

        long long num;
        scanf("%lld", &num);

        long long sumTotal = (num*num + num)/2;
        int aux = (int)log2(num);

        sumTotal -= 2*((1LL<<(aux +1)) -1);

        printf("%lld\n", sumTotal);
    }

    return 0;
}

/*
import math

for t in range(int(input())):

    num = int(input())

    sumTotal = (num*num + num)/2
    aux = math.floor(math.log2(num))

    sumTotal -= 2*((2**(aux +1) -1))

    print(f"{sumTotal:.0f}")
*/