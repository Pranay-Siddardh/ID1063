#include <stdio.h>

double calcarea(double len, double breadth){
	double area = len*breadth;
	return area;
}

int  main(void){
	double l,b;
	printf("Enter The Length: ");
	scanf(" %lf",&l);
	printf("Enter The Breadth: ");
	scanf(" %lf",&b);
	printf("The Area is %.4lf sq.units",calcarea(l,b));
}
