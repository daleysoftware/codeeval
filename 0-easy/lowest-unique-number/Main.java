import java.util.*;
import java.io.*;
import java.util.Arrays;

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

            String[] lineArray = line.split(" ");
            int[] intArray = new int[lineArray.length];

            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

            for (int i = 0; i < intArray.length; i++) {
                int n = Integer.parseInt(lineArray[i]);
                intArray[i] = n;

                if (map.containsKey(n)) {
                    int value = map.get(n);
                    map.put(n, value+1);
                } else {
                    map.put(n, 1);
                }
            }

            Arrays.sort(intArray);

            int lowestUnique = 0;

            for (int i : intArray) {
                if (map.get(i) == 1) {
                    lowestUnique = i;
                    break;
                }
            }

            if (lowestUnique == 0) {
                System.out.println(0);
            } else {
                String n = Integer.toString(lowestUnique);
                for (int i = 0; i < lineArray.length; i++) {
                    if (lineArray[i].equals(n)) {
                        System.out.println(i+1);
                    }
                }
            }
        }
    }
}
