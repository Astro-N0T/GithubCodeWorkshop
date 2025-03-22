#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void OnlyAlphabetic(char string[]);

int main() {
    char string[500];
    printf("Insert phrase: ");
    fgets(string, sizeof(string), stdin);

    OnlyAlphabetic(string);

    return 0;
}

void OnlyAlphabetic(char string[]) {
    char alphab[500];
    int n = strlen(string);
    int j = 0;  // Index for the alphab array

    for (int i = 0; i < n; i++) {
        if (isalpha((unsigned char)string[i])) {
            alphab[j] = string[i];
            j++;
        }
    }

    alphab[j] = '\0';  // Null-terminate the alphab array
    printf("\nPhrase written in alphabetic: %s\n", alphab);
}
