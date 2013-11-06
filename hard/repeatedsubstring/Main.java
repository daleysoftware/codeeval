package codeeval.hard.repeatedsubstring;

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
            line = line.trim();

            if (line.length() > 0) {
                String result = longestRepeatedSubstring(line);

                if (result != null) {
                    System.out.println(result);
                } else {
                    System.out.println("NONE");
                }
            }
        }
    }

    public static String longestRepeatedSubstring(String str)
    {
        return longestRepeatedSubstring(str.toCharArray());
    }

    private static String longestRepeatedSubstring(char[] str)
    {
        boolean foundRepeatedSubstring = false;
        int bestIndex = 0;
        int bestLength = 0;

        for (int width = 1; width <= str.length/2; width++) {

            for (int offset = 0; offset <= str.length-(2*width); offset++) {
                String base = new String(str, offset, width);

                if (isStringAllWhitespace(base)) {
                    continue;
                }

                boolean continueToNextOffset = true;
                for (int current = offset+width; current <= str.length-width; current++) {
                    String compare = new String(str, current, width);

                    if (base.equals(compare)) {
                        foundRepeatedSubstring = true;
                        bestIndex = offset;
                        bestLength = width;

                        continueToNextOffset = false;
                        break;
                    }
                }

                if (!continueToNextOffset) {
                    break;
                }
            }
        }

        if (foundRepeatedSubstring) {
            return new String(str, bestIndex, bestLength);
        } else {
            return null;
        }
    }

    private static boolean isStringAllWhitespace(String str)
    {
        for (char c : str.toCharArray()) {
            if (!Character.isWhitespace(c)) {
                return false;
            }
        }

        return true;
    }
}