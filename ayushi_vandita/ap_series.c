/*
1 3 7 13 21 31 43 ...
case is to print the series to 100

el = 1
while el < 100{
    print(el)
    el += 2 multiple
}
*/

#include<stdio.h>

void main(){
    int el=1, multiple = 2;

    while (el < 100){
        printf("%d ", el);
        el += multiple;
        multiple += 2;
    }
}