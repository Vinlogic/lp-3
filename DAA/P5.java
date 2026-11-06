
import java.util.Scanner;

public class P5 {

    static int n;
    static int[][] board;

    // Check whether queen can be placed
    static boolean isSafe(int row, int col) {

        // Check column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1;
             i >= 0 && j >= 0; i--, j--) {

            if (board[i][j] == 1)
                return false;
        }

        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1;
             i >= 0 && j < n; i--, j++) {

            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Solve using backtracking
    static boolean solve(int row) {

        if (row == n)
            return true;

        for (int col = 0; col < n; col++) {

            if (isSafe(row, col)) {

                board[row][col] = 1;

                if (solve(row + 1))
                    return true;

                // Backtracking
                board[row][col] = 0;
            }
        }

        return false;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter value of N: ");
        n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid N");
            sc.close();
            return;
        }

        board = new int[n][n];

        System.out.print("Enter first queen column (1 to " + n + "): ");
        int col = sc.nextInt();

        if (col < 1 || col > n) {
            System.out.println("Invalid column");
            sc.close();
            return;
        }

        // Place first queen
        board[0][col - 1] = 1;

        if (solve(1)) {

            System.out.println("N-Queens Matrix:");

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(board[i][j] + " ");
                }
                System.out.println();
            }

        } else {
            System.out.println("No solution exists");
        }

        sc.close();
    }
}

/*
SAMPLE INPUT:
4
3

SAMPLE OUTPUT:
N-Queens Matrix:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

NOTE:
1 represents a queen.
0 represents an empty position.
The first queen is placed in the specified column.
*/
