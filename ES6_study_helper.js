"use strict";

//helper
export const p = (s) => console.log(s);
export const sleep = (time) =>{
    const d1 = new Date();
    while (true) {
        const d2 = new Date();
        if (d2 - d1 > time) {
            return;
        }
    }
}
//3秒以内のランダムな秒数でにID付きの文字列が返ってくる
export const randomWaiReturnerWithIn3Sec = (id) => { 
    let msecVal = Math.random()*3000;
    sleep(msecVal);
    return 'id:'+id+' wait:'+msecVal;
}
