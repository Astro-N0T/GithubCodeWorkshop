#include <stdio.h>
#include <stdlib.h>

void BubbleSort(int array[], int size);

int main () {
	int size;
	printf("Insert array size: ");
	scanf("%d",&size);
	int array[size];
	for (int i = 0; i < size; i++)
	{
		printf("\nInsert value onto position %d: ", i+1);
		scanf("%d",&array[i]);		
	}
	printf("\n Array:\n");
	for (int i = 0; i <  size; i++)
	{
		printf("%d \t",array[i]);
	}
	printf("\n Bubble Sort:\n ");
	BubbleSort(array,size);
		for (int i = 0; i <  size; i++)
	{
		
		printf("%d \t",array[i]);
	}
	
}
void BubbleSort(int array[], int size)

{
	for(int i = 0; i < size; i++)
	{
		for(int j = 0; j < size -1; j++)
		{
			if(array[j+1]>array[j])
			{
			int temp = array[j];
			array[j]= array[j+1];
			array[j+1] = temp;
			}
		}
		
	}
}
