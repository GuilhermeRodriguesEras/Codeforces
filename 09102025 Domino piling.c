#include <stdio.h>

int main() {
    int m, n, total;
    scanf("%d %d", &m, &n);

    total = (m/2 *n) + (m%2* (n/2));
    printf("%d\n",total);

    return 0;
}