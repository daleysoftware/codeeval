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

            String missedLetters = getMissedLetters(line);

            if (missedLetters.length() == 0) {
                System.out.println("NULL");
            } else {
                System.out.println(missedLetters);
            }
        }

        in.close();
    }

    public static String getMissedLetters(String str)
    {
        char[] allLetters = "abcdefghijklmnopqrstuvwxyz".toCharArray();

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (char c : allLetters) {
            map.put(c, 0);
        }

        for (char c : str.toCharArray()) {
            c = Character.toLowerCase(c);

            if (map.containsKey(c)) {
                map.put(c, map.get(c)+1);
            }
        }

        StringBuilder sb = new StringBuilder();

        for (char c : allLetters) {
            if (map.get(c) == 0) {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}
