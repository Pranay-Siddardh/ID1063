#include <stdio.h>

int main(void) {
    char word[100];
    int vowels = 0;

    scanf("%99s", word);

    for (int i = 0; word[i] != '\0'; i = i + 1) {
        if (word[i] == 'a' || word[i] == 'e' ||
            word[i] == 'i' || word[i] == 'o' ||
            word[i] == 'u') {
            vowels = vowels + 1;
        }
    }

    printf("Number of vowels = %d\n", vowels);

    return 0;
}
