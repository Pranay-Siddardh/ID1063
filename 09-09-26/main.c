#include <stdio.h>


void printb(int n){
	for(int i=0; i<n; i++) printf("*");
	printf("\n");
}

int main(){
	printb(40);
	printf("HI\n");
	printb(40);
	
}
