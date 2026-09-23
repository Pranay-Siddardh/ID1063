//code by pranay
//date 23-09-26

#include <stdio.h>
#include <math.h>

//checks the first stable point in the array and returns the index of the first stable point
int firstStable(double a[], int n, double tolerance)
{
    for (int i = 0; i < n - 1; i++)
    {//Checks if the diff is less than the tolerance value
        if (fabs(a[i + 1] - a[i]) <= tolerance)
            return i;
    }
	//else return no stable (-1 for my reference)
    return -1;
}

int main()
{
    int n;
    double tolerance;
	printf("Enter the number of readings: ");
    scanf("%d", &n);

    double a[n];

    printf("Input the reading array: ");
    for (int i = 0; i < n; i++)
        scanf(" %lf", &a[i]);

    printf("Enter the tolerance for difference: ");
    scanf("%lf", &tolerance);

    printf("%d\n", firstStable(a, n, tolerance));

    return 0;
}
