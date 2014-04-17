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

            String[] stringArray = line.split(";");
            int N = Integer.parseInt(stringArray[0].trim());
            stringArray = stringArray[1].trim().split(",");

            int sum = 0;
            for (String s : stringArray) {
                sum += Integer.parseInt(s);
            }

            int expectedSumLessDuplicate = (N-1)*(N-2)/2;
            System.out.println(sum - expectedSumLessDuplicate);
        }

        in.close();
    }
}
