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
            String[] lineArray = line.trim().split(",");

            String word = lineArray[0];
            char c = lineArray[1].toCharArray()[0];

            System.out.println(word.lastIndexOf(c));
        }
    }
}
