
import java.util.Scanner;

public class P1 {

    // Non-recursive method
    static void iterative(int n) {
        int a = 0, b = 1, c;

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
    static int fib(int n) {
        if (n <= 1)
            return n;

        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of terms: ");
        int n = sc.nextInt();

        if (n < 0) {
            System.out.println("Invalid input");
            sc.close();
            return;
        }

        iterative(n);

        System.out.print("Recursive: ");

        for (int i = 0; i < n; i++) {
            System.out.print(fib(i) + " ");
        }

        System.out.println();
        sc.close();
    }
}
