import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Stack;

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

            if (line.length() > 0) {
                String[] lineArray = line.trim().split(" ");

                // The integer m, the 1-based index of the element from the back of the list.
                int m = Integer.parseInt(lineArray[lineArray.length - 1]);

                Stack<String> s = new Stack<String>();
                s.addAll(Arrays.asList(lineArray).subList(0, lineArray.length-1));

                // Ignore input if the index is too large or otherwise out of bounds.
                if (m > s.size() || m < 1) {
                    continue;
                }

                String result = s.pop();
                for (int i = 2; i <= m; i++) {
                    result = s.pop();
                }

                System.out.println(result);
            }
        }
    }
}
