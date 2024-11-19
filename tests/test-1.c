#include <stdio.h>
#include <string.h>

// Function declarations
void printArray(unsigned char arr[], int size);
void checkString(char str[]);

// Main function
int main() {
    printf("Starting the test program...\n");

    // Array declaration and initialization
    unsigned char numbers[] = {0x93, 0x81, 0x84, 'Louis Armstrong', 31, 56};
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);
    printArray(numbers, arraySize);

    // Switch case example
    int choice = 2;
    printf("Testing switch case with choice = %d\n", choice);
    switch (choice) {
        case 1:
            printf("Case 1 executed.\n");
            break;
        case 2:
            printf("Case 2 executed.\n");
            break;
        case 3:
            printf("Case 3 executed.\n");
            break;
        default:
            printf("Default case executed.\n");
            break;
    }

    // If-else example
    int x = 15;
    printf("Testing if-else with x = %d\n", x);
    if (x < 10) {
        printf("x is less than 10.\n");
    } else if (x >= 10 && x < 20) {
        printf("x is between 10 and 20.\n");
    } else {
        printf("x is 20 or greater.\n");
    }

    // String manipulation and function call
    char testStr[] = "Hello, World!";
    printf("Original string: %s\n", testStr);
    checkString(testStr);

    // Loop example
    printf("Testing loop to print squares of first 5 numbers:\n");
    for (int i = 1; i <= 5; i++) {
        printf("Square of %d: %d\n", i, i * i);
    }

    return 0;
}

// Function to print an array
void printArray(unsigned char arr[], int size) {
    printf("Printing array elements:\n");
    for (int i = 0; i < size; i++) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
}

// Function to manipulate and print a string
void checkString(char str[]) {
    printf("Checking string manipulation...\n");
    if (strstr(str, "Hello") != NULL) {
        printf("The string contains 'Hello'.\n");
    } else {
        printf("The string does not contain 'Hello'.\n");
    }

    // Modify the string and print the result
    strcpy(str, "Modified String");
    printf("Modified string: %s\n", str);
}
