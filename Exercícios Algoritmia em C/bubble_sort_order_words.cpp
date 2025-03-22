/*
inverter texto
vogais, consoantes, digitos, espacos
string output de chars alfabeticos de uma determinada string
inverter texto
verificacao de palindrome
numero de palavras
(inserir numero de palavras para o utilizador escrever)
ordenar por ordem crescente 5 palavras por lexicografia - bubble sort
(inserir numero de palavras para o utilizador escrever)
ordenar por ordem decrescente essas palavras por lexicografia - bubble sort
*/

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void WordingBubbleSort ();

int main () {

	WordingBubbleSort();

}
void WordingBubbleSort ()
{
	int n,i,j;
	printf("\nAmount of words: ");
	scanf("%d",&n);
	char str[n][500], temp[500];
	//array bidimensional representativo do conjunto de palavras n, com 500 de array size por palavra
	for (int i = 0; i < n; i++)
	{
		printf("%d palavra: ",i+1);
		scanf("%s",str[i]);
	}
	
	for (int i = 0; i < n-1; i++)
	{
		for (int j = i + 1; j < n; j++)
		{

			if(strcmp(str[i],str[j]) > 0)
			{
				strcpy(temp,str[i]);
				strcpy(str[i],str[j]);
				strcpy(str[j],temp);
			}
		}
	}
	printf("\nIn the lexographical order: \n");
	for(int i = 0; i < n; i++){
		puts(str[i]);
	}
		//print para a string;
	
	
}
