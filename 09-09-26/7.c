#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void swapper(){
	printf("Enter The String: ");
	char *string = malloc(100*sizeof(char));
	fgets(string,100,stdin);
	printf("Enter The letter to be swapped: ");
	char x;
	scanf(" %c",&x);
	printf("Enter The leter to swap ");
	char y;
	scanf(" %c",&y);
	for(int i=0;i<strlen(string);i++){
		if (string[i] == x){
			string[i] = y;
		}
	}
	printf("The Swapped String is %s",string);
}

int main(void){
	swapper();
}
