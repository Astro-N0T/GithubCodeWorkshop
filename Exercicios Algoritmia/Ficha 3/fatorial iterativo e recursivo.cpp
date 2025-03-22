
#include <stdio.h>
#include <stdlib.h>




//function fatorial iterativo
int main ()
{
	int i,num, fatorial;
		printf("Insira um numero inteiro: ");
		scanf("%d",&num);
		
	
	fatorial=1;
	for(i=2;i<=num;i++)
	fatorial*=i;
	//return(fatorial);
	
	
}

	//function fatorial recursiva
long fatorialrec (int num){

	if(num==0) return 1;
	return(num * fatorialrec(num-1));
		
}

