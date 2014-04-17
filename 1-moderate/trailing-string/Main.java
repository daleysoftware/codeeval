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

            if (line.length() == 0) {
                continue;
            }

            String[] stringArray = line.split(",");

            String s1 = stringArray[0].trim();
            String s2 = stringArray[1].trim();

            if (s1.endsWith(s2)) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }

        in.close();
    }
}
