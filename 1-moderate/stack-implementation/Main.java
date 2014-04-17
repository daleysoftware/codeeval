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

            String[] stringArray = line.split(" ");
            int[] intArray = new int[stringArray.length];

            for (int i = 0; i < intArray.length; i++) {
                intArray[i] = Integer.parseInt(stringArray[i]);
            }

            Stack<Integer> stack = new Stack<Integer>();

            for (int i : intArray) {
                stack.push(i);
            }

            boolean print = true;
            while (!stack.isEmpty()) {
                int i = stack.pop();

                if (print) {
                    System.out.print(i);

                    if (stack.size() >= 2) {
                        System.out.print(" ");
                    }
                }

                print = !print;
            }

            System.out.println();
        }

        in.close();
    }
}
