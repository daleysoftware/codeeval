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

        Set<Point> set = new HashSet<Point>();
        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() > 0) {
                // We only need the IDs and the GPS coordinates, not the addresses.
                int id = Integer.parseInt(line.split("\\|")[0].trim());
                String[] coordinates = line.split("\\(")[1].split("\\)")[0].split(",");

                double lat = Double.parseDouble(coordinates[0]);
                double lon = Double.parseDouble(coordinates[1]);

                Point p = new Point(id, lat, lon);
                set.add(p);
            }
        }

        // Find all valid permutations of routes.
        List<List<Point>> permuted = permute(set, 1);

        // Find the smallest (best) distance by brute force checking each route.
        List<Point> bestRoute = null;
        double bestDistance = Double.POSITIVE_INFINITY;

        for (List<Point> route : permuted) {
            double distance = computeDistance(route);

            if (distance < bestDistance) {
                bestRoute = route;
                bestDistance = distance;
            }
        }

        // Print the best route.
        if (bestRoute != null) {
            printRoute(bestRoute);
        }
    }

    private static void printRoute(List<Point> route)
    {
        for (Point p : route) {
            System.out.println(p._id);
        }
    }

    /**
     * Helper class that represents a point, i.e. the location of a startup.
     */
    public static class Point implements Comparable<Point>
    {
        private final int _id;
        private final double _lat;
        private final double _lon;

        public Point(int id, double lat, double lon)
        {
            _id = id;
            _lat = lat;
            _lon = lon;
        }

        /**
         * Returns a distance metric.
         *
         * References:
         *   http://andrew.hedges.name/experiments/haversine/
         *   http://www.movable-type.co.uk/scripts/latlong.html
         */
        public double distanceTo(Point p)
        {
            final double R = 6371;

            double dLat = (p._lat-_lat) * Math.PI/180;
            double dLon = (p._lon-_lon) * Math.PI/180;

            double lat1 = _lat * Math.PI/180;
            double lat2 = p._lat * Math.PI/180;

            double a = Math.sin(dLat/2) * Math.sin(dLat/2) +
                    Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2);

            double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

            return  R * c;
        }

        @Override
        public int compareTo(Point p)
        {
            // We assume the ID is a unique identifier, and do not strictly check the x and y coordinates.
            return p._id == _id ? 0 : 1;
        }

        @Override
        public int hashCode()
        {
            // Ditto here.
            return _id;
        }
    }

    /**
     * Get all permutations of a given set of points.
     *
     * Caveats:
     *  - We only visit a point once.
     *  - We must visit all the points.
     *  - We must start at the provided starting point.
     */
    public static List<List<Point>> permute(Set<Point> set, int startingPointID)
    {
        Stack<Point> prefix = new Stack<Point>();
        Point startingPoint = null;

        for (Point p : set) {
            if (p._id == startingPointID) {
                startingPoint = p;
                break;
            }
        }

        set.remove(startingPoint);
        prefix.add(startingPoint);

        LinkedList<List<Point>> result = new LinkedList<List<Point>>();
        permute(set, result, prefix);

        set.add(startingPoint);

        return result;
    }

    private static void permute(Set<Point> set, List<List<Point>> result, Stack<Point> prefix)
    {
        if (prefix.size() == set.size()+1) {
            List<Point> pointList = new LinkedList<Point>();
            pointList.addAll(prefix);
            result.add(pointList);
            return;
        }

        for (Point p : set) {
            if (!prefix.contains(p)) {
                prefix.add(p);
                permute(set, result, prefix);
                prefix.pop();
            }
        }
    }

    /**
     * Compute the distance for a given route (list of points).
     */
    private static double computeDistance(List<Point> route)
    {
        double distance = 0.0;

        for (int i = 1; i < route.size(); i++) {
            Point p1 = route.get(i-1);
            Point p2 = route.get(i);

            distance += p1.distanceTo(p2);
        }

        return distance;
    }
}
