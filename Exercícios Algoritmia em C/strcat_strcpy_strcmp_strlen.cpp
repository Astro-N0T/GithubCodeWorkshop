#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () 
{
	char phrase1[500],phrase2[500],phrase3[500],phrase4[500];
	int length1, length2, length3, length4;
	
	//string creation and declaration
	
	printf("Write an array of characters: ");
	gets(phrase1);
	length1=strlen(phrase1);
	
	printf("Write a second array of characters: ");
	gets(phrase2);
	length2=strlen(phrase2);
	
	printf("Write a third array of characters: ");
	gets(phrase3);
	length3=strlen(phrase3);
	
	printf("Write a fourth array of characters: ");
	gets(phrase4);
	length4=strlen(phrase4);
	
	//string length
	
	printf("\nPhrase 1 %s has %d characters", phrase1, length1);
	printf("\nPhrase 2 %s has %d characters", phrase1, length2);
	printf("\nPhrase 3 %s has %d characters", phrase1, length3);
	printf("\nPhrase 4 %s has %d characters", phrase1, length4);	
	
	int comparison1 = strcmp(phrase1,phrase2);
	int comparison2 = strcmp(phrase2,phrase3);
	int comparison3 = strcmp(phrase1,phrase1); 
	
	printf("\n\nPhrase 1: %s and 2: %s comparison result: %d",phrase1,phrase2,comparison1);
	printf("\nPhrase 2: %s and 3: %s comparison result: %d",phrase2,phrase3,comparison2);
	printf("\nPhrase 1: %s and 1: %s comparison result: %d",phrase1,phrase1,comparison3);
	
	//string concatenation
	printf("\n\nConcatenation between phrase 3 and phrase 4: ");
	strcat(phrase3,phrase4);
	printf("%s",phrase3);
	
	//string copy strcpy
	printf("\n\nCopying phrase 2 onto phrase 1 and displaying phrase 1.");
	printf("\nPhrase 1: %s",phrase1);
	printf("\nPhrase 2: %s",phrase2);
	
	
	strcpy(phrase1,phrase2);
	printf("\n\nPhrase 1: %s",phrase1);
	printf("\nPhrase 2: %s",phrase2);
	//a string 1 é alocada a string 2, ou seja, a string 2 é a copiada, e a string 1 == string 2

	
	
}
