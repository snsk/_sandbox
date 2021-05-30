"use strict";
import {p, sleep, randomWaiReturnerWithIn3Sec} from './ES6_study_helper.js';

/*
const promiseTest = new Promise((resolve, reject)=>{
    p(randomWaiReturnerWithIn3Sec(1));
    resolve();
}).then(()=>{ 
    p(randomWaiReturnerWithIn3Sec(2));
}).then(()=>{
    p(randomWaiReturnerWithIn3Sec(3));
}).catch(()=>{
    console.log("error")
}).finally(()=>{
    console.log("complete")
})
*/

const p1 = new Promise((resolve, reject) =>{
    resolve(randomWaiReturnerWithIn3Sec(10));
});
const p2 = new Promise((resolve, reject) =>{
    resolve(randomWaiReturnerWithIn3Sec(11));
});
const p3 = new Promise((resolve, reject) =>{
    resolve(randomWaiReturnerWithIn3Sec(12));
});

Promise.all([ 
    p1,
    p2,
    p3
]).then((result)=>{
    console.log(result);
});

