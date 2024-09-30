#include <stdio.h>

int fatorial(int input);
int arranjo(int input1, int input2);

int main(void)
{
  int input;
  scanf("%d", &input);
  int resultado = fatorial(input);
  int resultado2 = arranjo(input, 3);
  printf("%d\n%d\n", resultado, resultado2);
  return 0;
}
int fatorial(int input)
{
  int resultado = 1;
  for (int i = input; i > 0; i--)
    {
      resultado = resultado * i;
    }
  return resultado;
}
int arranjo(int input1, int input2)
{
  int parte1 = fatorial(input1);
  int parte2 = fatorial(input1 - input2);
  int resultado = parte1 / parte2;
  return resultado;
}


