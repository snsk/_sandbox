"use strict";
import {p, sleep, randomWaiReturnerWithIn3Sec} from './ES6_study_helper.js';

const promiseTest = new Promise((resolve, reject)=>{
    p(randomWaiReturnerWithIn3Sec(1));
    resolve();
}).then(()=>{ 
/*上で resolve() を呼んでいるので、このthenが発火する。多くのライブラリでは内部で 
resolve()を呼んであるので、then() で受け止めてから先だけを書けばよい？ってこと？*/
    p(randomWaiReturnerWithIn3Sec(2));
}).then(()=>{
    p(randomWaiReturnerWithIn3Sec(3));
    reject();
}).catch(()=>{
    console.log("error")
}).finally(()=>{
    console.log("complete")
})
