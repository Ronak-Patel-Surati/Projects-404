
#include <stdio.h>
void main()
{
    int mark;
        printf("Enter marks of Student= ");
        scanf("%d",&mark);
    if(mark>=0 && mark<=100)
        {
        if(mark>=70)
            printf("Student secure Distinction");
        if(mark>=60 && mark<70)
            printf("Student secure First Class");
        if(mark>=35 && mark<60)
            printf("Student secure Second Class");
        if(mark<35)
            printf("Student is Fail");
        }
        
        else
        {
            printf("Please Enter Mark between 0 to 100");
        }
        return 0;
}

