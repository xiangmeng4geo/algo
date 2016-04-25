/**
 * 选择排序node.js实现
 */

/**
 * 选择排序算法实现
 * @param array 数组
 * @param compareFn 比较函数
 */
exports.sort = function (array, compareFn) {
    function exch(array, i, j) {
        var temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }
    //从第一个元素开始
    for (var i = 0; i < array.length - 1; i++) {
        var min = array[i];
        var minIndex = i;
        //比较下个元素到最后一个元素,找到最小值
        for (var j = i + 1; j < array.length; j++) {
            if(compareFn(min ,array[j])){
                min = array[j];
                minIndex = j;
            }
        }
        exch(array,i,minIndex);
    }

}