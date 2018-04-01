package org.algo.sort;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class SortTest {
    float[] random_arr;
    float[] arr;
    long startTime;
    private String name;
    private boolean isPrint = true;

    public SortTest() {
        int ARR_LENGTH = 5;
        this.random_arr = new float[ARR_LENGTH];
        for (int i = 0; i < this.random_arr.length; i++) {
            this.random_arr[i] = (float) Math.random() * 100;
        }
        this.arr = new float[ARR_LENGTH];
        System.arraycopy(this.random_arr, 0, this.arr, 0, this.random_arr.length);
    }

    private void arrPrint(float[] arr) {
        if (!this.isPrint) {
            return;
        }
        StringBuilder s = new StringBuilder();
        for (float anArr : arr) {
            s.append(anArr).append(",");
        }
        System.out.println(s);
    }

    @Before
    public void setUp() throws Exception {
        System.arraycopy(this.random_arr, 0, this.arr, 0, this.random_arr.length);
        arrPrint(this.arr);
        this.startTime = System.currentTimeMillis();
    }

    @Test
    public void testBubbleSort() {
        this.name = "bubble sort";
        this.arr = SortAlgo.bubbleSort(this.arr);
    }

    @Test
    public void testSelectSort() {
        this.name = "select sort";
        this.arr = SortAlgo.selectSort(this.arr);
    }

    @After
    public void tearDown() {
        long endTime = System.currentTimeMillis();
        arrPrint(this.arr);
        System.out.println(this.name + " : " + (float) (endTime - startTime) / 1000 + " s");
        for (int i = 0; i < this.arr.length - 1; i++) {
            assertTrue(this.arr[i] <= this.arr[i + 1]);
        }
    }
}