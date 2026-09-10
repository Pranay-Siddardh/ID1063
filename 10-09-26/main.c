#include <stdio.h>
#include <math.h>

float e = M_E;

void diff(float *xo)
{
    float xi = *xo - (expf(*xo) - 2) / expf(*xo);
    *xo = xi;
}

int main(void)
{
    // e^x - 2 = 0 implies x = ln(2)

    // Running Newton-Raphson
    float root = 1.0f;
    float old_root;

    do {
        old_root = root;
        diff(&root);

    } while (fabsf(root - old_root) > 1e-6f);

    // Printing the root
    printf("Root = %.6f\n", root);

    return 0;
}
