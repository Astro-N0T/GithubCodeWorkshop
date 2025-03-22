#include <stdio.h>
int main ()
{
	int lado1, lado2;
printf("Insira o valor de um lado:");
scanf("%d",&lado1);
printf("Insira o valor do outro lado:");
scanf("%d",&lado2);
	
	if (lado1==lado2)
	{
	printf("Os lados inseridos não correspondem a um retangulo!");
	}
	else
	{
	printf("Os lados inseridos correspondem a um retangulo!");	
	}
}
