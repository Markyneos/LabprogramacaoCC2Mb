#include <stdio.h>

int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    int diferenca = b - a;

    for (int i = 0; i <= diferenca; i++)
    {
        if (1 <= a && a <= 9)
        {
            switch (a) 
            {
                case 1: printf("one\n"); break;
                case 2: printf("two\n"); break;
                case 3: printf("three\n"); break;
                case 4: printf("four\n"); break;
                case 5: printf("five\n"); break;
                case 6: printf("six\n"); break;
                case 7: printf("seven\n"); break;
                case 8: printf("eight\n"); break;
                case 9: printf("nine\n"); break;
            }
        }
        else if (a > 9)
        {
            if (a % 2 == 0)
            {
                printf("even\n");
            }
            else
            {
                printf("odd\n");
            }
        }
        a++;
    }

    return 0;
}