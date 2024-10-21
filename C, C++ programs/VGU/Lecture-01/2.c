#include <stdio.h>

int main()
{
    // Declaration of Character Arrays
    char name[30], address[80], city[20];

    printf("Enter your name:\n");
    scanf("%s", name);

    printf("Enter your address:\n");
    scanf("%s", address);

    printf("Enter your city:\n");
    scanf("%s", city);
    
    // Display the inputs
    printf("Name: %s\n", name);
    printf("Address: %s\n", address);
    printf("City: %s\n", city);

    return 0;
}
