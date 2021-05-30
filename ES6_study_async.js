"use strict";
import {p,randomWaiReturnerWithIn3SecAsync} from './ES6_study_helper.js';

const main = async () => {
    try {
        p(await randomWaiReturnerWithIn3SecAsync(100));
        p(await randomWaiReturnerWithIn3SecAsync(200));
        p(await randomWaiReturnerWithIn3SecAsync(300));
    } catch (error) {
        console.error(error);
    } finally {
        p('-- Async function Done --');
    }
};

p('-- Start --');
main();
p('-- Completed --');
