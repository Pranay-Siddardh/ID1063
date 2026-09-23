#include <stdio.h>
#include <math.h>

double rms(double *array,int num){
	double sumsq = 0;
	for(int i=0;i<num;i++) sumsq+=pow(*(array+i),2);
	return pow(sumsq/num,0.5);
}

int main(void){

int num; 

printf("Input cases:- 4 , 3 4 0 5 \n");
num = 4;
double numbers[4] = {3,4,0,5};

printf("The rms value is %.2lf\n",rms(numbers,num));

printf("Input cases:- 4 , 1 -1 1 -1 \n");
 num = 4;
 double numbers1[4] = {1,-1,1,-1};
 printf("The rms value is %.2lf\n",rms(numbers1,num));

 printf("Input cases:- 1 , 7.5 \n");
 num = 1;
 double numbers2[1] = {7.5};
 printf("The rms value is %.2lf\n",rms(numbers2,num));

 return 0;
}
