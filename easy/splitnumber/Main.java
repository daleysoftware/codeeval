package codeeval.easy.splitnumber;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Main
{
    private enum Operation
    {
        ADD,
        SUBTRACT
    }

    private static int previous;
    private static int current;
    private static Operation op;

    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String number = line.split(" ")[0];
            String expression = line.split(" ")[1];

            previous = 0;
            current = 0;
            op = Operation.ADD;

            for (char c : expression.toCharArray()) {
                if (c == '+') {
                    evaluate();
                    op = Operation.ADD;
                } else if (c == '-') {
                    evaluate();
                    op = Operation.SUBTRACT;
                } else {
                    current *= 10;
                    current += Character.getNumericValue(number.charAt(c - 'a'));
                }
            }

            evaluate();
            System.out.println(previous);
        }
    }

    private static void evaluate()
    {
        switch (op) {
            case ADD:
                previous += current;
                break;
            case SUBTRACT:
                previous -= current;
                break;
        }

        current = 0;
    }
}
