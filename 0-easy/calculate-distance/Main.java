import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        String patternString = "^\\(([\\d-]+), ([\\d-]+)\\) \\(([\\d-]+), ([\\d-]+)\\)$";
        Pattern pattern = Pattern.compile(patternString);

        while ((line = in.readLine()) != null) {
            line = line.trim();

            Matcher m = pattern.matcher(line);

            if (m.matches()) {
                int x1 = Integer.parseInt(m.group(1));
                int y1 = Integer.parseInt(m.group(2));
                int x2 = Integer.parseInt(m.group(3));
                int y2 = Integer.parseInt(m.group(4));

                int xDiff = x1-x2;
                xDiff *= xDiff;

                int yDiff = y1-y2;
                yDiff *= yDiff;

                int distance = (int) Math.sqrt(xDiff + yDiff);

                System.out.println(distance);
            }
        }
    }
}
