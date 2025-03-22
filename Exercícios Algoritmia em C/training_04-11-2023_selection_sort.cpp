#include <stdio.h>
#include <stdlib.h>

void SelectionSortAsc(int array[],int size);
void SelectionSortDesc(int array[],int size);

int main () 
{
	int size;
	printf("Insert desired array's size: ");
	scanf("%d",&size);
	int array[size];
	for (int i=0; i < size; i++){
		printf("\nInsert value into position %d of the array: ",i + 1);
		scanf("%d", &array[i]);
	}
	printf("\nArray: \n");
	for (int i=0; i < size; i++){
	printf("\t%d",array[i]);
	}
	
	
	for (int i = 0; i < size; i++)
	{
		SelectionSortAsc(array,size);
	printf("\t%d",array[i]);
	}

}

void SelectionSortAsc(int array[],int size)
{
	for (int i =0;i < size; i++)
	{
		int pos= array[i];
		
		for (int j = pos+1; j < size; j++)
		{
			if(array[j] < pos)
			{
				pos = array[j];
				array[j] = array[i];
				i=i+1;
			}
		}
	}
}
void SelectionSortDesc(int array[],int size)
{
		for (int i =0;i < size; i++)
	{
		int pos= array[i];
		
		for (int j = pos+1; j < size; j++)
		{
			if(array[j] > pos)
			{
				pos = array[j];
				array[j] = array[i];
				i=i+1;
			}
		}
	}
}


