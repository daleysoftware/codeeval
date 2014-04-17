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

            int rows = Integer.parseInt(line);
            printPascalsTriangle(rows);
        }

        in.close();
    }

    public static void printPascalsTriangle(int rows)
    {
        int[] previous = new int[Math.max(2, rows)];
        int[] current = new int[Math.max(2, rows)];

        previous[0] = 1;
        current[0] = 1;
        current[1] = 1;

        boolean firstPrinted = false;

        for (int i = 0; i < rows; i++)
        {
            int[] tmp = current;
            current = previous;
            previous = tmp;

            for (int j = 1; j <= i; j++) {
                current[j] = previous[j-1] + previous[j];
            }

            for (int c : current) {
                if (c == 0) {
                    break;
                }

                if (firstPrinted) {
                    System.out.print(" ");
                } else {
                    firstPrinted = true;
                }

                System.out.print(c);
            }
        }

        System.out.println();
    }
}
