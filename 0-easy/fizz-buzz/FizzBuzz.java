import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class FizzBuzz
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String[] lineArray = line.split(" ");
            if (lineArray.length > 0) {
                int a = Integer.parseInt(lineArray[0]);
                int b = Integer.parseInt(lineArray[1]);
                int n = Integer.parseInt(lineArray[2]);

                doFizzBuzz(a, b, n);
                System.out.println();
            }
        }
    }

    private static void doFizzBuzz(int a, int b, int n)
    {
        for (int i = 1; i <= n; i++) {

            boolean isDivisibleByA = isNDivisibleByX(i, a);
            boolean isDivisibleByB = isNDivisibleByX(i, b);

            if (isDivisibleByA && isDivisibleByB) {
                System.out.print("FB");
            } else if (isDivisibleByA) {
                System.out.print("F");
            } else if (isDivisibleByB) {
                System.out.print("B");
            } else {
                System.out.print(i);
            }

            if (i < n) {
                System.out.print(" ");
            }
        }
    }

    private static boolean isNDivisibleByX(int n, int x)
    {
        return n % x == 0;
    }
}
