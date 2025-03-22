#include <stdlib.h>
#include <stdio.h>
#include <time.h>
int main () {
	
	srand(time(NULL));
	int r=rand();
	int num;
	int contador=0;
	

		printf("Qual é o numero que estou a pensar? ");
		scanf("%d",&num);
	
	while(num!=r)
	{
		if(num<r)
		{
		printf("O numero que estou a pensar é maior!\n");
		printf("Qual é o numero que estou a pensar? ");
		scanf("%d",&num);
		counter=counter+1;
		}
		if(num>r)
		{
		printf("O numero que estou a pensar é menor!\n");
		printf("Qual é o numero que estou a pensar? ");
		scanf("%d",&num);
		counter=counter+1;
		}
		
	}
	if(num==r)
		{
		counter=counter+1;
		printf("\nAcertaste no número! Random: %d , Input: %d, Tentativas: %d",r,num,counter);
		return 0;
		}

}

