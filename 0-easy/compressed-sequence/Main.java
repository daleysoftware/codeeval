import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String[] lineArray = line.split(" ");
            int[] input = new int[lineArray.length];

            for (int i = 0; i < lineArray.length; i++) {
                input[i] = Integer.parseInt(lineArray[i]);
            }

            printCompressedArray(input);
        }
    }

    public static void printCompressedArray(int[] input)
    {
        if (input.length == 0) {
            return;
        }

        int currentNumber = input[0];
        int currentCount = 1;

        for (int i = 1; i < input.length; i++) {
            int number = input[i];

            if (number != currentNumber) {
                System.out.print(currentCount + " " + currentNumber + " ");

                currentNumber = number;
                currentCount = 1;
            }
            else {
                currentCount++;
            }
        }

        System.out.println(currentCount + " " + currentNumber);
    }
}
