#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 19

int queue[MAXSIZE];
int front=-1;
int rear=-1;

int isfull();
int isempty();
int enqueue(int value);
int dequeue();
int peek();

int isfull()
{
    if(rear==MAXSIZE)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isempty()
{
    if(front==-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int enqueue(int value)
{
    if(!isfull())
    {

    }
    else
    {
        printf overflow;
    }
}

int dequeue()
{
    if(rear==-1)
    {
        
    }
    else

    {
        
    }


}