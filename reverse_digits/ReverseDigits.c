#include<stdlib.h>
#include<stdio.h>
int reversDigits(int x)
{
    int rev_num = 0;
    int num = x;
    if (x < 0) num = -x;
    while (num > 0)
    {
        rev_num = rev_num * 10 + num % 10;
        num = num / 10;
    }
    if (x < 0) return -rev_num;
    else return rev_num;
}
 
int main()
{
    int num = 4562;
    printf("Reverse of no. is %d", reversDigits(num));
 
    getchar();
    return 0;
}
