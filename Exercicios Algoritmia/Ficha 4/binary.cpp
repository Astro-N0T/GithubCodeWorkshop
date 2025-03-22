#include <stdlib.h>
#include <stdio.h>

void iSelectionSort(int array[],int size)


{
	for(int inicialciclo=0;inicialciclo<size;inicialciclo++)
	{
		int inicial=inicialciclo;
		
		for(int apontador=inicial+1;apontador<size;apontador++)
		{
			
			if(apontador<inicial)
			{
				inicial=apontador;
			}
			
			
			
			if(inicial!=inicialciclo)
			{
				int valortemp=array[apontador];
				array[apontador]=array[inicial];
				array[inicial]=valortemp;
				
			}
			
		}
		
	
	}
	
}

void rBinarySearch(int array[],int initial, int final, int value)
{
	int middle=(initial + final) / 2;
		
		if(array[middle] == valor)
		{
			return middle;
		}
		if(array[mid]>valor)
		{
			return -1;
		}
		else
			if(array[middle]<valor)
				return rBinarySearch(array, middle+1, final, value);
			else
				return rBinarySearch(array, initial, middle-1, value);
}

void iBinarySearch(int array[], int comp, int value)
{
	int middle=0,initial=0;
	int mid=(initial + final) / 2;
	
		if(array[mid]==valor)
		{
			printf("\n A posicao do valor a pesquisar: %d",mid);
		}
		while(array[mid]!=valor)
		{
			if(array)
		}
}





int main () {

    int comp,min,max=0;
    printf("Insira o comprimento do array: ");
    scanf("%d",&comp);
    int array[comp];

    for(int i=0;i<comp;i++)
    {
        printf("\nInsira um valor para a posicao %d",i+1,": ");
        scanf("%d",&array[i]);
        
        if(max<array[i])
		{
			max=array[i];
			min=array[i];
		}        
		if(array[i+1]<min)
		{
			min=array[i+1];
		}
    }
    
	iSelectionSort(array,comp);
	for (int i=0;i<comp;i++)
	{
		printf("%d",array[i]);
	}
	
	rBinarySearch
}


