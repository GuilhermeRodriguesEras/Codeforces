#include <stdio.h>
#include <stdlib.h>

void nextPos(int n, int m, int layer, int* i, int*j){
    int limitI = n+layer, limitJ = m+layer;


}

void countOcorrences(char** matrix, char* comparation, int n, int m, int layer, int* ocorr) {
    int i = 0 + layer, j = 0 + layer, dx, count = 0, limit = (2*n + 2*(m-1) + 3), find;

    /*
    4x4 -> 
    n = 2 e layer = 1
    [1][2]
    [0][0] -> [0][1] -> [0][2] -> [0][3] -> [1][3] -> [2][3] -> [3][3] -> [3][2] -> [3][1] -> [3][1]
    */

    while(count < limit){
        dx = 1, find = 1;
        for(int k; k < 4; k++){
            if(matrix[i][j] != comparation[k]){
                find = 0;
                nextPos(n, m, layer, &i, &j);
                break;
            }
            else{
                dx++;
                nextPos(n, m, layer, &i, &j);
            }
        }

        if(find)
            *ocorr++;

        count += dx;
    }

    if(n != 2 && m != 2)
        countOcorrences(matrix, comparation, n-2, m-2, layer+1, ocorr);
}

int main() {

    int t;
    scanf("%d", &t);
    while (t--) {

        int n, m, ocorr = 0;
        scanf("%d %d", &n, &m);
        char comparation[5] = "1543";

        char** matrix = (char**)malloc(n * sizeof(int*));

        for (int i = 0; i < n; i++){
            matrix[i] = (char*)malloc(m * sizeof(char));
            scanf("%s", matrix[i]);
        }

        countOcorrences(matrix, &comparation, n, m, 0, &ocorr);

        printf("%d\n", ocorr);

        for (int i = 0; i < n; i++) {
            free(matrix[i]);
        }
        free(matrix);
    }


    return 0;
}