import java.text.NumberFormat;
import java.util.*;
import java.io.*;

/**
 * Order of operations:
 *
 *   1 ()  Brackets
 *   2 -   Unary minus
 *   3 ^   Exponent
 *   4 *,/ Multiply, Divide (left-to-right precedence)
 *   5 +,- Add, Subtract (left-to-right precedence)
 *
 * Example input:
 *
 *   250*14.3
 *   3^6 / 117
 *   (2.16 - 48.34)^-1
 *   (59 - 15 + 3*6)/21
 *   8-(1*(2+2))-4
 */
public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String rpn = infixToReversePolish(line.trim());
            double result = evaluateReversePolish(rpn);

            NumberFormat f = NumberFormat.getNumberInstance();
            f.setMaximumFractionDigits(5);
            f.setGroupingUsed(false);

            System.out.println(f.format(result));
        }
    }

    public static double evaluateReversePolish(String rpn)
    {
        String[] elements = rpn.split(" ");
        Stack<String> stack = new Stack<String>();

        for (String e : elements) {

            boolean isOperator = isOperator(e);

            if (!isOperator) {
                stack.push(e);
            } else {
                if (stack.size() < 2) {
                    throw new IllegalArgumentException();
                }

                double second = Double.parseDouble(stack.pop());

                double first;
                String firstString = stack.pop();

                if (firstString.length() == 0) {
                    first = 0.0;
                } else {
                    first = Double.parseDouble(firstString);
                }

                double result = 0.0d;
                switch (e.charAt(0)) {
                    case '+':
                        result = first + second;
                        break;
                    case '-':
                        result = first - second;
                        break;
                    case '*':
                        result = first * second;
                        break;
                    case '/':
                        result = first / second;
                        break;
                    case '^':
                        result = Math.pow(first, second);
                        break;
                }

                stack.push(Double.toString(result));
            }

        }

        if (stack.size() != 1) {
            throw new IllegalArgumentException();
        }

        return Double.parseDouble(stack.pop());
    }

   public static String infixToReversePolish(String infix)
    {
        char[] in = infix.toCharArray();
        StringBuilder rpn = new StringBuilder();
        Stack<Character> stack = new Stack<Character>();

        for (char c : in)
        {
            switch (c) {
                case '+':
                case '-':
                    while (!stack.empty() && isOperator(stack.peek())) {
                        rpn.append(' ');
                        rpn.append(stack.pop());
                    }
                    rpn.append(' ');
                    stack.push(c);
                    break;
                case '*':
                case '/':
                    while (!stack.empty() && (
                            stack.peek() == '^' ||
                            stack.peek() == '*' ||
                            stack.peek() == '/')) {
                        rpn.append(' ');
                        rpn.append(stack.pop());
                    }
                case '^':
                    rpn.append(' ');
                    stack.push(c);
                    break;
                case '(':
                    stack.push(c);
                    break;
                case ')':
                    while (!stack.empty() && stack.peek() != '(') {
                        rpn.append(' ');
                        rpn.append(stack.pop());
                    }
                    stack.pop();
                    break;
                default:
                    if (!Character.isWhitespace(c)) {
                        rpn.append(c);
                    }
                    break;
            }
        }

        while (!stack.empty()) {
            rpn.append(' ');
            rpn.append(stack.pop());
        }

        return rpn.toString();
    }

    private static boolean isOperator(String s)
    {
        s = s.trim();
        return s.length() == 1 && isOperator(s.charAt(0));
    }

    private static boolean isOperator(char c)
    {
        switch (c) {
            case '+':
            case '-':
            case '*':
            case '/':
            case '^':
                return true;
            default:
                return false;
        }
    }
}
