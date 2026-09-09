//Code BY T.Pranay 09-09-2026
 
#include <stdio.h> 
#include <stdlib.h>
 
//Function To Take Input And String 
char *stringStorer(int n){ 
	//Mallocation for variable sizes (Dynamic memory alloc) 
	char *string = malloc((n + 1) * sizeof(char)); 
	int i = 0; 
	//reaeding chars 
	for (int i =0; i<n; i++) { scanf("%c",&string[i]); } string[n] = '\0';
        //returning the string pointer       
        return string;    
}
 
int main(void){
 
//Take the number 
printf("Enter The Number of characters(including spaces): "); 
int num; 
scanf(" %d ",&num);
 
char *strn = stringStorer(num);
 
//Print the string 
printf("The String is %s.",strn);
 
//Clearing malloc 
free(strn);
 
return 0;
}
 
