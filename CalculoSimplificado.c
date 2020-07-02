#include <stdio.h>
#include<stdlib.h>

int main(void)
{

float totalRend = 0, Base_IRPF, IRPF = 0, prev;

int n, d, i;

prev = ;

Base_IRPF = totalRend - prev*(totalRend);

if(Base_IRPF<=12000)	printf("Isento de Imposto de Renda");

if(Base_IRPF>=12000 && Base_IRPF<=24000) IRPF = Base_IRPF * 0.15;

if(Base_IRPF>=24000) IRPF = Base_IRPF * 0.275;

printf("IRPF");

printf("Salário Liquído: %.2f\n", totalRend - IRPF);

return 0;
}
