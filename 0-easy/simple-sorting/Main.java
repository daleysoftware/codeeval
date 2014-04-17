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
            String[] stringArray = line.split(" ");
            double[] doubleArray = new double[stringArray.length];

            for (int i = 0; i < stringArray.length; i++) {
                doubleArray[i] = Double.parseDouble(stringArray[i]);
            }

            Arrays.sort(doubleArray);

            for (int i = 0; i < doubleArray.length; i++) {
                System.out.format("%.3f", doubleArray[i]);

                if (i == doubleArray.length-1) {
                    System.out.println();
                } else {
                    System.out.print(" ");
                }
            }
        }
    }

}
