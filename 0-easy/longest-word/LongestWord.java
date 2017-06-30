import java.io.*;

public class LongestWord
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String longestWord = null;
            line = line.trim();

            for (String word : line.split(" ")) {
                if (longestWord == null) {
                    longestWord = word;
                } else if (word.length() > longestWord.length()) {
                    longestWord = word;
                }
            }

            System.out.println(longestWord);
        }
    }
}
