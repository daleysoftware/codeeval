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
                String[] lineArray = line.trim().split(",");

                if (lineArray.length > 0) {
                    int n = Integer.parseInt(lineArray[0]);
                    int p1 = Integer.parseInt(lineArray[1]);
                    int p2 = Integer.parseInt(lineArray[2]);

                    System.out.println(isBitAtPositionTheSame(n, p1, p2));
                }
            }
        }
    }

    public static boolean isBitAtPositionTheSame(int n, int p1, int p2)
    {
        boolean bit1 = (n & (0x1 << (p1-1))) == 0;
        boolean bit2 = (n & (0x1 << (p2-1))) == 0;

        return bit1 == bit2;
    }
}
