#include <stdio.h>
int main ()
{
//area e perimetro de um retangulo

	int numero, fatorial,i;	
	printf("Insira um numero:");
	scanf("%d",&numero);
	fatorial=numero;
		
		for (i=numero-1;i>0;i--) 
		{
		fatorial=fatorial*i;
		
		
	}
	
	printf("\n Fatorial do numero inserido: %.d",fatorial);	
		
}
