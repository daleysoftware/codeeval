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
            System.out.println(capitalizeWordLetters(line));
        }
    }

    public static String capitalizeWordLetters(String str)
    {
        char[] array = str.toCharArray();

        for (int i = 0; i < array.length; i++) {
            char c = array[i];

            if (i == 0 || Character.isWhitespace(array[i-1])) {
                array[i] = Character.toTitleCase(c);
            }
        }

        return new String(array);
    }
}
