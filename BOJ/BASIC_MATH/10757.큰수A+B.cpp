// BOJ#10757 큰 수 A+B
// 기본 수학 1

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

#define ARRAY_MAX 10001

int chartoint(char letter) {
	if (letter >= 48 && letter <= 57)
		return (int)letter - 48;
	else
		return 0;
}	

char inttochar(int num) {
	return (char)num + 48;
}

void reverse(char* num) {
	char temp = 48;
	for (int i = 0; i < strlen(num) / 2; i++) {
		temp = num[i];
		num[i] = num[strlen(num) - 1 - i];
		num[strlen(num) - 1 - i] = temp;
	}
}

int result_len(char a[], char b[]) {
	if (strlen(a) > strlen(b))
		return strlen(a);
	else
		return strlen(b);
}

int main(void) {

	char a[ARRAY_MAX] = { 0 };
	char b[ARRAY_MAX] = { 0 }; 
	char result[ARRAY_MAX + 1] = { 0 };

	scanf("%s %s", &a, &b);
	int len = result_len(a, b);
	
	reverse(a);
	reverse(b);

	

	int sum = 0;
	for (int i = 0; i < len; i++) {
		sum = chartoint(a[i]) + chartoint(b[i]) + chartoint(result[i]);
		if (sum >= 10) {
			result[i+1] = inttochar(sum / 10);
			result[i] = inttochar(sum % 10);
		}
		else {
			result[i] = inttochar(sum);
		}
	}

	reverse(result);
	printf("%s", result);
}

