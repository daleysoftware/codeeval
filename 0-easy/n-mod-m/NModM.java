import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class NModM
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String[] lineArray = line.split(",");
            if (lineArray.length > 0) {
                int n = Integer.parseInt(lineArray[0]);
                int m = Integer.parseInt(lineArray[1]);

                System.out.println(nModMWithoutModulusOperator(n, m));
            }
        }
    }

    /**
     * Calculate n mod m without using the built-in modulus operator.
     *
     * N.B. do not assume the integers are positive.
     */
    public static int nModMWithoutModulusOperator(int n, int m)
    {
        int current = n;

        while (Math.abs(current) >= Math.abs(m)) {
            current -= m;
        }

        return current;
    }
}
