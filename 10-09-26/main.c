#include <stdio.h>
#include <math.h>

float e = M_E;

void diff(float *xo){
	*xo = *xo - ((pow(e,*xo)-2)/(pow(e,*xo)));
}

int main(void){
//e^x -2 = 0 implies x = ln(2)	
	
	//running newton raphson
	float root = 1;
	for (int i=0;i<1000;i++){
	     diff(&root);	
	}

	//orinting the root
	printf("The root is %.6f \n",root);
	
}
