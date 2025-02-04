#include <stdio.h>

int main() {
    int arr[3] = {1, 2, 3};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Printing the original array
    printf("Original array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // Reversing the array using in-place swapping
    for (int i = 0, j = size - 1; i < j; i++, j--) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Printing the reversed array
    printf("Reversed array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
