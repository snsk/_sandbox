'''
https://www.jabba.cloud/20161020172918/

DPのアプローチ
トップダウン：メモ化再帰、メモ化
ボトムアップ：分割統治法、漸化式ループ
'''

'''
漸化式とは、各項がそれ以前の項の関数として定まるという意味で数列を再帰的に定める等式である。
線形漸化式の例：
フィボナッチ数列は線形漸化式
Fn = Fn-1 + Fn-2 に、初期値 F0=0, F1=1 を与えて得られる
'''
import sys
import time
#pythonの再帰回数の制限を解除する
sys.setrecursionlimit(2000)

#単純再帰の例
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)

#メモ化再帰の例
def fib2(n):
    m = [0]*(n+1) #フィボナッチ計算の外側でメモ用の配列を確保

    def _fib(n):
        if n == 0:  
            return 0
        if n == 1:
            return 1
        if m[n] != 0: #メモにすでに値があれば、（０でなければ）
            return m[n] #その値を返却＝計算しない
        #上記いずれでもなければ計算してメモに格納
        m[n] = _fib(n - 1) + _fib(n - 2)
        return m[n]
    
    return _fib(n) #内側の関数を呼ぶ

n = 40

start = time.time()
print(fib1(n))
stop = time.time()
print("fib1 elapsed: {}".format(stop - start))

start = time.time()
print(fib2(n))
stop = time.time()
print("fib2 elapsed: {}".format(stop - start))
