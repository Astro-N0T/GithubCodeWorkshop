#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void sortCharacterAsc (char phrase[], int length);
void sortCharacterDesc (char phrase[], int length);
int countCharacter (char phrase[], int length);


int main () {
	char phrase[500];
	int length;
	printf("Write an array of characters: ");
	gets(phrase);
	length=strlen(phrase);
	
	printf("\nInserted phrase: ");
	puts(phrase);

	printf("\nAmount of encounters: %d",countCharacter(phrase,length));
	printf("\n");
	
	printf("\nAscendant phrase:");
	sortCharacterAsc(phrase,length);
	puts(phrase);
	
	printf("\nDescendant phrase:");
	sortCharacterDesc(phrase,length);
	puts(phrase);
}

void sortCharacterAsc (char phrase[], int length)
{
	
	for (int i=0; i < length; i++)
	{
		for(int j=i+1; j < length; j++)
		{
			if(phrase[j]>phrase[j-1])
			{
				int temp=phrase[j];
				phrase[j]=phrase[i];
				phrase[i]=phrase[j];
			}
		}
	}
}

void sortCharacterDesc (char phrase[], int length)
{
	
	for (int i=0; i < length; i++)
	{
		for(int j=i+1; j < length; j++)
		{
			if(phrase[j]<phrase[j-1])
			{
				int temp=phrase[j];
				phrase[j]=phrase[i];
				phrase[i]=phrase[j];
			}
		}
	}
}

int countCharacter (char phrase[], int length)
{
	char car;
	int soma=0;
	printf("\nInsert wanted character: ");
	scanf("%c",&car);
	for(int i = 0; i < length; i++)
	{
		if (phrase[i]==car)
		{
			soma=soma+1;
		}
	}
	return soma;
}
