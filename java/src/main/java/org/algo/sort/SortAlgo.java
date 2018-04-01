package org.algo.sort;

class SortAlgo {
    static float[] bubbleSort(float[] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = arr.length - 1; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    float tmp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = tmp;
                }
            }
        }
        return arr;
    }

    static float[] selectSort(float[] arr) {
        boolean flag;
        for (int i = 0; i < arr.length - 1; i++) {
            flag = false;
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[minIndex] > arr[j]) {
                    minIndex = j;
                    flag = true;
                }
            }
            // 发生过交换
            if (flag){
                float min = arr[minIndex];
                arr[minIndex] = arr[i];
                arr[i] = min;
            }
            else {
                break;
            }
        }
        return arr;
    }
}
