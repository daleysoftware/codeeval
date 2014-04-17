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

            String[] stringArray = line.split(",");
            int[] intArray = new int[stringArray.length];

            for (int i = 0; i < intArray.length; i++) {
                intArray[i] = Integer.parseInt(stringArray[i].trim());
            }

            System.out.println(computeLargestContinuousSum(intArray));
        }

        in.close();
    }

    public static int computeLargestContinuousSum(int[] array)
    {
        if (array.length == 0) {
            throw new IllegalArgumentException();
        }

        int bestSum = array[0];

        for (int starting = 0; starting < array.length; starting++) {
            for (int ending = starting; ending < array.length; ending++) {
                int sum = sumIntegerValues(array, starting, ending);

                if (sum > bestSum) {
                    bestSum = sum;
                }

                if (sum < 0) {
                    break;
                }
            }
        }

        return bestSum;
    }

    private static int sumIntegerValues(int[] array, int starting, int ending)
    {
        int sum = 0;

        for (int i = starting; i <= ending; i++) {
            sum += array[i];
        }

        return sum;
    }
}
