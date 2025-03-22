/*
Dada uma matriz de valores numericos (inteiros ou floats), determinar:
	a)somatorio dos valores da matriz
	b)valor minimo da matriz
	c)valor maximo da matriz
*/

#include <stdio.h>
int main ()
{

	int i,j,col,line,soma=0,min=0,max=0;
	
		
	printf("Insira o valor do numero de linhas: ");
	scanf("%d",&line);
	printf("Insira o valor do numero de colunas: ");
	scanf("%d",&col);
	int matriz[line][col];
	printf("Insira os valores dos elementos da matriz\n");
	
	
	for(i=0;i<line;i++)
	{
		for(j=0;j<col;j++)
		{
			printf("Posicao [%d][%d] = ",i+1,j+1);
			scanf("%d",&matriz[i][j]);
		}
		
	}
	printf("\n\n Matriz: \n");
	for(i=0;i<line;i++)
	{
		for(j=0;j<col;j++)
		{
			printf(" %d\t = ",matriz[i][j]);
		}
		printf("\n");
		
	}
	
	min=matriz[0][0];
	max=matriz[0][0];
	
	for(i=0;i<line;i++)
	{
		for(j=0;j<col;j++)
		{	
		
		soma=soma+matriz[i][j];
			if(matriz[i][j]>max){
				max=matriz[i][j];
			}
			if(matriz[i][j]<min){
				min=matriz[i][j];
			}
		}
	}
	
	printf("\nSoma dos elementos da matriz: %d",soma);
	printf("\nMaximo dos elementos da matriz: %d",max);
	printf("\nMinimo dos elementos da matriz: %d",min);
	return 0;
}
