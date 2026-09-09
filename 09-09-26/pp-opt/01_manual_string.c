#include <stdio.h>

int main(void) {
    char word[4];

    word[0] = 'c';
    word[1] = 'a';
    word[2] = 't';
    word[3] = '\0';

    printf("%s\n", word);

    return 0;
}
