#include <stdio.h>


int main ()
{
	int i, num, soma,n;
	float media;

	soma = 0;
	i=0;
	
	printf("Insira o numero de elementos:");
	scanf("%d",&n);
	
	while (i<n)
	{
		printf("\n Insira um numero: ");
		scanf("%d",&num);
		soma=soma+num;
		i++;
	}
	media=soma/n;
	printf("\n Total: %d",soma);
	printf("\n Media: %.2f",media);
	return 0;
}
