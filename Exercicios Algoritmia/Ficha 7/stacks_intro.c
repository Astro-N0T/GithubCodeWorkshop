#include <stdio.h>
#include <stdlib.h>

/*
Uma pilha é uma estrutura de dados dinâmica, do tipo LIFO que tem um apontador para o topo.
A inserção push é feita no topo da pilha
A remoção pop é feita no topo
*/

// stack initialisation
#define MSIZE 14

//definir duas variáveis globais.
int stack[MSIZE]; //stack creation using an array of 15. (0 is included in the 14 declared above)
int top=-1; //top = -1, 0 é a primeira posição e neste momento o array não tem nada dentro.

/*O que é uma variável global?
Primeiro, deve-se evitar usá-las em qualquer linguagem. */

int isempty();
//devolve 1 se a pilha estiver vazia e devolve 0 se a pilha não estiver vazia
int isfull();
//devolve 1 se a pilha não estiver cheia e devolve 0 se a pilha estiver cheia
int push(int data);
//introduzir um valor após verificar que a pilha não está cheia
int pop();
//tirar um "objeto" da pilha, após retificar que a pilha não está vazia

//int peek();
//espreitar um especifico valor, ou todos os valores, do stack;

int main ()
{
  
    int x=1;
    while(!isfull())
    {
        printf("\n Push new element into the stack: ");
        scanf("%d", &x);
        push(x);
    }
    
    while(!isempty())
    {
        int data = pop ();
        printf("Value deleted from stack: %d | ",data);
    }


}





int isempty()
{
    //um if para verificar se a pilha está vazia, devolver 1 se sim, 0 se não
    if (top == -1)
        return 1;
    else    
        return 0;
}

int isfull()
{
    //um if para verificar se o topo da pilha foi atingido, (verifica se tem as posições totalmente lotadas), devolver 1 se sim, 0 se não
    if (top==MSIZE)
        return 1;
    else
        return 0;
}

int push(int data)
{
    //se o array não estiver cheio
    if(!isfull())
    {
        top = top + 1;
        stack[top] = data; //é atríbuido um valor para a posição do stack
    }
    else
    {
        printf("Stack overflow\n");
        //stack está cheio.
    }
}

int pop()
{
    int data;
    if(!isempty())
    {
        data = stack[top]; //guardar com uma variavel o valor presente no topo
        top = top - 1;
        return data; //para devolver o valor do novo topo.
    }
    else
    {
        printf("Stack is empty\n");
        //stack didnt have anything to begin with, hell are you tryna remove
    }


}