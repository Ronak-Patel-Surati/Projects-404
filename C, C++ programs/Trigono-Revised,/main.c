
#include<stdio.h>
#include<math.h>
void main()
{
    int a,o,h,sin,cos,tan,sec,cosec,cot;
    
    printf("\n\nEnter the base of triangle : ");
    scanf("%d",a);
    
    printf("\n\nEnter the opposite of trinagle : ");
    scanf("%d",o);
    
    printf("\n\nEnter the hypotenuse of triangle : ");
    scanf("%d",h);
    
    sin=(o,h);
    cos=(a,h);
    tan=(o,a);
    sec=(h,a);      
    cosec=(h,o);
    cot=(a,o);
    
    printf("\nsin of the Triangle =%d",sin);
    printf("\ncos of the Triangle =%d",cos);
    printf("\ntan of the Triangle =%d",tan);
    printf("\nsec of the Triangle =%%d",sec);
    printf("\ncosec of the Triangle =%d",cosec);
    printf("\ncot of the Triangle =%d",cot);    
    
   return 0;
}
