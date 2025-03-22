#include <iostream>
using namespace std;
int main () {
	int alunos,i,nota,soma=0;
	float media;
	
	cout<<"Insira o numero de alunos da turma: ";
	cin>>alunos;
	for(i=0;i<alunos;i++){
		cout<<"Insira a nota obtida pelo aluno n"<<i+1<<" : ";
		cin>>nota;
		soma=soma+nota;
	}
	media=soma/alunos;
		
		cout<<"A media da turma: "<<media;
	}
