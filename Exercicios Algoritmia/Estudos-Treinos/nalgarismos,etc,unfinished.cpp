#include <stdio.h>

int main () {
	
	int i,nalgarismos,numero,primo,par10,impar5;
	
	printf("Insira o numero de algarismos que pretende no intervalo: ");
	scanf("%d",&nalgarismos);
	
	for(i=0;i<nalgarismos;i++)
	{
		printf("Insira um numero: ");
		scanf("%d",&numero);
		if(numero/10==0)
		{
			printf("Verifica-se que tem um numero par divisivel por 10");
		}
	}
	
}
