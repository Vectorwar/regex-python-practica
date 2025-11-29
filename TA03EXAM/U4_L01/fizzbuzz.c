/*
 * FizzBuzz Algorithm
 * 
 * Este programa imprime números del 1 al 100, pero:
 * - Para múltiplos de 3, imprime "Fizz"
 * - Para múltiplos de 5, imprime "Buzz"
 * - Para múltiplos de ambos 3 y 5, imprime "FizzBuzz"
 * - Para otros números, imprime el número
 */

#include <stdio.h>

int main() {
    printf("=== Algoritmo FizzBuzz (1-100) ===\n\n");
    
    for (int i = 1; i <= 100; i++) {
        // Verificar si es múltiplo de 3 y 5
        if (i % 3 == 0 && i % 5 == 0) {
            printf("FizzBuzz\n");
        }
        // Verificar si es múltiplo de 3
        else if (i % 3 == 0) {
            printf("Fizz\n");
        }
        // Verificar si es múltiplo de 5
        else if (i % 5 == 0) {
            printf("Buzz\n");
        }
        // Si no es múltiplo de 3 ni de 5
        else {
            printf("%d\n", i);
        }
    }
    
    return 0;
}