import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

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

                if (lineArray.length > 0) {
                    for (int i = lineArray.length-1; i >= 0; i--) {
                        System.out.print(lineArray[i]);

                        if (i == 0) {
                            System.out.println();
                        } else {
                            System.out.print(" ");
                        }
                    }
                }
            }
        }
    }
}
