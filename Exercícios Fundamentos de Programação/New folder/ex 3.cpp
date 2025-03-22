#include <stdio.h>
#include <math.h>
int main () {
	char op;
	float celsius;
	printf("Insert the desired temperature in Celsius: ");
	scanf("%f",&celsius);

		printf("Escolha entre 0 a 2: \n 1: Fahrenheit \n 2: Kelvin \n 0: Exit\n\n Inserir: ");
		fflush(stdin);
		scanf("%c",&op);
	
	switch (op) {
		
		
	case '1':
		celsius=(9/5*celsius)+32;
			printf("Em fahrenheit: %.3f",celsius);
		break;
	
	case '2':
		celsius=celsius+273;
		printf("Em kelvin: %.3f",celsius);
		break;
		
	case '0':
		return(0);
		break;
		
	default:
		printf("%f",celsius);
	
	
	
	}
}

