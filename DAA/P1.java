import java.util.Scanner;

public class P1 {

    // Non-recursive method
    static void iterative(int n) {
        long a = 0, b = 1, c;

        System.out.print("Non-Recursive: ");

        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            c = a + b;
            a = b;
            b = c;
        }
        System.out.println();
    }

    // Recursive method
    static long fib(int n) {
        if (n <= 1)
            return n;

        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of terms (0 to 30): ");
        int n = sc.nextInt();

        if (n < 0 || n > 30) {
            System.out.println("Enter a value between 0 and 30");
            sc.close();
            return;
        }

        iterative(n);

        System.out.print("Recursive: ");
        for (int i = 0; i < n; i++) {
            System.out.print(fib(i) + " ");
        }

        System.out.println();

        System.out.println("Iterative Time: O(n), Space: O(1)");
        System.out.println("Recursive Time: O(2^n), Space: O(n)");

        sc.close();
    }
}

/*
SAMPLE INPUT:
5

SAMPLE OUTPUT:
Non-Recursive: 0 1 1 2 3
Recursive: 0 1 1 2 3
Iterative Time: O(n), Space: O(1)
Recursive Time: O(2^n), Space: O(n)

RUN:
javac P1.java
java P1
*/
