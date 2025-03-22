#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void killingmyselfslowly (char nomes[][500],float notas[],int total);
void searchanddestroy (char nomes[][500],int total);


int main (){
	int total;
	printf("Insira o numero de alunos: ");
	scanf("%d",&total);
	getchar();
	
	char nomes[total][500];
	float notas[total];
	
	for(int i = 0; i < total; i++)
	{
		printf("\nInsira a nome do aluno n%d:",i+1);
		gets(nomes[i]);
		
	}
	for(int i = 0; i < total; i++)
	{
		
		printf("\nInsira a nota do aluno n%d:",i+1);
		scanf("%f",&notas[i]);
		
		if(notas[i]<0 || notas[i]>20){
			printf("\nValor da nota tem que ser entre 0 e 20. Por favor tente de novo.");
			i=i-1;	
		}
	}
	
	searchanddestroy(nomes,total);
	killingmyselfslowly(nomes,notas,total);
		
}

void killingmyselfslowly (char nomes[][500],float notas[],int total){


	char temp2[500];
	float temp1;
    
    for (int i = 0; i < total-1; i++)
    {
        for (int j = i + 1; j < total; j++)
        {
			
            if(notas[i]<notas[j])
            {
                temp1=notas[i];
                notas[i]=notas[j];
                notas[j]=temp1;
                
                strcpy(temp2,nomes[i]);
                strcpy(nomes[i],nomes[j]);
                strcpy(nomes[j],temp2);
            }
        }
	}
	printf("\nNotas ordenadas por ordem decrescente: \n");
	 for (int i = 0; i < total; i++)
    {
    	printf("\nNome do aluno: %s \n Nota desse aluno: %f",nomes[i],notas[i]);
	}
}

void searchanddestroy(char nomes[][500],int total)
{
	int valid=0;
	char pesquisa[500];
	printf("Insira o nome a pesquisar: ");
  	getchar();  
    gets(pesquisa);
    
	for (int i = 0; i < total; i ++){
		
		if (tolower(nomes[i]) == tolower(pesquisa[i]){
			valid=1;
			break;
		}
		else{
			valid=0;
		}
	}
	if(valid=1)
	{
		printf("O nome %s existe",pesquisa);
	}
	else
	{
		printf("O nome %s nao existe",pesquisa);
	}
}

