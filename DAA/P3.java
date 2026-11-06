import java.util.*;

public class P3 {

    static class Item {
        int weight, value;
        double ratio;

        Item(int weight, int value) {
            this.weight = weight;
            this.value = value;
            ratio = (double) value / weight;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid number of items");
            sc.close();
            return;
        }

        Item[] items = new Item[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter weight and value: ");
            int weight = sc.nextInt();
            int value = sc.nextInt();

            if (weight <= 0 || value < 0) {
                System.out.println("Invalid input");
                sc.close();
                return;
            }

            items[i] = new Item(weight, value);
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        if (capacity < 0) {
            System.out.println("Invalid capacity");
            sc.close();
            return;
        }

        // Sort items by value/weight ratio
        Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));

        double totalValue = 0;

        // Fill the knapsack
        for (Item item : items) {
            if (capacity == 0)
                break;

            if (item.weight <= capacity) {
                totalValue += item.value;
                capacity -= item.weight;
            } else {
                totalValue += item.ratio * capacity;
                capacity = 0;
            }
        }

        System.out.println("Maximum value: " + totalValue);
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
Maximum value: 240.0

RUN:
javac P3.java
java P3
*/
