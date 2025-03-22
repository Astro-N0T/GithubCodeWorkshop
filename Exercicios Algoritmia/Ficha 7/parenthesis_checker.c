#include <stdio.h>
#include <stdlib.h>

int msize = 50;
char stack[100];
int top = -1;

void push(char data);
char pop();
int isempty();
int isfull();
int findChar(char str[], char car);
int checkMathParenthesis(char exp[]);

int main ()
{
    char exp[50];

    //Leitura da expressao e analise dos parentesis;
    printf("\n\n Insert math expression: ");
    scanf("%s",&exp);
    checkMathParenthesis(exp);


}

void push (char data)
{
    if (!isfull())
    {
        top = top + 1;
        stack[top] = data;
    }
    else
    {
        printf("\n Stack overflow!");
    }   
}

char pop()
{
    int data;
    if (!isempty())
    {
        data = stack[top]; 
        top = top - 1;
        return data; 
    }
    else
    {
        printf("\n Stack is empty!");
    }
}

int isempty()
{
    if (top == -1)
        return 1;
    else    
        return 0;
}

int isfull()
{
    if (top==msize)
        return 1;
    else
        return 0;
}


int findChar(char str[], char car)
{
    for(int i = 0; str[i] != '\0'; i++)
    {
        if(str[i] == car)
            return i;
    }
    return -1;
}


int checkMathParenthesis(char exp[])
{
    int i;
    char car, par;
    char par_abre[] = "{[(";
    char par_fecha[] = "}])";
    //para todos os caracteres da expressao
    for (i = 0; exp[i] != '\0'; i++)
    {
        car = exp[i];
        // empilha parentesis abertos
        if (findChar(par_abre, car) != -1)
            push(car);

        // verifica parentesis fechados
        if (findChar(par_fecha, car) != -1)
        {
            if (!isempty())
            {
                par = pop();
                // verificar compatibilidade
                if(findChar(par_fecha,car) != findChar(par_abre,par))
                {
                    printf("\nInvalid expression! One ore moc closed parenthesis from the expression is of a different type!");
                    return 0;
                }
            }
        }
        
            if (!isempty())
            {
                printf("\n Invalid expression! The expression has a parenthesis left unclosed!");
            }
            else
            {
                printf("\n Invalid expression!");
                return 0;
            }
    }
}