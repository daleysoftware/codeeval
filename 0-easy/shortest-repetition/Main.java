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
            line = line.trim();

            for (int i = 1; i <= line.length(); i++) {
                String sub = line.substring(0, i);

                String[] lineArray = line.split(sub);

                boolean allSplitElementsEmpty = true;
                for (String s : lineArray) {
                    if (!s.isEmpty()) {
                        allSplitElementsEmpty = false;
                        break;
                    }
                }

                if (allSplitElementsEmpty) {
                    System.out.println(sub.length());
                    break;
                }
            }
        }
    }
}
