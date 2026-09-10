//Design A Dynamic Array(Resizable Array)
#include<iostream>
using namespace std;


class DynamicArray{
private:
    int* arr;
    int capacity;
    int length;

    void resize()
    {
        int newCapcity = capacity * 2;
        int* newArr = new int[newCapcity];
        for(int i = 0; i<length; i++){
            newArr[i] = arr[i]; //Copy the values
        }

        //free the memory from old arr
        delete[] arr;

        arr = newArr;
        capacity = newCapcity;
    }

public:
    //Constructor
    DynamicArray(int initCapacity = 2):capacity(initCapacity), arr(new int[initCapacity]), length(0){}
    ~DynamicArray(){delete[] arr;}

    //Element at idx i
    int get(int i){
        return arr[i];
    }

    //Sets element at idx i with n
    void set(int i, int n){
        arr[i] = n;
    }

    //will push the element n to the end of the array
    void pushback(int n){
        //check if the length is at capcity 
        if(length == capacity) resize();
        arr[length++] = n;
    }

    int popback(){
        //Decrements the length first and returns the
        //array at that length
        return arr[--length];
    }

    int getSize() {return length;}
    int getCapacity() {return capacity;}
};