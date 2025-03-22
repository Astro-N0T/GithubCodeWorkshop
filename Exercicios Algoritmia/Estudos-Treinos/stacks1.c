#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 19

int stack[MAXSIZE];
int top=-1;

int isempty();
int isfull();
int pop();
int push(int data);

int isempty()
{
    if(top==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isfull()
{
    if(top==MAXSIZE)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int pop()
{
    int data;
    if (!isempty())
    {
        data=stack[top];
        top=top-1;
        return data;
    }
    else
    {
        printf("shit no work");
    }
}

int push(int data);
{
    if(!isfull())
    {
        top=top+1;
        stack[top]=data;
    }
    else
    {

    }
}