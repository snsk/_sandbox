"use strict";
import {p, sleep, randomWaitReturer} from './ES6_study_helper.js';

const promiseTest = new Promise((resolve, reject)=>{
    p(randomWaitReturer(1));
    resolve();
}).then(()=>{
    p(randomWaitReturer(2));
    reject();
}).then(()=>{
    p(randomWaitReturer(3));
}).catch(()=>{
    console.log("error")
}).finally(()=>{
    console.log("complete")
})
