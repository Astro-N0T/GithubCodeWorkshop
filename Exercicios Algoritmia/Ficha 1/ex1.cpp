#include <stdio.h>
int main ()
{
	int i, num, soma,n;
	float media;
	printf("Insira o numero de elementos:");
	scanf("%d",&n);
	soma = 0;
	
	for (i=0;i<n;i++)
	{
		printf("\n Insira um numero: ");
		scanf("%d",&num);
		soma=soma+num;
	}
	media=soma/n;
	printf("\n Total: %d",soma);
	printf("\n Media: %.2f",media);
	
}
