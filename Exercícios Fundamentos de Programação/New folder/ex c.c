#include <stdio.>
#include <stdlib.h>
#include <math.h>

struct ponto{
        int x;
        int y;
    }abc;

struct ponto ler_ponto(char* label)
{
    struct ponto p;
    printf("%s: Insira coordenadas x y: ",label);
   scanf("%d%d, &p.x, &p.y ");

    return p;
}

void imprime_ponto 
{
    printf("%s(%d, %d)", label, p.x, p.y)
}

double distancia_entre_pontos (struct ponto p1, struct ponto p2)
{
    return sqrt(
        pow(p1.x - p2.x, 2) 
    +   pow(p1.y - p2.y, 2)
    );
}

int main()
{


    struct ponto p1, p2;

    p1 = ler_ponto("P1");
    p2 = ler_ponto("P2");

    imprime_ponto("P1", p1);
    imprime_ponto("P2", p2);


    struct ponto p2;
    struct ponto p4 = { 1, 1 };

    p2.x = 2;
    p2.y = 3;






}