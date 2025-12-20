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
