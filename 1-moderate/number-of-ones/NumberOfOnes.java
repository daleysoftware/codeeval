import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class NumberOfOnes
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

            int n = Integer.parseInt(line);
            int numberOfOnes = countNumberOfOneBits(n);

            System.out.println(numberOfOnes);
        }

        in.close();
    }

    public static int countNumberOfOneBits(int n)
    {
        int count = 0;

        while (n != 0) {
            int lastBit = n & 0x1;

            if (lastBit != 0) {
                count++;
            }

            n >>= 1;
        }

        return count;
    }
}
