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
            line = line.trim();
            System.out.println(swapCase(line));
        }
    }

    public static String swapCase(String str)
    {
        char[] array = str.toCharArray();

        for (int i = 0; i < array.length; i++) {
            char c = array[i];

            if (Character.isLowerCase(c)) {
                array[i] = Character.toTitleCase(c);
            } else {
                array[i] = Character.toLowerCase(c);
            }
        }

        return new String(array);
    }
}
