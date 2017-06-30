import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class LowestCommonAncestor
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        // Hard-coded tree.
        Node n30 = new Node(30);
        Node n8  = new Node(8);
        Node n52 = new Node(52);
        Node n3  = new Node(3);
        Node n20 = new Node(20);
        Node n10 = new Node(10);
        Node n29 = new Node(29);

        n30._left = n8;
        n30._right = n52;
        n8._left = n3;
        n8._right = n20;
        n20._left = n10;
        n20._right = n29;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() == 0) {
                continue;
            }

            String[] lineArray = line.split(" ");

            int a = Integer.parseInt(lineArray[0]);
            int b = Integer.parseInt(lineArray[1]);

            System.out.println(findLowestCommonAncestor(n30, a, b));
        }

        in.close();
    }

    private static int findLowestCommonAncestor(Node n, int a, int b)
    {
        int lower = Math.min(a, b);
        int higher = Math.max(a, b);

        int value = n.getValue();

        // We have found one of the nodes. The other is below, so we're done.
        if (lower == value) {
            return value;
        }
        if (higher == value) {
            return value;
        }

        // The nodes are to the left and right, so we're done.
        if (lower < value && higher > value) {
            return value;
        }

        if (lower < value && higher < value) {
            if (n.getLeft() != null) {
                return findLowestCommonAncestor(n.getLeft(), a, b);
            } else {
                return value;
            }
        }

        assert(lower > value && higher > value);

        if (n.getRight() != null) {
            return findLowestCommonAncestor(n.getRight(), a, b);
        } else {
            return value;
        }
    }

    private static class Node
    {
        private int _value;

        private Node _left = null;
        private Node _right = null;

        public Node(int value)
        {
            _value = value;
        }

        public int getValue()
        {
            return _value;
        }

        public Node getLeft()
        {
            return _left;
        }

        public Node getRight()
        {
            return _right;
        }
    }
}
