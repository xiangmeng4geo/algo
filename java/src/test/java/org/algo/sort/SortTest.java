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

    public SortTest() {
        int ARR_LENGTH = 10000;
        this.random_arr = new float[ARR_LENGTH];
        for (int i = 0; i < this.random_arr.length; i++) {
            this.random_arr[i] = (float) Math.random() * 100;
        }
        this.arr = new float[ARR_LENGTH];
        System.arraycopy(this.random_arr, 0, this.arr, 0, this.random_arr.length);
    }

    @Before
    public void setUp() throws Exception {
        this.startTime = System.currentTimeMillis();
    }

    @Test
    public void testBubbleSort() {
        this.name = "bubble sort";
        this.arr = SortAlgo.bubbleSort(this.arr);
    }

    @After
    public void tearDown() {
        long endTime = System.currentTimeMillis();
        System.out.println(this.name + " : " + (float) (endTime - startTime) / 1000 + " s");
        for (int i = 0; i < this.arr.length - 1; i++) {
            assertTrue(this.arr[i] <= this.arr[i + 1]);
        }


    }
}