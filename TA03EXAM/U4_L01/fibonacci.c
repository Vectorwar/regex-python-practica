/*
 * Fibonacci Sequence
 * 
 * Este programa calcula y muestra la secuencia de Fibonacci.
 * La secuencia comienza con 0 y 1, y cada número subsecuente
 * es la suma de los dos números anteriores.
 * 
 * Fórmula: F(n) = F(n-1) + F(n-2)
 * donde F(0) = 0 y F(1) = 1
 */

#include <stdio.h>

// Función iterativa para calcular Fibonacci
void fibonacciIterativo(int n) {
    unsigned long long fib1 = 0, fib2 = 1, siguiente;
    
    printf("\nSecuencia de Fibonacci (primeros %d términos):\n", n);
    
    for (int i = 0; i < n; i++) {
        if (i <= 1) {
            siguiente = i;
        } else {
            siguiente = fib1 + fib2;
            fib1 = fib2;
            fib2 = siguiente;
        }
        printf("%d: %llu\n", i, siguiente);
    }
}

// Función recursiva para calcular un término específico de Fibonacci
unsigned long long fibonacciRecursivo(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2);
}

int main() {
    int terminos;
    
    printf("=== Calculadora de Secuencia Fibonacci ===\n");
    printf("¿Cuántos términos deseas calcular? (recomendado: 20-30): ");
    scanf("%d", &terminos);
    
    if (terminos <= 0) {
        printf("Error: El número de términos debe ser positivo.\n");
        return 1;
    }
    
    if (terminos > 93) {
        printf("Advertencia: Para números mayores a 93, puede haber overflow.\n");
    }
    
    // Método iterativo (más eficiente)
    fibonacciIterativo(terminos);
    
    // Ejemplo de método recursivo para un término específico
    printf("\n--- Ejemplo con método recursivo ---\n");
    int n = (terminos < 20) ? terminos - 1 : 19; // Limitamos a 19 para evitar lentitud
    printf("Fibonacci(%d) usando recursión: %llu\n", n, fibonacciRecursivo(n));
    printf("Nota: El método recursivo es menos eficiente para números grandes.\n");
    
    return 0;
}