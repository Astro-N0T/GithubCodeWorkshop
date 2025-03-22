#include <stdlib.h>
#include <stdio.h>

#define MAX 10
int QueueARRAY[MAX];
int front = -1;
int rear = -1;

void QInsert();
void QDelete();
void QPrint();

int main()
{
    int op;
    while (1)
    {
        printf("\n\n1 - Insert element into queue.");
        printf("\n\n2 - Eliminate element from queue.");
        printf("\n\n3 - Check elements in the queue.");
        printf("\n0 - Exit");
        printf("\n\n Select the operation: ");
        
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            QInsert();
            break;
        case 2:
            QDelete();
            break;
        case 3:
            QPrint();
            break;
        case 0:
            exit(0);
            break;
        default:
            printf("\nInvalid input");
        }
    }
}

void QInsert()
{
    int item;
    if (rear == MAX - 1)
    {
        printf("\nQueue Overflow");
    }
    else
    {
        if (front == -1)
            front = 0;
        printf("\n Insert new element into queue: ");
        scanf("%d", &item);
        rear = rear + 1;
        QueueARRAY[rear] = item; // Corrected the array name
    }
}

void QDelete()
{
    int item;
    if (front == -1 || front > rear)
    {
        printf("\nQueue is Empty! ALERT QUEUE UNDERFLOW!!!");
    }
    else
    {
        item = QueueARRAY[front];
        front = front + 1;
    }
}

void QPrint()
{
    if (front == -1 || front > rear)
        printf("\nEmpty Queue");
    else
    {
        printf("\nElements in the Queue: ");
        for (int i = front; i <= rear; i++)
        {
            printf("| %d", QueueARRAY[i]);
            printf("|");
        }
    }
}