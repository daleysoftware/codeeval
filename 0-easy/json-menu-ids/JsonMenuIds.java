import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * JSON Menu IDs problem.
 *
 * If I were solving this in real life I'd use a JSON parser library. But for the purposes of this problem, I'm just
 * going to find the ID tags and extract those individually. Rolling an entire JSON parse myself seems like a bit much.
 */
public class JsonMenuIds
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

            int sum = 0;

            Pattern p = Pattern.compile("\"id\": (\\d+), \"label\"");
            Matcher m = p.matcher(line);
            while (m.find()) {
                sum += Integer.parseInt(m.group(1));
            }

            System.out.println(sum);
        }
    }
}
