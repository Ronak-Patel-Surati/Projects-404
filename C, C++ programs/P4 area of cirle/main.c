
#include <stdio.h>
float main()
{
  float r,pi,aoc;
  printf("Enter value of Radii = ");
  scanf("%f", &r);

  pi=3.14;
  aoc=pi*r*r;
  printf("\nArea of circle=%f", aoc);
  return 0;
}
