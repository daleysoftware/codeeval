import java.io.*;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String hiddenDigits = getHiddenDigits(line.trim());

            if (hiddenDigits.length() == 0) {
                System.out.println("NONE");
            } else {
                System.out.println(hiddenDigits);
            }
        }
    }

    private static String getHiddenDigits(String s)
    {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            char c = mapCharacter(s.charAt(i));

            if (Character.isDigit(c)) {
                sb.append(c);
            }
        }

        return sb.toString();
    }

    private static char mapCharacter(char c)
    {
        switch (c) {
            case 'a':
                return '0';
            case 'b':
                return '1';
            case 'c':
                return '2';
            case 'd':
                return '3';
            case 'e':
                return '4';
            case 'f':
                return '5';
            case 'g':
                return '6';
            case 'h':
                return '7';
            case 'i':
                return '8';
            case 'j':
                return '9';
            default:
                return c;
        }
    }
}
