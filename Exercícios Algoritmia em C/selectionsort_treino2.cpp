#include <stdio.h>
#include <stdlib.h>

void SelectionSortAsc(int array[],int size);

int main ()
{
	int size;
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
		for(int i = 0; i < size; i++)
	{
		SelectionSortAsc(array,size);
		printf("%d\t",array[i]);
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

