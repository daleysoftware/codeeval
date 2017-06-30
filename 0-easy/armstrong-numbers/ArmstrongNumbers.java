import java.io.*;

public class ArmstrongNumbers
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (isArmstrongNumber(Integer.parseInt(line))) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        }
    }

    /**
     * An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.
     */
    public static boolean isArmstrongNumber(int n)
    {
        int digits = digitCount(n);

        int sum = 0;
        int working = n;

        while (working > 0) {
            int digit = working % 10;
            int multipliedDigit = digit;

            for (int i = 1; i < digits; i++) {
                multipliedDigit *= digit;
            }

            sum += multipliedDigit;
            working /= 10;
        }

        return sum == n;
    }

    public static int digitCount(int n)
    {
        int count = 0;

        while (n > 0) {
            count++;
            n /= 10;
        }

        return count;
    }
}
