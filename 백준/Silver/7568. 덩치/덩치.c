#include <stdio.h>
typedef struct {
    int height;
    int weight;
    int rank;
} person;

int main() {
    int i, j, n;
    person list[50];

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d %d", &list[i].weight, &list[i].height);
        list[i].rank = 1;
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (list[i].height < list[j].height && list[i].weight < list[j].weight) {
                list[i].rank += 1;
            }
        }
    }

    for (i = 0; i < n; i++) {
        printf("%d ", list[i].rank);
    }
    return 0;
}