import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.TreeMap;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        TreeMap<Integer, String> tm = new TreeMap<Integer, String>();
        int n = Integer.parseInt(in.readLine());

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() > 0) {
                tm.put(line.length(), line);
            }
        }

        int counter = 0;
        for (Integer i : tm.descendingKeySet()) {
            line = tm.get(i);
            System.out.println(line);

            counter++;
            if (counter == n) {
                break;
            }
        }
    }
}
