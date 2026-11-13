import java.util.Scanner;

public class P4 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        int[] weight = new int[n];
        int[] value = new int[n];

        // Input item details
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
        int[][] dp = new int[n + 1][W + 1];

        // Fill DP table
        for (int i = 1; i <= n; i++) {

            for (int j = 0; j <= W; j++) {

                if (weight[i - 1] <= j) {

                    int include = value[i - 1]
                            + dp[i - 1][j - weight[i - 1]];

                    int exclude = dp[i - 1][j];

                    dp[i][j] = Math.max(include, exclude);

                } else {

                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        System.out.println("Maximum value: " + dp[n][W]);

        sc.close();
    }
}

// Input:
// Enter number of items: 3
// Enter weight and value: 10 60
// Enter weight and value: 20 100
// Enter weight and value: 30 120
// Enter knapsack capacity: 50

// Output:
// Maximum value: 220
