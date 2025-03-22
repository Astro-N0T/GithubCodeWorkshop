#include <stdio.h>
#include <stdlib.h>

int main() {
    int N;

    // Read the value of N with validation using a while loop
    printf("Introduza um valor para um vetor (1 < N <= 20): ");
    scanf("%d", &N);
    while (N <= 1 || N > 20) {
        printf("Valor invalido! Por favor, introduza um valor entre 2 e 20.\n");
        printf("Introduza um valor para um vetor (1 < N <= 20): ");
        scanf("%d", &N);
    }

    int array[N];

    // Read N integer values from the user
    printf("Introduza %d valores inteiros:\n", N);
    for (int i = 0; i < N; i++) {
        printf("Valor %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    // Determine the maximum and minimum values
    int max = array[0];
    int min = array[0];
    for (int i = 1; i < N; i++) {
        if (array[i] > max) {
            max = array[i];
        }
        if (array[i] < min) {
            min = array[i];
        }
    }

    // Print the maximum and minimum values
    printf("O elemento maior é: %d\n", max);
    printf("O elemento menor é: %d\n", min);

    return 0;
}