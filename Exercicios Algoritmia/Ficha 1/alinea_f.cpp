#include <stdio.h>
int main ()
{
int quantity, num;

printf("Insira a quantidade de numeros no intervalo: ");
scanf("%d",&quantity);

	for(int i = 0; i < quantity; i++)
	{
	printf("\nInsira um numero para a posicao %d: ",i+1);
	scanf("%d",&num);
	
		if (num % 2 == 0) {
	        printf("\nO numero inserido apresenta ser par!\n");
	    }
	    else
	    {
	 	    printf("\nO numero inserido apresenta ser impar!\n");	
		}
	}
	
}

