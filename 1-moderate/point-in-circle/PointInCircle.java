import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PointInCircle
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        // Example:
        // Center: (2.12, -3.48); Radius: 17.22; Point: (16.21, -5)
        Pattern p = Pattern.compile(
                "Center: \\(([0-9.\\-]+), ([0-9.\\-]+)\\); " +
                "Radius: ([0-9.\\-]+); Point: \\(([0-9.\\-]+), ([0-9.\\-]+)\\)");

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() == 0) {
                continue;
            }

            Matcher m = p.matcher(line);
            if (m.find()) {
                double centerX = Double.parseDouble(m.group(1));
                double centerY = Double.parseDouble(m.group(2));
                double radius  = Double.parseDouble(m.group(3));
                double pointX  = Double.parseDouble(m.group(4));
                double pointY  = Double.parseDouble(m.group(5));

                Circle circle = new Circle(new Point(centerX, centerY), radius);
                Point point = new Point(pointX, pointY);

                System.out.println(circle.containsPoint(point));
            }
        }

        in.close();
    }

    public static class Point
    {
        private final double _x;
        private final double _y;

        public Point(double x, double y)
        {
            _x = x;
            _y = y;
        }

        public double getX()
        {
            return _x;
        }

        public double getY()
        {
            return _y;
        }
    }

    public static class Circle
    {
        private final Point _center;
        private final double _radius;

        public Circle(Point center, double radius)
        {
            _center = center;
            _radius = radius;
        }

        public boolean containsPoint(Point p)
        {
            double xDiff = _center.getX() - p.getX();
            double yDiff = _center.getY() - p.getY();

            double distance = Math.sqrt((xDiff*xDiff) + (yDiff*yDiff));
            return distance < _radius;
        }
    }
}
