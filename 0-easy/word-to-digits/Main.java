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
            String[] lineArray = line.split(";");

            for (String word : lineArray) {
                if (word.equals("zero")) {
                    System.out.print(0);
                } else if (word.equals("one")) {
                    System.out.print(1);
                } else if (word.equals("two")) {
                    System.out.print(2);
                } else if (word.equals("three")) {
                    System.out.print(3);
                } else if (word.equals("four")) {
                    System.out.print(4);
                } else if (word.equals("five")) {
                    System.out.print(5);
                } else if (word.equals("six")) {
                    System.out.print(6);
                } else if (word.equals("seven")) {
                    System.out.print(7);
                } else if (word.equals("eight")) {
                    System.out.print(8);
                } else if (word.equals("nine")) {
                    System.out.print(9);
                }
            }

            System.out.println();
        }
    }
}
