#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int verifyPalindrome (char phrase[], int length);

int main () {
	char phrase[500];
	int length;
	printf("Write an array of characters: ");
	gets(phrase);
	length=strlen(phrase);
	
	printf("\nInserted phrase: ");
	puts(phrase);

	printf("\nAmount of vowels: %d",countVogais(phrase,length));
	printf("\n");
	
	printf("\nAmount of consonantes: %d",countConsoante(phrase,length));
	printf("\n");
	
	printf("\nAmount of spaces: %d",countEspaco(phrase,length));
	printf("\n");

	printf("\nAmount of digits: %d",countDigitos(phrase,length));
	printf("\n");		
}



int verifyPalindrome (char phrase[], int length)
{

	for(int i = 0; i < length; i++)
	{
		while(phrase[i]==phrase[length])	
		{
			phrase[i]=phrase[i+1];
			phrase[length]=phrase[length-1];x
		}
	}
	
	
	return vogalcount;
}


