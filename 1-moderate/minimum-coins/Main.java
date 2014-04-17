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
            int remaining = Integer.parseInt(line.trim());

            int fives = remaining / 5;
            remaining -= fives * 5;

            int threes = remaining / 3;
            remaining -= threes * 3;

            int ones = remaining;

            System.out.println(fives + threes + ones);
        }
    }
}
