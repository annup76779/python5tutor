#include<stdio.h>
#include<math.h>

int main(){
    int p, i, multi;
    printf("Please enter any positive number, which will the amount: "); scanf("%d", &p);
    for (i = 0, multi=1; i< 12; i++){
        if (multi > p){
            multi /=2;
            break;
        }
        multi = (int)pow(2, i);
    }
    i=0;
    printf("Prices of the products you can buy: ");
    while(p>0){
        if (p>=multi){
            printf("%d ", multi);
            i += p/multi;
            p%= multi;
        }
        multi /=2;
    }
    printf("\n%d is the min product count\n", i);
}