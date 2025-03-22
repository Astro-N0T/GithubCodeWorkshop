#include <stdio.h>

// função fibonacci recursiva
long long int fibonaccirec(int num) {
    if (num <=1) return num;
    return fibonaccirec(num - 1) + fibonaccirec(num - 2);
}

int main() {
		int num;
		printf("Insira um numero inteiro: ");
		scanf("%d",&num);
		
		
	printf("%lli",fibonaccirec(num));
}

