import java.io.*;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        Node root = new Node(Integer.parseInt(in.readLine().trim()));
        Node[] previous = new Node[1];
        previous[0] = root;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            String[] stringArray = line.split(" ");
            Node[] current = new Node[stringArray.length];

            for (int i = 0; i < current.length; i++) {
                current[i] = new Node(Integer.parseInt(stringArray[i]));
            }

            for (int i = 0; i < previous.length; i++) {
                previous[i]._left = current[i];
                previous[i]._right = current[i+1];
            }

            previous = current;
        }

        System.out.println(root.getMaxValuesSumForPathToLeaf());
        in.close();
    }

    private static class Node
    {
        private Node _left;
        private Node _right;

        private boolean _sumComputed = false;
        private int _cachedSum = 0;

        private final int _value;

        public Node(int value)
        {
            _value = value;
        }

        public int getValue()
        {
            return _value;
        }

        public boolean leftExists()
        {
            return getLeft() != null;
        }

        public boolean rightExists()
        {
            return getRight() != null;
        }

        public Node getLeft()
        {
            return _left;
        }

        public Node getRight()
        {
            return _right;
        }

        public int getMaxValuesSumForPathToLeaf()
        {
            if (_sumComputed) {
                return _cachedSum;
            }

            int left = leftExists() ? getLeft().getMaxValuesSumForPathToLeaf() : 0;
            int right = rightExists() ? getRight().getMaxValuesSumForPathToLeaf() : 0;

            int result = Math.max(left + getValue(), right + getValue());

            _sumComputed = true;
            _cachedSum = result;

            return result;
        }
    }
}
