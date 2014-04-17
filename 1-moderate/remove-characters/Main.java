import java.io.*;
import java.util.*;

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

            String[] lineArray = line.split(",");

            String sentence = lineArray[0].trim();
            String charsToRemove = lineArray[1].trim();

            System.out.println(removeSpecificCharacters(sentence, charsToRemove));
        }

        in.close();
    }

    public static String removeSpecificCharacters(String sentence, String charsToRemove)
    {
        StringBuilder sb = new StringBuilder();

        for (char c : sentence.toCharArray()) {
            if (!charsToRemove.contains(String.valueOf(c))) {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}
