import java.io.*;
import java.util.*;

/**
 * This is a solution to the commuting engineer problem.
 */
public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        // Parse the input file.
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        Set<Integer> set = new HashSet<Integer>();
        Map<Integer, Point> map = new HashMap<Integer, Point>();

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() > 0) {
                // We don't need the addresses.
                int id = Integer.parseInt(line.split("\\|")[0].trim());
                String[] coordinates = line.split("\\(")[1].split("\\)")[0].split(",");

                double lat = Double.parseDouble(coordinates[0]);
                double lon = Double.parseDouble(coordinates[1]);

                Point p = new Point(lat, lon);
                set.add(id);
                map.put(id, p);
            }
        }

        // Find the smallest (best) distance by brute force checking each route.
        Result result = new Result(set.size());
        findBestRoute(set, map, 1, result);

        // Print the best route.
        for (int i = 0; i <= result._index; i++) {
            System.out.println(result._bestRoute[i]);
        }
    }

    public static void findBestRoute(Set<Integer> set, Map<Integer, Point> map, int startingPointID, Result result)
    {
        // Need to make my own stack implementation.
        ArrayStack prefix = new ArrayStack(set.size());
        set.remove(startingPointID);
        prefix.push(startingPointID);

        findBestRoute(set, map, result, prefix);
        set.add(startingPointID);
    }

    private static void findBestRoute(Set<Integer> set, Map<Integer, Point> map, Result result, ArrayStack prefix)
    {
        if (prefix.size() == set.size()+1) {
            double distance = computeDistance(prefix, map);

            if (distance < result._bestDistance) {
                // Copy the best distance.
                result._bestDistance = distance;

                // Copy the best route.
                result._index = prefix._index;
                for (int i = 0; i <= prefix._index; i++) {
                    result._bestRoute[i] = prefix._array[i];
                }
            }

            return;
        }

        for (Integer i : set) {
            if (!prefix.contains(i)) {
                prefix.push(i);
                findBestRoute(set, map, result, prefix);
                prefix.pop();
            }
        }
    }

    /**
     * Compute the distance for a given route (list of points).
     */
    private static double computeDistance(ArrayStack route, Map<Integer, Point> map)
    {
        double distance = 0.0;

        for (int i = 1; i <= route._index; i++) {
            Point p1 = map.get(route._array[i-1]);
            Point p2 = map.get(route._array[i]);
            distance += p1.distanceTo(p2);
        }

        return distance;
    }
    
    private static class Result
    {
        private double _bestDistance = Double.POSITIVE_INFINITY;
        int[] _bestRoute;
        int _index = 0;

        public Result(int capacity)
        {
            _bestRoute = new int[capacity];
        }
    }
    
    /**
     * Helper class that represents a point, i.e. the location of a startup.
     */
    private static class Point
    {
        private final double _latitude;
        private final double _longitude;

        public Point(double latitude, double longitude)
        {
            _latitude = latitude;
            _longitude = longitude;
        }

        /**
         * Returns a distance metric.
         */
        public double distanceTo(Point p)
        {
            final double R = 6371;
            double diffLatitude = (p._latitude-_latitude) * Math.PI/180;
            double diffLongitude = (p._longitude-_longitude) * Math.PI/180;
            double lat1 = _latitude * Math.PI/180;
            double lat2 = p._latitude * Math.PI/180;
            double a = Math.sin(diffLatitude/2) * Math.sin(diffLatitude/2) +
                       Math.sin(diffLongitude/2) * Math.sin(diffLongitude/2) *
                       Math.cos(lat1) * Math.cos(lat2);
            double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
            return  R * c;
        }
    }

    private static class ArrayStack
    {
        private int[] _array;
        private int _index = -1;

        public ArrayStack(int capacity)
        {
            _array = new int[capacity];
        }

        public void push(int i)
        {
            _index++;
            _array[_index] = i;
        }

        public int head()
        {
            return _array[_index];
        }

        public int pop()
        {
            int result = head();
            _index--;
            return result;
        }

        public int size()
        {
            return _index+1;
        }

        public boolean contains(int number)
        {
            for (int i = 0; i <= _index; i++) {
                if (_array[i] == number) {
                    return true;
                }
            }

            return false;
        }
    }
}
