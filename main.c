#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include<time.h>
#include<math.h>

struct cadastro
{
    char nome;
    int cpf;
    int idade;
    int numeroDependentes;
    int contPrevidenciaria;
    int totalRend;
};

void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}


void cadastroSimples(void)
{
    char nome[50], contPrev[12], totalRend[12], CPF[15], base, IRPF = 0;
    //float Base_IRPF, IRPF = 0;
    int n, d, i;
    //prev = ;
        printf("\n Nome: ");
        gets (nome);
        scanf("%c", &nome);
            printf("\n CPF: ");
            gets (CPF);
            scanf("%d", &CPF);
                printf("\n Contr. Previd.: R$");
                gets (contPrev);
                scanf("%d", &contPrev);
                    printf("\n Total Rend.: R$");
                    gets (totalRend);
                    scanf("%d", &totalRend);
                    base = totalRend-contPrev;
                    base = base * 0.95;
                    if(base<=12000)	printf("\nIsento de Imposto de Renda");
                    if(base>=12000 && base<=24000) IRPF = base * 0.15;
                    if(base>=24000) IRPF = base * 0.275;
                    printf("\nSalario Liquido: %.2f", totalRend - IRPF);
                    printf("\n\n\n\n\n");
//                    return 0;


//    system("cls");
}

void cadastroCompleto(void)
{
    char nome[50], contPrev[12], totalRend[12], CPF[15], idade[2], numDepend[2];
        printf("\n Nome: ");
        gets (nome);
        scanf("%c", &nome);
            printf("\n CPF: ");
            gets (CPF);
            scanf("%d", &CPF);
                printf("\n Idade: ");
                gets (idade);
                scanf("%d", &idade);
                    printf("\n Num. Dependentes: ");
                    gets (numDepend);
                    scanf("%d", &numDepend);
                        printf("\n Contr. Previd.: R$");
                        gets (contPrev);
                        scanf("%d", &contPrev);
                            printf("\n Total Rend.: R$");
                            gets (totalRend);
                            scanf("%d", &totalRend);
//    system("cls");
}

/******************* função principal (main) *********************/

int main(void)
{
    while(1)
    {
        int tipo;
        printf("\n  ******************************************** ");
        printf("\n  *                                          * ");
        printf("\n  *  SISTEMA DE DECLARACAO IMPOSTO DE RENDA  * ");
        printf("\n  *                                          * ");
        printf("\n  ******************************************** ");

        printf("\n\n        ***  OPCOES CADASTRAMENTO ***    ");
        printf("\n  -------------------------------------------");
        printf("\n         ( 1 ) DECLARACAO SIMPLIFICADA");
        printf("\n         ( 2 ) DECLARACAO COMPLETA");
        printf("\n       --> ");
        scanf("%d", &tipo);

        switch(tipo)
        {
            case 1:
              {
                    system("cls");
                    printf("\n *** DECLARACAO SIMPLIFICADA ***");
                    cadastroSimples();
                }break;
            case 2:
                {
                    system("cls");
                    printf("\n *** DECLARACAO COMPLETA ***");
                    cadastroCompleto();
                }break;

            default:
                system("cls");

        }


    //delay(1000);
    }





    //return 0;
}
