#include <stdio.h>

int main(void) {
    char str[50];

    printf("Enter a full sentence: ");
    scanf("%49[^\n]", str);

    printf("You entered: %s\n", str);

    return 0;
}
