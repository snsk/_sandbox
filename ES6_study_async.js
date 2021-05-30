"use strict";
import {p,staticWaiReturnerWith2Sec, staticWaiReturnerWith2SecAsync} from './ES6_study_helper.js';

const main = async () => {
    await Promise.all([
        p(staticWaiReturnerWith2Sec(100)),
        p(staticWaiReturnerWith2Sec(200)),
        p(staticWaiReturnerWith2Sec(300))
    ]);
};  

main();