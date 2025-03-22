#include <stdio.h>
int main ()
{
//somatorio das elementos de uma matriz quadrada

	int i,j,num,soma=0;
	
	printf("Insira o valor do numero de linhas e colunas: ");
	scanf("%d",&num);
	int matriz[num][num];
	
	printf("Insira os valores dos elementos da matriz\n");
	for(i=0;i<num;i++)
	{
		for(j=0;j<num;j++)
		{
			printf("Posicao [%d][%d] = ",i+1,j+1);
			scanf("%d\t",&matriz[i][j]);
		}
	}
	printf("\n\n Matriz: \n");
	for(i=0;i<num;i++)
	{
		for(j=0;j<num;j++)
		{
			printf(" %d\t = ",matriz[i][j]);
		}
		printf("\n");
	}
	for(i=0;i<num;i++)
		for(j=0;j<num;j++)
			soma=soma+matriz[i][j];
	
	printf("\nSoma dos elementos da matriz quadrada: %d",soma);
	return 0;
}
