#include <stdio.h>

int main() {
  int t1 = 1;
  int t2 = 1;
  int nextFib;
  for (int i = 0; i < 10; i++) {
    printf("%d ", t1);
    nextFib = t1 + t2;
    t1 = t2;
    t2 = nextFib;
  }
  printf("\n");
  return 0;
}
