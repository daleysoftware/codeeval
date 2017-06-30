import java.io.*;
import java.util.*;

public class NumberPairs
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

            String[] stringArray = line.split(";");
            int sumToValue = Integer.parseInt(stringArray[1]);
            stringArray = stringArray[0].split(",");
            int[] intArray = new int[stringArray.length];

            for (int i = 0; i < intArray.length; i++) {
                intArray[i] = Integer.parseInt(stringArray[i]);
            }

            List<IntegerPair> pairs = findPairsMatchingSum(intArray, sumToValue);

            if (pairs.size() == 0) {
                System.out.println("NULL");
            } else {
                Iterator<IntegerPair> it = pairs.iterator();

                while (it.hasNext()) {
                    System.out.print(it.next());

                    if (it.hasNext()) {
                        System.out.print(";");
                    }
                }

                System.out.println();
            }
        }

        in.close();
    }

    public static List<IntegerPair> findPairsMatchingSum(int[] array, int desiredSum)
    {
        array = sortAndRemoveDuplicates(array);
        LinkedList<IntegerPair> result = new LinkedList<IntegerPair>();

        int right = array.length - 1;

        for (int left = 0; left < array.length && array[left] <= desiredSum/2; left++) {
            while (left < right && array[left] + array[right] > desiredSum) {
                right--;
            }

            if (left >= right) {
                break;
            }

            if (array[left] + array[right] == desiredSum) {
                result.add(new IntegerPair(array[left], array[right]));
            }
        }

        return result;
    }

    public static int[] sortAndRemoveDuplicates(int[] array)
    {
        if (array.length == 0) {
            throw new IllegalArgumentException();
        }

        Arrays.sort(array);
        int[] working = new int[array.length];

        working[0] = array[0];

        int previousValue = working[0];
        int currentIndex = 0;

        for (int i = 1; i < array.length; i++) {
            int currentValue = array[i];

            if (currentValue == previousValue) {
                continue;
            }

            currentIndex++;
            working[currentIndex] = currentValue;
        }

        int[] result = new int[currentIndex+1];
        System.arraycopy(working, 0, result, 0, result.length);

        return result;
    }

    public static class IntegerPair
    {
        public int _min;
        public int _max;

        public IntegerPair(int min, int max)
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

        public String toString()
        {
            return Integer.toString(getMin()) + "," + Integer.toString(getMax());
        }
    }
}
