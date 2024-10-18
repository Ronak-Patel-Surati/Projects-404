
#include<stdio.h>
   int main()
{
    int p,r,n,si,amount; 
                 /*** p means principle amount***/
                 /** r means rate of interest per year**/
                 /**n means number of years**/
                 /** si means simple interset**/
        printf("Enter value of p= ");
        scanf("%d",&p);
        printf("\nEnter value of r= ");
        scanf("%d",&r);
        printf("\nEnter value of n= ");
        scanf("%d",&n);
    
        printf("\nSimple Interest=%d",si=(p*r*n)/100);
        printf("\nTotal amount to pay back is %d",amount=si+p);
    return 0;    
}
