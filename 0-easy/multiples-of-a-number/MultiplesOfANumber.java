import java.io.*;

public class MultiplesOfANumber
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String[] lineArray = line.trim().split(",");

            int x = Integer.parseInt(lineArray[0]);
            int n = Integer.parseInt(lineArray[1]);

            System.out.println(findNextMultipleOfNGreaterThanX(x, n));
        }
    }

    public static int findNextMultipleOfNGreaterThanX(int x, int n)
    {
        int multiplier = 1;

        while (true) {
            int multiple = n * multiplier;

            if (multiple > x) {
                return multiple;
            }

            multiplier++;
        }
    }
}
