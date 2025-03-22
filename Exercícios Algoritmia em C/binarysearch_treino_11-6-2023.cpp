#include <stdio.h>
#include <stdlib.h>

void SelectionSortAsc(int array[],int size);

int BinarySearch(int array[], int size, int valor);

int main ()
{
	int size,valor;
	printf("Insert array size: ");
	scanf("%d",&size);
	int array[size];
	
	for(int i = 0; i < size; i++)
	{
		printf("Insira um elemento na posicao %d: ",i+1);
		scanf("%d",&array[i]);
	}
	printf("\nArray:\n");
		for(int i = 0; i < size; i++)
	{
		printf("%d\t",array[i]);
	}
	
	printf("\nArray ascendente:\n");
		SelectionSortAsc(array,size);
		for(int i = 0; i < size; i++)
	{	
		printf("%d\t",array[i]);
	}
	
	printf("\nValor a pesquisar:\n");
	scanf("%d",&valor);
		int i=BinarySearch(array,size,valor);
		if(i==-1)
		{
			printf("Valor nao encontrado");
		}
		else
		{
			printf("Valor encontrado");
		}

}

void SelectionSortAsc(int array[],int size)
{
	int start;
	for(int i = 0; i < size; i++){
		start=i;
		for(int j = start+1; j < size; j++)
		{
			if(array[start]>array[j]){
				int temp=array[j];
				array[j]=array[start];
				array[start]=temp;
			}
		}
	}
}

int BinarySearch(int array[], int size, int value)
{
	int inicio = 1;
	int fim = size;
	int meio;
	
	while(inicio<fim)
	{
		meio=(inicio+fim)/2;
		if(value < array[meio])
		{
			fim=meio-1;
		}
		else if(value > array[meio])
		{
			inicio=meio+1;
		}
		else 
		{
			return meio;
		}
				
	}
	return -1;
}

