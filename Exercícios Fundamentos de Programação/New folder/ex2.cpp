#include <stdio.h>
#include <math.h>
int main () {
    double raio;
    double volume;
    double area;
    printf("Insira o raio da esfera: ");
    scanf("%d", &raio);

    area = M_PI * raio * raio;
    volume = (4.0/3.0 * M_PI) * raio * raio * raio;

    printf("Raio da esfera: %f\n", raio);
    printf("Area da esfera: %f\n", area);
    printf("Volume da esfera: %f", volume);

    return 0;
}

