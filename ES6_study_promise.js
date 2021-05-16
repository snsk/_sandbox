"use strict";
import {p, sleep, randomWaiReturnerWithIn3Sec} from './ES6_study_helper.js';

p(randomWaiReturnerWithIn3Sec('A'));
p(randomWaiReturnerWithIn3Sec('B'));
p(randomWaiReturnerWithIn3Sec('C'));
p(randomWaiReturnerWithIn3Sec('D'));

const promiseTest = new Promise((resolve, reject)=>{
    p(randomWaiReturnerWithIn3Sec(1));
    resolve();
}).then(()=>{
    p(randomWaiReturnerWithIn3Sec(2));
}).then(()=>{
    p(randomWaiReturnerWithIn3Sec(3));
    reject();
}).catch(()=>{
    console.log("error")
}).finally(()=>{
    console.log("complete")
})
