#include <stdio.h>
#include <stdlib.h>

void selectionsort_sort_asc(int array[], int numelementos) {
    int i, j, min, temp;
    for (i = 0; i < numelementos - 1; i++) {
        min = i;
        for (j = i + 1; j < numelementos; j++) {
            if (array[j] < array[min]) {
                min = j;
            }
        }
        if (min != i) {
            temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }
}

void selectionsort_sort_desc(int array[], int numelementos) {
    int i, j, max, temp;
    for (i = 0; i < numelementos - 1; i++) {
        max = i;
        for (j = i + 1; j < numelementos; j++) {
            if (array[j] > array[max]) {
                max = j;
            }
        }
        if (max != i) {
            temp = array[i];
            array[i] = array[max];
            array[max] = temp;
        }
    }
}

int binarysearch(int array[], int n, int x) {
    int meio, inicio, fim;
    inicio=0;
    fim=n;
	//binary search logic
	while(inicio<fim)
	{
	meio=(inicio + fim)/2;
		if(x<array[meio])
			fim=meio-1;
		else if(x>array[meio])
			inicio=meio+1;
		else
			return meio;
	}
}
    

int main() {
    int liminf = 1, limsup = 0, numelementos=-1, i, j, temp,x;

	while(numelementos<=0)
	{
    printf("\nInsira o numero de elementos do array: ");
    scanf("%d", &numelementos);
    
	    if (numelementos <= 0) {
	        printf("O número de elementos deve ser maior que zero.\n");
	    }
	}	

    int array[numelementos];
    int random[numelementos];

    while (liminf >= limsup) {
        printf("\nInsira o limite inferior: ");
        scanf("%d", &liminf);
        printf("\nInsira o limite superior: ");
        scanf("%d", &limsup);

        if (liminf >= limsup)
            printf("\nLimite inferior maior ou igual ao limite superior!\n");
    }

    for (i = 0; i < numelementos; i++) {
        random[i] = liminf + (float)rand() / RAND_MAX * (limsup - liminf + 1);
    }

    printf("\nArray de valores aleatórios:\n");
    for (i = 0; i < numelementos; i++) {
        printf("v[%d] = %d |", i + 1, random[i]);
    }

    
    printf("\nInsira um numero que deseja pesquisar no array:");
    scanf("%d",&x);
    printf("\nPosicao do valor procurado: %d \n", binarysearch(random, numelementos,x));
    
    selectionsort_sort_asc(random, numelementos);
    printf("\nArray ordenado em ordem crescente:\n");
    for (i = 0; i < numelementos; i++) {
        printf("%d ", random[i]);
    }

    selectionsort_sort_desc(random, numelementos);
    printf("\nArray ordenado em ordem decrescente:\n");
    for (i = 0; i < numelementos; i++) {
        printf("%d ", random[i]);
    }
   
    

    return 0;
}
