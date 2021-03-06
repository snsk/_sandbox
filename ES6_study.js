"use strict";

import {p, sleep, randomWaiReturnerWithIn3Sec} from './ES6_study_helper.js';

//arrow function
const f1 = (n) => {return n * n};
console.log(f1(2));

//standard object definition(not class )
const obj = {
    member1: "foo",
    member2(n){return n*6} 
};

console.log(obj.member2(4));

//分割代入
const [n, m] = [1, 5];
console.log(n, m)

//スプレッド構文
const aiko = {job:"singer", age:25, nullval:null};
const keiko = {...aiko}; //オブジェクトのコピー時にレストパラメータ構文が使える
console.log(keiko.job); // => singer
let reiko = null;

//optional chaining ?.
//nullかもしれないobjのチェックを簡略化できる   

//p(reiko.job) //=> raise exeption 
p(reiko?.job) //=> undefined 
reiko = {...aiko}
p(reiko?.job)

const double = (n) => n * 2;
p([1, 2, 3].map(double));

//Hi xx ! と書き出す関数を返す関数（高階関数）
const greeter = (target) => () => console.log(`Hi, ${target}!`);
//ので、呼び出し方はこう。greeter("hoge") の時点で文字列の決まった関数が
//返ってるので、”それ”を呼び出す
greeter("hoge")()

//元のがこれ。returnが1文のときはブロックとreturn文を省略できるので↑になる
const base_greeter = (target) => {
    return () => console.log(`Hi, ${target}!`);
}
base_greeter("fuga")()

//カリー化
//もとの関数
const baseSum = (n, m) => n + m;
p(baseSum(1, 2));

//カリー化。
//(2) が渡されて、n + 2 を返す関数が作られて、それに (1) が渡されて、3になる
const curriedSum = (n) => (m) => n + m;
p(curriedSum(1)(2));

//部分適用: カリー化した関数を、「10に何かを足す関数」に変える
//curriedSumを引数1個だけで呼び出して1つ目の関数の値を固定化して、別の関数に仕様を変えてしまう
const addTen = curriedSum(10);
p(addTen(10))


//Promise オブジェクトの自作
const isSucceeded = true;

//resolve, rejectは Promise についてくるメソッド
const promise = new Promise((resolve, reject)=>{
    if(isSucceeded){
        resolve('Success');
    } else{
        reject(new Error('Failure'));
    }
});

promise.then((value)=>{
    console.log('1.', value);
    return 'Success again';
})
.then((value)=>{
    console.log('2.', value);
})
.catch((error)=>{
    console.error('3.', error);
})
.finally(()=>{
    console.log('4.', 'Completed');
});

//node-fetch モジュールを使う
import fetch from 'node-fetch';

fetch('https://api.github.com/users/snsk')
//	.then(res => res.json())
//	.then(json => console.log(json));

//p(randamWaitReturer(1));
//p(randamWaitReturer(2));
