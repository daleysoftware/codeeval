import java.io.*;

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

            String[] stringArray = line.split(";");

            int reverseCount = Integer.parseInt(stringArray[1]);
            stringArray = stringArray[0].split(",");
            int[] intArray = new int[stringArray.length];

            for (int i = 0; i < intArray.length; i++) {
                intArray[i] = Integer.parseInt(stringArray[i]);
            }

            for (int i = 0; i+reverseCount-1 < intArray.length; i += reverseCount) {
                for (int j = 0; j < reverseCount/2; j++) {
                    int firstIndex = i + j;
                    int secondIndex = i + reverseCount - j - 1;

                    int tmp = intArray[firstIndex];
                    intArray[firstIndex] = intArray[secondIndex];
                    intArray[secondIndex] = tmp;
                }
            }

            for (int i = 0; i < intArray.length; i++) {
                System.out.print(intArray[i]);

                if (i+1 != intArray.length) {
                    System.out.print(",");
                }
            }

            System.out.println();
        }
    }
}
