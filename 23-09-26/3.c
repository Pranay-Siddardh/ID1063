
#include <stdio.h>

//the length of consecutive 1 counter
int runLength(int a[], int n, int i)
{
// returning length 0 as there is no 1
if (a[i] == 0)
return 0;

int count = 0;  

//this will check the one repeating for the remaining part of array frmo i and then returns l
//
while (i < n && a[i] == 1)  
{  
    count++;  
    i++;  
}  

return count;

}

int main()
{
// Example data
int n;
int k;

printf("Enter The value of n: ");
scanf(" %d",&n);
printf("Enter the value of k: ");
scanf(" %d",&k);

int a[n];

printf("Enter The vector: \n");
for(int i =0;i<n;i++){
	scanf(" %d",&a[i]);
}

int answer = 0;  

for (int i = 0; i < n; i++)  
{  
    int length = runLength(a, n, i);  
//then going to i+1 if the folloeing below beak condition doesnt satisfy.
//
//and then for each and every i , we check the length 
    if (length > k)  
    {  
        // The violation occurs at the kth+1  
        // studying session of this run.  
        answer = i + k + 1;  
        break;  
    }  
}  

printf("n = %d\n", n);  
printf("k = %d\n", k);  

printf("Entries: ");  
for (int i = 0; i < n; i++)  
{  
    printf("%d ", a[i]);  
}  

printf("\nOutput = %d\n", answer);  

return 0;

}
