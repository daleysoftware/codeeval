package codeeval.moderate.findsquare;

import java.io.*;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() == 0) {
                continue;
            }

            String[] array = line.split("\\),");
            assert(array.length == 4);
            Point[] points = new Point[4];

            for (int i = 0; i < 4; i++) {
                String pointString = array[i];

                int x = Integer.parseInt(pointString.split(",")[0].split("\\(")[1]);
                int y = Integer.parseInt(pointString.split(",")[1].split("\\)")[0]);

                Point p = new Point(x, y);
                points[i] = p;
            }

            // Step 1. If this is a square, determine how the points are connected. Do
            // this by inferring the arrangement based on the distances to a given point.
            int d1 = points[0].squareDistanceTo(points[1]);
            int d2 = points[0].squareDistanceTo(points[2]);
            int d3 = points[0].squareDistanceTo(points[3]);

            Quadrilateral q;

            if (d1 == d2 && d2 == d3) {
                System.out.println(false);
                continue;
            } else if (d1 == d2) {
                q = new Quadrilateral(points[0], points[1], points[3], points[2]);
            } else if (d2 == d3) {
                q = new Quadrilateral(points[0], points[2], points[1], points[3]);
            } else if (d3 == d1) {
                q = new Quadrilateral(points[0], points[1], points[2], points[3]);
            } else {
                System.out.println(false);
                continue;
            }

            // And finally determine if it indeed a square by checking the remaining
            // lengths and perpendicularity of the line segments.
            System.out.println(q.isSquare());
        }

        in.close();
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

        public int getX()
        {
            return _x;
        }

        public int getY()
        {
            return _y;
        }

        public int squareDistanceTo(Point p)
        {
            int xDiff = getX() - p.getX();
            int yDiff = getY() - p.getY();

            return (xDiff*xDiff) + (yDiff*yDiff);
        }

        @Override
        public String toString()
        {
            return "(" + Integer.toString(getX()) + "," + Integer.toString(getY()) + ")";
        }
    }

    public static class LineSegment
    {
        private final Point _p1;
        private final Point _p2;

        public LineSegment(Point p1, Point p2)
        {
            _p1 = p1;
            _p2 = p2;
        }

        public Vector toVector()
        {
            return new Vector(_p1.getX() - _p2.getX(), _p1.getY() - _p2.getY());
        }

        public boolean isPerpendicularTo(LineSegment ls)
        {
            // Use the dot product to determine if two line segments are perpendicular.
            return toVector().dot(ls.toVector()) == 0;
        }
    }

    public static class Vector
    {
        private final int _x;
        private final int _y;

        public Vector(int x, int y)
        {
            _x = x;
            _y = y;
        }

        public int dot(Vector v)
        {
            return _x * v._x + _y * v._y;
        }
    }

    public static class Quadrilateral
    {
        private Point _p1;
        private Point _p2;
        private Point _p3;
        private Point _p4;

        /**
         * Order matters here. P1 connects to P2, P2 connects to P3, P3 to P4, and of
         * course P4 to P1.
         */
        public Quadrilateral(Point p1, Point p2, Point p3, Point p4)
        {
            _p1 = p1;
            _p2 = p2;
            _p3 = p3;
            _p4 = p4;
        }

        public boolean isSquare()
        {
            // Verify the sides are the same size.
            int d12 = _p1.squareDistanceTo(_p2);
            int d23 = _p2.squareDistanceTo(_p3);
            int d34 = _p3.squareDistanceTo(_p4);
            int d41 = _p4.squareDistanceTo(_p1);

            boolean lengthsAreSameSize = d12 == d23 && d23 == d34 && d34 == d41;
            if (!lengthsAreSameSize) {
                return false;
            }

            // Verify perpendicularity.
            LineSegment l12 = new LineSegment(_p1, _p2);
            LineSegment l23 = new LineSegment(_p2, _p3);
            LineSegment l34 = new LineSegment(_p3, _p4);
            LineSegment l41 = new LineSegment(_p4, _p1);

            return l12.isPerpendicularTo(l23) &&
                   l23.isPerpendicularTo(l34) &&
                   l34.isPerpendicularTo(l41) &&
                   l41.isPerpendicularTo(l12);
        }
    }
}
