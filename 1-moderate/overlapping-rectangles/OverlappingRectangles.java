import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

class Point
{
    private int m_x;
    private int m_y;

    public Point(int x, int y)
    {
        m_x = x;
        m_y = y;
    }

    int getX()
    {
        return m_x;
    }

    int getY()
    {
        return m_y;
    }
}

class Rectangle
{
    private Point m_upperLeft;
    private Point m_lowerRight;

    public Rectangle(Point upperLeft, Point lowerRight)
    {
        m_upperLeft = upperLeft;
        m_lowerRight = lowerRight;
    }

    private boolean containsPoint(Point p)
    {
        boolean fitsInX = m_upperLeft.getX() <= p.getX() && p.getX() <= m_lowerRight.getX();
        boolean fitsInY =  m_lowerRight.getY() <= p.getY() && p.getY() <= m_upperLeft.getY();

        return fitsInX && fitsInY;
    }

    boolean overlapsWith(Rectangle r)
    {
        // Left side
        for (int y = m_lowerRight.getY(); y <= m_upperLeft.getY(); y++) {
            if (r.containsPoint(new Point(m_upperLeft.getX(), y))) {
                return true;
            }
        }

        // Top side
        for (int x = m_upperLeft.getX(); x <= m_lowerRight.getX(); x++) {
            if (r.containsPoint(new Point(x, m_upperLeft.getY()))) {
                return true;
            }
        }

        // Right side
        for (int y = m_lowerRight.getY(); y <= m_upperLeft.getY(); y++) {
            if (r.containsPoint(new Point(m_lowerRight.getX(), y))) {
                return true;
            }
        }

        // Bottom side
        for (int x = m_upperLeft.getX(); x <= m_lowerRight.getX(); x++) {
            if (r.containsPoint(new Point(x, m_lowerRight.getY()))) {
                return true;
            }
        }

        return false;
    }
}

class OverlappingRectangles
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

            String[] stringArray = line.split(",");
            int[] intArray = new int[stringArray.length];

            for (int i = 0; i < intArray.length; i++) {
                intArray[i] = Integer.parseInt(stringArray[i].trim());
            }

            Rectangle r1 = new Rectangle(
                    new Point(intArray[0], intArray[1]),
                    new Point(intArray[2], intArray[3]));
            Rectangle r2 = new Rectangle(
                    new Point(intArray[4], intArray[5]),
                    new Point(intArray[6], intArray[7]));

            if (r1.overlapsWith(r2)) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }

        }

        in.close();
    }
}
