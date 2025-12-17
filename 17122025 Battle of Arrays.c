#include <stdio.h>
#include <stdlib.h>

void solve() {
    int n, m;

    if (scanf("%d %d", &n, &m) != 2) return;

    int *arrA = (int *)malloc(n * sizeof(int));
    int *arrB = (int *)malloc(m * sizeof(int));

    for (int i = 0; i < n; i++) scanf("%d", &arrA[i]);
    for (int i = 0; i < m; i++) scanf("%d", &arrB[i]);

    int sizeA = n;
    int sizeB = m;
    int turn = 1;

    while (sizeA > 0 && sizeB > 0) {

        int Alice_max_idx = 0;
        for (int i = 1; i < sizeA; i++) {
            if (arrA[i] > arrA[Alice_max_idx]) Alice_max_idx = i;
        }
        int Alice_max = arrA[Alice_max_idx];

        int Bob_max_idx = 0;
        for (int i = 1; i < sizeB; i++) {
            if (arrB[i] > arrB[Bob_max_idx]) Bob_max_idx = i;
        }
        int Bob_max = arrB[Bob_max_idx];

        if (turn == 1) { 
            if (Alice_max >= Bob_max) {

                for (int i = Bob_max_idx; i < sizeB - 1; i++) arrB[i] = arrB[i + 1];
                sizeB--;
            } else {
                arrB[Bob_max_idx] = Bob_max - Alice_max;
            }
            turn = 0;
        } else { 
            if (Bob_max >= Alice_max) {

                for (int i = Alice_max_idx; i < sizeA - 1; i++) arrA[i] = arrA[i + 1];
                sizeA--;
            } else {

                arrA[Alice_max_idx] = Alice_max - Bob_max;
            }
            turn = 1;
        }
    }

    if (sizeA == 0) {
        printf("Bob\n");
    } else {
        printf("Alice\n");
    }

    free(arrA);
    free(arrB);
}

int main() {
    int t;
    if (scanf("%d", &t) != 1) return 0;
    while (t--) {
        solve();
    }
    return 0;
}