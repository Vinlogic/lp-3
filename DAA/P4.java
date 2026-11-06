import java.util.Scanner;

public class P4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid number of items");
            sc.close();
            return;
        }

        int[] weight = new int[n];
        int[] value = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter weight and value: ");
            weight[i] = sc.nextInt();
            value[i] = sc.nextInt();

            if (weight[i] <= 0 || value[i] < 0) {
                System.out.println("Invalid input");
                sc.close();
                return;
            }
        }

        System.out.print("Enter knapsack capacity: ");
        int W = sc.nextInt();

        if (W < 0) {
            System.out.println("Invalid capacity");
            sc.close();
            return;
        }

        // Create DP table
        long[][] dp = new long[n + 1][W + 1];

        // Fill DP table
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= W; w++) {
                if (weight[i - 1] <= w) {
                    long include = value[i - 1]
                            + dp[i - 1][w - weight[i - 1]];

                    long exclude = dp[i - 1][w];

                    dp[i][w] = Math.max(include, exclude);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        System.out.println("Maximum value: " + dp[n][W]);
        sc.close();
    }
}

/*
SAMPLE INPUT:
3
10 60
20 100
30 120
50

SAMPLE OUTPUT:
Maximum value: 220

RUN:
javac P4.java
java P4
*/
