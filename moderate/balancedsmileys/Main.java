package codeeval.moderate.balancedsmileys;

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

            if (isBalancedParenthesis(line)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }

        }
    }

    /**
     * A message has balanced parenthesis if it consists of one of the following:
     *
     * 1. An empty string ""
     * 2. One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a
     *    colon)
     * 3. An open parenthesis '(', followed by a message with balanced parentheses,
     *    followed by a close parenthesis ')'.
     * 4. A message with balanced parentheses followed by another message with balanced
     *    parentheses.
     * 5. A smiley face ":)" or a frowny face ":("
     */
    public static boolean isBalancedParenthesis(String str)
    {
        // TODO
        return false;
    }
}