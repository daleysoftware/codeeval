import java.io.*;
import java.util.*;

public class StringPermutations
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

            Set<String> result = permute(line);

            Iterator<String> it = result.iterator();

            while (it.hasNext()) {
                System.out.print(it.next());

                if (it.hasNext()) {
                    System.out.print(",");
                }
            }

            System.out.println();
        }

        in.close();
    }

    public static Set<String> permute(String str)
    {
        char[] array = str.toCharArray();

        Set<String> result = new TreeSet<String>();
        permute(array, 0, result);

        return result;
    }

    private static void permute(char[] array, int index, Set<String> result)
    {
        if (index == array.length-1) {
            result.add(new String(array));
            return;
        }

        for (int i = index; i < array.length; i++) {
            swap(array, i, index);
            permute(array, index+1, result);
            swap(array, i, index);
        }
    }

    private static void swap(char[] array, int index1, int index2)
    {
        char tmp = array[index1];
        array[index1] = array[index2];
        array[index2] = tmp;
    }
}
