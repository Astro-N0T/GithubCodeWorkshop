#include <stdio.h>
#include <stdlib.h>

	int main () {
	
		
		int liminf=1,limsup=0,numelementos,i=0,j=0,min,temp;
		
		printf("\nInsira o numero de elementos do array: ");
		scanf("%d",&numelementos);
		int array[numelementos];
		int random[numelementos];
		
		while(liminf>limsup)
		{
		
			printf("\nInsira o limite inferior: ");
			scanf("%d",&liminf);
			printf("\nInsira o limite superior: ");
			scanf("%d",&limsup);
			
			if(liminf>=limsup)
			printf("\nLimite inferior maior ou igual ao limite superior!\n");

		}
		
		//array de valores aleatórios
		for(i=0;i<numelementos;i++){
			random[i]=liminf+((float)rand()/RAND_MAX)*(float)(limsup-liminf+1);
		}
		//imprimir array de valores aleatórios
		for(i=0;i<numelementos;i++){
			printf("v[%d] = %d |", i+1,random[i]);
		}
		//selection sort
		selectionsort_sort_asc(random,numelementos);
		selectionsort_sort_desc(random,numelementos);
		
		//min
		for(i=1;i<=numelementos;i++)
		{
			min=array[i];
		
		for(j=i+1;j<numelementos;j++)
			{
				if(array[j]<array[min])
				min=j;
			}
			if(min!=i)
			{
				temp=array[i];
				array[i]=array[min];
				array[min]=temp;
			}
		}
	
		for(i=1;i<=numelementos;i++)
		printf(array[min]);
		
}
