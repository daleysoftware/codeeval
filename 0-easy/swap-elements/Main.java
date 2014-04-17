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

            String[] lineStringArray = line.split(":");
            String[] elementStringArray = lineStringArray[0].trim().split(" ");
            String[] swapStringArray = lineStringArray[1].trim().split(",");

            int[] elementArray = new int[elementStringArray.length];
            for (int i = 0; i < elementArray.length; i++) {
                elementArray[i] = Integer.parseInt(elementStringArray[i]);
            }

            for (String s : swapStringArray) {
                s = s.trim();
                String[] sArray = s.split("-");

                int firstElement = Integer.parseInt(sArray[0]);
                int secondElement = Integer.parseInt(sArray[1]);

                int tmp = elementArray[firstElement];
                elementArray[firstElement] = elementArray[secondElement];
                elementArray[secondElement] = tmp;
            }

            for (int i = 0; i < elementArray.length; i++) {
                System.out.print(elementArray[i]);

                if (i == elementArray.length-1) {
                    System.out.println();
                } else {
                    System.out.print(" ");
                }
            }
        }
    }
}
