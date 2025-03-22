#include <stdlib.h>
#include <stdio.h>

void selectionSort(int array[],int size)

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

int main () {

    int comp;
    printf("Insira o comprimento do array: ");
    scanf("%d",&comp);
    int array[comp];

    for(int i=0;i<comp;i++)
    {
        printf("\nInsira um valor para a posicao %d",i+1,": ");
        scanf("%d",&array[i]);
    }
    
	selectionSort(array,comp);
	for (int i=0;i<comp;i++)
	{
		printf("%d",array[i]);
	}
}


