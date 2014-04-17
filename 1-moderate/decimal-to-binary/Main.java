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

            int n = Integer.parseInt(line);
            System.out.println(Integer.toBinaryString(n));
        }

        in.close();
    }
}
