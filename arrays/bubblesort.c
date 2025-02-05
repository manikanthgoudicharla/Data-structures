#include<stdio.h>

void bubblesort(int size,int array[]){
 int i,j,temp;
 for(i=0;i<size;i++){
     for(j=0;j<size-i-1;j++){
         if(array[j]>array[j+1]){
             temp=array[j];
             array[j]=array[j+1];
             array[j+1]=temp;
         }
         else{
             continue;
         }
     }
 }
}

void printarray(int size,int array[]){
    int i;
      for(i=0;i<size;i++){
        printf("the %d th element of the array is:%d\n",i+1,array[i]);
    }
}

int main(){
    int size;
    printf("Enter the Size of the Array:");
    scanf("%d",&size);
    int array[size],i;
    for(i=0;i<size;i++){
        printf("Enter %d th Element of the Array:",i+1);
        scanf("%d",&array[i]);
    }
    printf("Array Before Bubble sort:\n");
    printarray(size,array);
    bubblesort(size,array);
    printf("Array After Bubble sort:\n");
    printarray(size,array);

    printf("hi");

}
