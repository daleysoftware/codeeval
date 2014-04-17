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

            String[] split = line.split(",");
            String word1 = split[0];
            String word2 = split[1];

            if (isStringRotation(word1, word2)) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        }
    }

    public static boolean isStringRotation(String word1, String word2)
    {
        char[] a1 = word1.toCharArray();
        char[] a2 = word2.toCharArray();

        if (a1.length != a2.length) {
            return false;
        }

        for (int i = 0; i < a2.length; i++) {
            if (isCircularArrayEqual(a1, 0, a2, i)) {
                return true;
            }
        }

        return false;
    }

    public static boolean isCircularArrayEqual(char[] a1, int start1,
                                               char[] a2, int start2)
    {
        if (a1.length != a2.length) {
            return false;
        }

        int length = a1.length;
        for (int i = 0, c1 = start1, c2 = start2; i < length; i++, c1++, c2++) {
            int index1 = c1 % length;
            int index2 = c2 % length;

            if (a1[index1] != a2[index2]) {
                return false;
            }
        }

        return true;
    }
}
