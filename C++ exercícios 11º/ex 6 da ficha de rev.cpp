#include <iostream> 
#include <string.h> 
using namespace std;
int main () {
	char frase[20]; int num,i;
	cout<<"Insira o seu nome inteiro: ";
	gets(frase);
	num=strlen(frase);
	cout<<"O numero de letras da frase: "<<num<<endl;
	for(i=0;i<num;i++){
		frase[i]=tolower(frase[i]);
	}
	
	cout<<frase;
}
