#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int AbsoluteFrequenceOfAString (char phrase[], int length);


int main () {
	char phrase[500];
	int length;
	printf("Write an array of characters: ");
	gets(phrase);
	length=strlen(phrase);
	
	printf("\nInserted phrase: ");
	puts(phrase);

	} 

int AbsoluteFrequencyOfAString (char phrase[], int length)
{
	char alphabet[]= "abcdefghijklmnopqrstuvwxyz";
	char digits [10] = "0123456789";
	
	int freqalphabet[26];
	int freqdigits[10];
	
	for(int j = 0; j < strlen(alphabet); j++)
	{
		freqalphabet[j] = 0;
	}
		for(int j = 0; j < strlen(digits); j++)
	{
		freqdigits[j] = 0;
	}
	
	for(int i = 0; i < length; i++)
	{
		for(int j = 0; j < strlen(alphabet); j++)
		{
			if(alphabet[j]=tolower(phrase))
			{
				freqalphabet[j]++;
				printf("\n%d: %d",alphabet[j],j);
			}
			for(int j = 0; j < strlen(digits); j++)
			{
				freqdigits[j]++;
				printf("\n%d: %d",digits[j],j);
			}
		}
	}
}
