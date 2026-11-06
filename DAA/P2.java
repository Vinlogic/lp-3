import java.util.PriorityQueue;
import java.util.Scanner;

public class P2 {

    // Node of the Huffman tree
    static class Node {
        char ch;
        int freq;
        Node left, right;

        Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
        }
    }

    // Walk the tree: left edge = 0, right edge = 1
    static void printCodes(Node root, String code) {
        if (root == null) return;

        // Leaf node -> print its code
        if (root.left == null && root.right == null) {
            System.out.println(root.ch + " : " + (code.isEmpty() ? "0" : code));
            return;
        }

        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of characters: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid input");
            sc.close();
            return;
        }

        // Min-heap ordered by frequency
        PriorityQueue<Node> pq =
            new PriorityQueue<>((a, b) -> Integer.compare(a.freq, b.freq));

        for (int i = 0; i < n; i++) {
            System.out.print("Enter character and frequency: ");
            char ch = sc.next().charAt(0);
            int freq = sc.nextInt();

            if (freq <= 0) {
                System.out.println("Invalid frequency");
                sc.close();
                return;
            }

            pq.add(new Node(ch, freq));
        }

        // Greedy step: repeatedly merge the two smallest-frequency nodes
        while (pq.size() > 1) {
            Node left = pq.poll();
            Node right = pq.poll();

            Node parent = new Node('-', left.freq + right.freq);
            parent.left = left;
            parent.right = right;

            pq.add(parent);
        }

        System.out.println("\nHuffman Codes:");
        printCodes(pq.poll(), "");

        sc.close();
    }
}

/*
SAMPLE INPUT:
Enter number of characters: 6
a 5
b 9
c 12
d 13
e 16
f 45

SAMPLE OUTPUT (bits may differ on ties, code lengths stay the same):
f : 0
c : 100
d : 101
a : 1100
b : 1101
e : 111

Time complexity : O(n log n)
Space complexity: O(n)
*/
