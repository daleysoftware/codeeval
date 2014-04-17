import java.io.*;
import java.util.*;

/**
 * Solution uses a variation of the Sieve of Eratosthenes. Solution is O(n ln(ln(n))) time
 * complexity.
 *
 * See http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
 */
public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        LinkedList<Integer> maxes = new LinkedList<Integer>();
        int largestMax = 0;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() == 0) {
                continue;
            }

            int max = Integer.parseInt(line);
            maxes.add(max);

            if (max > largestMax) {
                largestMax = max;
            }
        }

        boolean[] isCompositeTable = computeIsCompositeTable(largestMax);
        for (int max : maxes) {
            boolean comma = false;
            for (int i = 2; i < max; i++) {
                if (!isCompositeTable[i]) {
                    if (comma) {
                        System.out.print(",");
                    }

                    comma = true;
                    System.out.print(i);
                }
            }

            System.out.println();
        }

        in.close();
    }

    public static boolean[] computeIsCompositeTable(int max)
    {
        boolean[] isComposite = new boolean[max];
        for (int i = 0; i < isComposite.length; i++) {
            isComposite[i] = false;
        }

        int currentPrime = 2;
        while (true) {
            for (int i = currentPrime; i * currentPrime < max; i++) {
                isComposite[i * currentPrime] = true;
            }

            boolean more = false;
            for (int i = currentPrime+1; i < max; i++) {
                if (!isComposite[i]) {
                    currentPrime = i;
                    more = true;
                    break;
                }
            }

            if (!more) {
                break;
            }
        }

        return isComposite;
    }
}
