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

            if (isValidParenthesis(line)) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        }

        in.close();
    }

    public static boolean isValidParenthesis(String str)
    {
        Stack<Character> stack = new Stack<Character>();

        for (Character c : str.toCharArray()) {
            if (isLeftBracket(c)) {
                stack.push(c);
            } else if (isRightBracket(c)) {
                if (stack.size() == 0) {
                    return false;
                }

                char popped = stack.pop();
                switch (popped) {
                    case '(':
                        if (c != ')') {
                            return false;
                        }
                        break;
                    case '{':
                        if (c != '}') {
                            return false;
                        }
                        break;
                    case '[':
                        if (c != ']') {
                            return false;
                        }
                        break;
                    default:
                        return false;
                }
            }
        }

        return stack.size() == 0;
    }

    public static boolean isLeftBracket(char c)
    {
        return c == '[' || c == '{' || c == '(';
    }

    public static boolean isRightBracket(char c)
    {
        return c == ']' || c == '}' || c == ')';
    }

}
