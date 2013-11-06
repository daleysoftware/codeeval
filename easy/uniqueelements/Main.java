package codeeval.easy.uniqueelements;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.LinkedHashSet;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;


        while ((line = in.readLine()) != null) {
            LinkedHashSet<Integer> lhs = new LinkedHashSet<Integer>();

            line = line.trim();
            String[] lineArray = line.split(",");


            for (String s : lineArray) {
                int n = Integer.parseInt(s);

                if (!lhs.contains(n)) {
                    lhs.add(n);
                }
            }

            Iterator<Integer> it = lhs.iterator();

            while (true) {
                System.out.print(it.next());

                if (it.hasNext()) {
                    System.out.print(",");
                } else {
                    System.out.println();
                    break;
                }
            }
        }
    }
}
