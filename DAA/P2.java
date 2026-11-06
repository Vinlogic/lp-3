
import java.util.*;

public class P2 {

    static class Node {
        char ch;
        int freq;
        Node left, right;

        Node(char ch, int freq) {
            this.ch = ch;
            this.freq = freq;
        }
    }

    // Print Huffman codes
    static void printCodes(Node root, String code) {

        if (root == null)
            return;

        if (root.left == null && root.right == null) {
            System.out.println(root.ch + " : " +
                    (code.isEmpty() ? "0" : code));
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

        PriorityQueue<Node> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.freq, b.freq)
        );

        // Read characters and frequencies
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

        // Build Huffman tree
        while (pq.size() > 1) {

            Node left = pq.poll();
            Node right = pq.poll();

            Node parent = new Node(
                '\0', left.freq + right.freq
            );

            parent.left = left;
            parent.right = right;

            pq.add(parent);
        }

        // Print final Huffman codes
        System.out.println("\nHuffman Codes:");
        printCodes(pq.poll(), "");

        sc.close();
    }
}

// Input : 
// Enter number of characters: 4
// Enter character and frequency: A 5
// Enter character and frequency: B 9
// Enter character and frequency: C 12
// Enter character and frequency: D 13

// Output : 
// Huffman Codes:
// C : 00
// D : 01
// A : 10
// B : 11
