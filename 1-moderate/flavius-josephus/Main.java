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
            String[] split = line.split(",");

            int total = Integer.parseInt(split[0]);
            int next = Integer.parseInt(split[1]);

            boolean[] killed = new boolean[total];

            int current = 0;
            for (int i = 0; i < total; i++) {
                int count = 0;

                while (true) {
                    if (!killed[current]) {
                        count++;

                        if (count == next) {
                            break;
                        }
                    }

                    current++;
                    current %= total;
                }

                killed[current] = true;
                System.out.print(current);

                if (i+1 != total) {
                    System.out.print(" ");
                }
            }

            System.out.println();
        }
    }
}
