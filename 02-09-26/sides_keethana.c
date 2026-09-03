//Code by GVV Sharma
//June 6, 2025
//Revised June 9, 2025
//released under GNU GPL
//Find the lengths and equations of the sides of a triangle given 3 vertices
//Code by GVV Sharma
//June 6, 2025
//Revised June 9, 2025
//released under GNU G
//
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double **createMat(int m, int n);
double **transposeMat(double **a, int m, int n);
double **Matmul(double **a, double **b, int m, int n, int p);
void printMat(double **p, int m, int n);
void freeMat(double **p, int m);

#include "libs/matfun.h"

int main() {
    int m;
    printf("Enter the value of n: ");
    if (scanf("%d", &m) != 1 || m <= 0) return 1;

    int n = 1;

    double **V = createMat(m, n);
    for (int i = 0; i < m; i++) {
        V[i][0] = i + 1;
    }

    double **V_trans = transposeMat(V, m, n);
    double **result = Matmul(V, V_trans, m, n, m);

    printMat(result, m, m);

    freeMat(V, m);
    freeMat(V_trans, n);
    freeMat(result, m);

    return 0;
}



