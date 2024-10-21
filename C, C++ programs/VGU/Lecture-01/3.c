#include <stdio.h>

int main()
{

    float cel, fah;

    printf("Enter Fahrenheit Temperature: ");
    scanf("%f", &fah); 

    cel = (fah - 32) / 1.8;

    printf("Temperature in Degree Celsius: %.2f\n", cel);

    return 0;
}
