
#include <stdio.h>
int main()
{   int a,b, add, sub, mul, divi;
        printf("Enter value of a=" );
        scanf("%d", &a);
        printf("\nEnter value of b=");
        scanf("%d" , &b);
    add=a+b;
        printf("\nAddition=%d",add);
    sub=a-b;
        printf("\nSubtraction=%d",sub);
    mul=a*b;
        printf("\nMultiplication=%d",mul);
    divi=a/b;
        printf("\ndivision=%d",divi);
    return 0;
}
