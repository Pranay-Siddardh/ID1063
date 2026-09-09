#include <stdio.h>

int main(void) {
    char str1[] = "Hello";
    char str2[10] = "Hello";
    char str3[] = {'H', 'e', 'l', 'l', 'o', '\0'};

    printf("%s\n", str1);
    printf("%s\n", str2);
    printf("%s\n", str3);

    /*
    A wrong version:

    char str[10];
    str = "Hello";   // ERROR: Array types are not assignable
    */

    return 0;
}
