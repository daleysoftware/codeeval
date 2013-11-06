package codeeval.easy.setintersection;

import java.util.*;
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
            String[] sets = line.split(";");

            Set<Integer> set1 = stringToIntegerSet(sets[0]);
            Set<Integer> set2 = stringToIntegerSet(sets[1]);

            // Compute the set intersection.
            SortedSet<Integer> intersection = new TreeSet<Integer>();

            for (Integer i : set1) {
                if (set2.contains(i) && !intersection.contains(i)) {
                    intersection.add(i);
                }
            }

            Iterator<Integer> it = intersection.iterator();

            while (it.hasNext()) {
                System.out.print(it.next());

                if (it.hasNext()) {
                    System.out.print(",");
                }
            }

            System.out.println();
        }
    }

    public static Set<Integer> stringToIntegerSet(String str)
    {
        String[] array = str.split(",");
        HashSet<Integer> set = new HashSet<Integer>();

        for (String s : array) {
            set.add(Integer.parseInt(s));
        }

        return set;
    }
}
