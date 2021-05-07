#include <stdio.h>
#include <stdlib.h>

/*
反復と再帰のフィボナッチ計算結果の比較。
コマンドライン引数に与えられた非負整数までのフィボナッチ数。2つ与えられたらN1～N2までを1行ごとに出力。
1行にはフィボナッチ数と、関数が呼ばれた回数を表示。反復と再帰の結果が一致していたら . を最後に書く
*/

int count = 0;
long int fib(int n){
    long int i, n1=0, n2=1;
    for(i=0; i<n; ++i){
        long int tmp = n1; n1 = n2; n2 += tmp;
    }
    return n1;
}
long int fib_r(int n){
    count++;
    if( n<=1 ) return n;
    return fib_r(n-1)+fib_r(n-2);
}

//fib(10) = 55[177] .
int main(int argc, char *argv[]){
    if(argc==1) return 0;
    int i, num1, num2;
    long int fib_num, fibr_num;
    if(argc==2){
        num1=atoi(argv[1]);
        num2=num1;
    }
    if(argc==3){
        num1=atoi(argv[1]);
        num2=atoi(argv[2]);
    }
    for(i=num1; i <= num2; i++){
        printf("fib(%d) = ", i);
        fibr_num = fib_r(i);
        fib_num = fib(i);
        printf("%ld", fibr_num);
        printf("[%d]", count);
        if(fib_num == fibr_num){
            printf(" .\n");
        }else{
            printf(" %ld\n", fib_num);
        }
        count = 0;
    }
    return 0;
}








