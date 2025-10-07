#include <stdio.h>

int main(){

    int cases, candles, rest;

    scanf("%d", &cases);
    for(int i=0; i<cases; i++){
        scanf("%d",&candles);
        rest = candles%3;
        rest = (-3*(rest*rest) + (7*rest))/2;
        printf("%d\n",rest);
    }
    return 0;
}