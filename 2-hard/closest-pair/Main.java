import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Set;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));

        Set<Point> set;
        while (true) {
            set = parseSet(in);

            if (set.size() == 0) {
                break;
            }

            double distance = findMinDistanceInSet(set);

            if (distance == Double.POSITIVE_INFINITY) {
                System.out.println("INFINITY");
            } else {
                System.out.println(String.format("%.4f", distance));
            }
        }
    }

    public static Set<Point> parseSet(BufferedReader in)
            throws IOException
    {
        int n = Integer.parseInt(in.readLine());
        HashSet<Point> set = new HashSet<Point>();

        for (int i = 0; i < n; i++) {
            String[] lineArray = in.readLine().split(" ");

            Point p = new Point(
                    Integer.parseInt(lineArray[0]),
                    Integer.parseInt(lineArray[1]));

            set.add(p);
        }

        return set;
    }

    public static double findMinDistanceInSet(Set<Point> set)
    {
        double minDistance = Double.POSITIVE_INFINITY;

        for (Point comparator : set) {
            for (Point p : set) {
                if (comparator.equals(p)) {
                    continue;
                }

                double distance = comparator.distanceTo(p);

                if (distance < 10000.0 && distance < minDistance) {
                    minDistance = distance;
                }
            }
        }

        return minDistance;
    }

    public static class Point
    {
        private final int _x;
        private final int _y;

        public Point(int x, int y)
        {
            _x = x;
            _y = y;
        }

        public double distanceTo(Point p)
        {
            int x = (_x-p._x)*(_x-p._x);
            int y = (_y-p._y)*(_y-p._y);

            return Math.sqrt(x+y);
        }

        public boolean equals(Point p)
        {
            return _x == p._x && _y == p._y;
        }
    }
}
