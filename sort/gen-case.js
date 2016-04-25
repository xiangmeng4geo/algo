#!/usr/bin/env node
var fs = require('fs');

//生成的随机数个数
var caseKeys = [100,10000,100000,10000000];
var caseObj = {};

for (var i = 0; i < caseKeys.length; i++) {
    //按照给定随机数长度,生成指定个数的随机数
    var length = caseKeys[i];
    var j = 0;
    caseObj[length + ''] = [];
    while (j < length) {
        caseObj[length + ''].push(Math.random() * 100);
        j++;
    }
}
fs.writeFileSync('./case/sort.json', JSON.stringify(caseObj));
