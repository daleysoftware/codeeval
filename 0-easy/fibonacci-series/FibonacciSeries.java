import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class FibonacciSeries
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() > 0) {
                String[] lineArray = line.trim().split(",");
                int position = Integer.parseInt(lineArray[0]);

                System.out.println(fibonacciNumberAtPosition(position));
            }
        }
    }

    public static int fibonacciNumberAtPosition(int position)
    {
        if (position == 0) {
            return 0;
        } else if (position == 1) {
            return 1;
        }

        int nMinus2 = 0;
        int nMinus1 = 1;
        int next = 0;

        for (int i = 2; i <= position; i++) {
            next = nextFibonacci(nMinus1, nMinus2);

            nMinus2 = nMinus1;
            nMinus1 = next;
        }

        return next;
    }

    private static int nextFibonacci(int nMinus2, int nMinus1)
    {
        return nMinus1 + nMinus2;
    }
}
