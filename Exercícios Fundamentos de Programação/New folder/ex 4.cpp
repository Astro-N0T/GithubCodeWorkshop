#include <stdlib.h>
#include <stdio.h>
#include <time.h>
int main () {
	
	srand(time(NULL));
	int r=rand();
	int num;
	int contador=0;
	

		printf("Qual � o numero que estou a pensar? ");
		scanf("%d",&num);
	
	while(num!=r)
	{
		if(num<r)
		{
		printf("O numero que estou a pensar � maior!\n");
		printf("Qual � o numero que estou a pensar? ");
		scanf("%d",&num);
		counter=counter+1;
		}
		if(num>r)
		{
		printf("O numero que estou a pensar � menor!\n");
		printf("Qual � o numero que estou a pensar? ");
		scanf("%d",&num);
		counter=counter+1;
		}
		
	}
	if(num==r)
		{
		counter=counter+1;
		printf("\nAcertaste no n�mero! Random: %d , Input: %d, Tentativas: %d",r,num,counter);
		return 0;
		}

}

