#include <stdio.h>
struct Person
{
char name[50];
int age;
float salary;
};
int main()
{
struct Person person = {"John Doe", 30, 50000.0};
printf ("Name: %s\n", person.name);
printf ("Age: %d\n", person.age);
printf ("Salary: %.2f\n", person.salary);
return 0;
}
