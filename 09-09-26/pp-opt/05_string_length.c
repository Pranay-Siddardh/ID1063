#include <stdio.h>

int main(void) {
    char word[] = "abc";
    int length = 0;

    while (word[length] != '\0') {
        length = length + 1;
    }

    printf("Length = %d\n", length);

    return 0;
}
