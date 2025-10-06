#include <stdio.h>
#include <stdlib.h>

void mathupsCount(int n, int* out){
    int upper = n, lower = 0, aux;

    while(upper != 1 || lower != 1){
        aux = upper/2;
        *out += aux;
        upper = aux + upper%2;
        lower += aux;
        aux = lower/2;
        *out += aux;
        lower = aux + lower%2;
    }
    (*out)++;

    return;
}

int main(){

    int size, players, mathups = 0;
    scanf("%d", &size);

    for(int i = 0; i<size; i++){
        scanf("%d", &players);
        mathupsCount(players, &mathups);
        printf("%d\n", mathups);
        mathups = 0;
    }

    return 0;
}