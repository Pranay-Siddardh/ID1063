#include <stdio.h>
#include "libs/matfun.h"

int main()
{
    int m, n, T;

    printf("Enter matrix size (m n): ");
    scanf("%d %d", &m, &n);

    double **a = createMat(m, n);

    printf("Enter threshold: ");
    scanf(" %d", &T);

    printf("Enter %d x %d matrix:\n", m, n);

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf(" %d", &a[i][j]);

            if (a[i][j] >= T)
                a[i][j] = 255;
            else
                a[i][j] = 0;
        }
    }

    printf("Thresholded matrix:\n");
    printMat(a, m, n);

    return 0;
}
