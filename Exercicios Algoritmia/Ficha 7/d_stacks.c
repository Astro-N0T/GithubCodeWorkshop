#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define MSIZE 5
int top = -1;
char stack[MSIZE];


void gen_stack();
char gen_letter();
void print();
char pop_stack();
void show();
int isempty();
int isfull();

int main() {
    int x;
    time_t random;

    while (1) 
    {
        printf("1) Generate Stack! \n 2) Delete all from  stack. \n 3) Print out current stack. \n4) Print the inverted matrix.\n");
        printf("Option: ");
        scanf("%d", &x);
        switch(x) {
            case 1:
                gen_stack();
                break;
            case 2:
                pop_stack();
                break;
            case 3:
                show();
                break;
            case 4:
                print();
                break;
            case 0:
                break;
        }
    }
}

void print() 
{
    char inverted[MSIZE];
    int num = 0;
    for (int i = top; i >= 0; i--) {
        inverted[j] = stack[i];
        num++;
    }
    for (int i = 0; i <= MSIZE; i++) {
        printf("%c", inverted[i]);
    }
    printf("\n");
}

void gen_stack() 
{

    for (int i = 0; i < MSIZE; i++) {
        char plate = gen_letter();
        if (!isfull()) {
            top++;
            stack[top] = plate;
        } else {
            printf("Stack overflow\n");
        }
    }
}

char pop_stack() 
{
    if (!isempty()) {
        for (int i = 0; i < MSIZE; i++) {
            top--;
        }
    } else {
        printf("Empty stack\n");
    }
}

void show() 
{
    if (!isempty()) {
        for (int i = top; i >= 0; i--) {
            printf("%c\n", stack[i]);
        }
    }
}

int isempty() 
{
    if (top == -1) {
        return 1;
    } else {
        return 0;
    }
}

int isfull() 
{
    if (top == MSIZE) {
        return 1;
    } else {
        return 0;
    }
}

char gen_letter() 
{
    char random = rand() * time(NULL);
    return (random % 26) + 96;
}