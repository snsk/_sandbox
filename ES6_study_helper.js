"use strict";

//helper
export const p = (s) => console.log(s);

export const sleep = (ms) => {
    var time = new Date().getTime() + ms;
    while (new Date().getTime() < time) {}
}

//3秒以内のランダムな秒数でにID付きの文字列が返ってくる
export const randomWaiReturnerWithIn3Sec = (id) => { 
    let msecVal = Math.random()*3000;
    sleep(msecVal);
    return 'id:'+id+' wait:'+msecVal;
}

export const randomWaiReturnerWithIn3SecAsync = async (id) => { 
    let msecVal = Math.random()*3000;
    sleep(msecVal);
    return 'id:'+id+' wait:'+msecVal;
}

//3s秒後にID付きの文字列が返ってくる
export const staticWaiReturnerWith2Sec = (id) => { 
    sleep(2000);
    return 'id:'+id+' wait: 2000';
}

//3s秒後にID付きの文字列が返ってくる aysnc付き
export const staticWaiReturnerWith2SecAsync = async (id) => { 
    sleep(2000);
    return 'id:'+id+' wait: 2000';
}
