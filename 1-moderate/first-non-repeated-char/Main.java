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

            System.out.println(findFirstNonRepeatedChar(line.toCharArray()));
        }

        in.close();
    }

    /**
     * Find the first non-repeated character in the given character array.
     *
     * Note that this function does not handle the case where there is no non-repeated
     * characters. In this case it will throw an IllegalArgumentException.
     */
    public static char findFirstNonRepeatedChar(char[] string)
    {
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        for (char c : string) {
            if (!map.containsKey(c)) {
                map.put(c, 1);
            } else {
                map.put(c, map.get(c) + 1);
            }
        }

        for (char c : string) {
            int count = map.get(c);

            if (count == 1) {
                return c;
            }
        }

        throw new IllegalArgumentException();
    }
}
