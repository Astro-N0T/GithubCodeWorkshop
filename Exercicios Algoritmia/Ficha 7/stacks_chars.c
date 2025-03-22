#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAXSIZE 14

char stack[MAXSIZE];
int top = -1;

int isfull();
int isempty();
int pop();
int push(char character);

int main()
{
    char x = '1';  
    while (!isfull())
    {
        printf("\n Push new element into the stack: ");
        scanf("%c", &x);  
        push(x);
    }

    while (!isempty())
    {
        int data = pop();
        printf("Value popped from stack: %c | ", data);
    }

    return 0;
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
    if (top == MAXSIZE - 1)
        return 1;
    else
        return 0;
}

int push(char character)
{
    if (!isfull())
    {
        top++;
        stack[top] = character;
    }
    else
    {
        printf("Stack overflow!\n");
    }
}

int pop()
{
    if (!isempty())
    {
        char poppedValue = stack[top];
        top--;
        return poppedValue;
    }
    else
    {
        printf("Stack underflow!\n");
        return -1;  
    }
}

//fix later