//Code by GVV Sharma
//June 6, 2025
//Revised June 9, 2025
//released under GNU GPL
//Find the lengths and equations of the sides of a triangle given 3 vertices
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "libs/matfun.h"
// #include "libs/geofun.h"

int main() {
int m=2, n=1;
double **A = createMat(m,n);
double **B = createMat(m,n);
double **C = createMat(m,n);
A[0][0] = 1;
A[1][0] = -1;
B[0][0] = -4;
B[1][0] = 6;
C[0][0] = -3;
C[1][0] = -5;
double **m_ab = Matsub(A,B,m,n);//A-B
double **m_bc = Matsub(B,C,m,n);//B-C
double **m_ca = Matsub(C,A,m,n);//C-A
double sideAB = Matnorm(m_ab,m);
double sideBC = Matnorm(m_bc,m); 
double sideCA = Matnorm(m_ca,m);
double **n_ab=normVec(m_ab);
double **n_bc=normVec(m_bc);
double **n_ca=normVec(m_ca);
double **c_ab=Matmul(transposeMat(n_ab,  2, 1), A, 1, 2, 1);//multiply matrices a and b
double **c_bc=Matmul(transposeMat(n_bc,  2, 1), B, 1, 2, 1);//multiply matrices a and b
double **c_ca=Matmul(transposeMat(n_ca,  2, 1), C, 1, 2, 1);//multiply matrices a and b
printf("%lf %lf %lf\n",sideAB, sideBC, sideCA);//print AB
printMat(n_ab,2,1);//normal vector of BC
printMat(n_bc,2,1);//normal vector of BC
printMat(n_ca,2,1);//normal vector of CA
printf("%lf %lf %lf\n",c_ab[0][0],c_bc[0][0],c_ca[0][0]);//constant parameters for the lines

freeMat(A,2);
freeMat(B,2);
freeMat(C,2);

freeMat(m_ab,2);
freeMat(m_bc,2);
freeMat(m_ca,2);
return (0);
}
