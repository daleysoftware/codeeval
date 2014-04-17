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
            String[] lineArray = line.split("\\|");

            String[] list1 = lineArray[0].trim().split(" ");
            String[] list2 = lineArray[1].trim().split(" ");

            assert(list1.length == list2.length);

            for (int i = 0; i < list1.length; i++) {
                System.out.print(Integer.parseInt(list1[i]) * Integer.parseInt(list2[i]));

                if (i != list1.length-1) {
                    System.out.print(" ");
                }
            }

            System.out.println();
        }
    }
}
