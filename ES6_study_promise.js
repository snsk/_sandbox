"use strict";

const sleep3sec = (id) =>{
    setTimeout(() => {
        console.log(id + ' done')
    }, 3000);
}

const task1 = new Promise((resolve, reject) =>{
    sleep3sec(1);
    resolve();
});
const task2 = new Promise((resolve, reject) =>{
    sleep3sec(2);
    resolve();
});
const task3 = new Promise((resolve, reject) =>{
    sleep3sec(3);
    resolve();
});
const task4 = new Promise((resolve, reject) =>{
    sleep3sec(4);
    resolve();
});
const task5 = new Promise((resolve, reject) =>{
    sleep3sec(5);
    resolve();
});

Promise.all([ 
    task1,
    task2,
    task3,
    task4,
    task5
]).then()
