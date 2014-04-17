import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line.trim());

            if ((n & 0x1) == 0) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
