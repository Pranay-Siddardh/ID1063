
#include <stdio.h>

int daysElapsed(int day, int month)
{
int days[] = {31, 28, 31, 30, 31, 30,
31, 31, 30, 31, 30, 31};

int total = day;  

for (int i = 0; i < month - 1; i++)  
{  
    total += days[i];  
}  

return total;

}

int main()
{
int day;
int month;

printf("Enter the day: ");
scanf("%d",&day);
printf("Enter the month: ");
scanf(" %d",&month);
int output = daysElapsed(day, month);  

printf("day = %d\n", day);  
printf("month = %d\n", month);  
printf("Days Elapsed = %d\n", output);  

return 0;

}
