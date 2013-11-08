package codeeval.moderate.countingprimes;

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

        LinkedList<IntegerRange> ranges = new LinkedList<IntegerRange>();
        int largestMax = 0;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() == 0) {
                continue;
            }

            String[] array = line.split(",");
            int min = Integer.parseInt(array[0]);
            int max = Integer.parseInt(array[1]);
            ranges.add(new IntegerRange(min, max));

            if (max > largestMax) {
                largestMax = max;
            }
        }

        boolean[] isComposite = computeIsCompositeTable(largestMax+1);
        for (IntegerRange r : ranges) {
            int primeCount = 0;
            for (int i = r.getMin(); i <= r.getMax(); i++) {
                if (!isComposite[i]) {
                    primeCount++;
                }
            }

            System.out.println(primeCount);
        }

        in.close();
    }

    public static class IntegerRange
    {
        private final int _min;
        private final int _max;

        public IntegerRange(int min, int max)
        {
            _min = min;
            _max = max;
        }

        public int getMin()
        {
            return _min;
        }

        public int getMax()
        {
            return _max;
        }
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
