#include <iostream>

// Function to check if a number is perfect
bool isPerfect(int num) {
    int sum = 1; // Start with 1 because every number is divisible by 1

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            sum += i;

            // If the divisors are not equal, add the other divisor
            if (i != num / i) {
                sum += num / i;
            }
        }
    }

    // Check if the sum of divisors equals the original number
    return sum == num;
}

// Function to find the first n perfect numbers
void findPerfectNumbers(int n) {
    int count = 0;
    int num = 2; // Start checking from 2

    std::cout << "First " << n << " perfect numbers are:\n";

    while (count < n) {
        if (isPerfect(num)) {
            std::cout << num << " ";
            count++;
        }
        num++;
    }

    std::cout << std::endl;
}

int main() {
    int n;

    std::cout << "Enter the value of n: ";
    std::cin >> n;

    findPerfectNumbers(n);

    return 0;
}
