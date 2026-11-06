import java.util.PriorityQueue;
import java.util.Scanner;

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

    static void printCodes(Node root, String code) {
        if (root == null)
            return;

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

        PriorityQueue<Node> queue =
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

            queue.add(new Node(ch, freq));
        }

        while (queue.size() > 1) {
            Node left = queue.poll();
            Node right = queue.poll();

            Node parent = new Node('-', left.freq + right.freq);
            parent.left = left;
            parent.right = right;

            queue.add(parent);
        }

        System.out.println("\nHuffman Codes:");
        printCodes(queue.poll(), "");

        sc.close();
    }
}

/*
SAMPLE INPUT:
4
A 5
B 9
C 12
D 13

SAMPLE OUTPUT:
Huffman Codes:
A : 00
B : 01
C : 10
D : 11

NOTE:
Huffman codes can differ when frequencies tie, but the code lengths
and total encoding cost remain optimal.

Time complexity : O(n log n)
Space complexity: O(n)

RUN:
javac P2.java
java P2/

*/
