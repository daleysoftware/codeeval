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

            SortedSet<Integer> ss = new TreeSet<Integer>();
            String[] cities = line.split(";");

            for (String c : cities) {
                ss.add(Integer.parseInt(c.split(",")[1]));
            }

            Iterator<Integer> it = ss.iterator();
            int previous = 0;

            while (it.hasNext()) {
                int current = it.next();
                System.out.print(current - previous);
                previous = current;

                if (it.hasNext()) {
                    System.out.print(",");
                }
            }

            System.out.println();
        }
    }
}
