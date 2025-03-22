#include <stdio.h>
int main ()
{
//area e perimetro de um retangulo

	int base, altura, perimetro=0, area=0;
	
	printf("Insira o valor da base de um retangulo:");
	scanf("%d",&base);
	printf("Insira o valor da altura de um retangulo:");
	scanf("%d",&altura);
	
	if (base==altura)
	{
	printf("Os lados inseridos não correspondem a um retangulo!");
	}
	else
	{
	
	perimetro=(base*2)+(altura*2);
	area=base*altura;
	printf("\n Perimetro: %.d",perimetro);
	printf("\n Area: %.d",area);	
	
	}
}
