#include <stdio.h>

void print_star(int i, int j, int num) {
	if ((i / num) % 3 == 1 && (j / num) % 3 == 1)
		printf(" ");
	else {
		if (num / 3 == 0)
			printf("*");
		else
			print_star(i, j, num / 3);
	}
}

int main(void) {
	int input = 0;
	scanf("%d", &input);
	int i = 0, j = 0;

	for (i = 0; i < input; i++) {
		for (j = 0; j < input; j++) {
			print_star(i, j, input);
		}
		printf("\n");
	}
	
}
