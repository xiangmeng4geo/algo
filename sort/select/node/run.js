var caseObj = require('../../case/sort.json');
var selectSort = require('./select-sort');

var compareFn = function (a, b) {
    return a >= b;
}
for(var caseLength in caseObj){
    console.time(caseLength);
    //selectSort.sort(caseObj[caseLength],compareFn);
    caseObj[caseLength].sort(compareFn);
    console.timeEnd(caseLength)
}