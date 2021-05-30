"use strict";
import {p,staticWaiReturnerWith2SecAsync} from './ES6_study_helper.js';

const main = async () => {
    try {
        const ret100 = await staticWaiReturnerWith2SecAsync(100);
        const ret110 = await staticWaiReturnerWith2SecAsync(110);
        const ret120 = await staticWaiReturnerWith2SecAsync(120);    
        console.log(ret100);
        console.log(ret110);
        console.log(ret120);
    } catch (error) {
        console.error(error);
    } finally {
        console.log('-- Completed --');
    }
};

main();