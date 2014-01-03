package codeeval.moderate.overlappingrectangles;

import java.io.*;
import java.util.*;

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

            // TODO
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
    }

    public static class Rectangle
    {
        public Rectangle()
        {

        }
    }
}
