package codeeval.easy.mixedcontent;

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
            String[] lineArray = line.trim().split(",");

            LinkedList<Integer> integers = new LinkedList<Integer>();
            LinkedList<String> strings = new LinkedList<String>();

            for (String s : lineArray) {
                try {
                    int i = Integer.parseInt(s);
                    integers.add(i);
                } catch (NumberFormatException e) {
                    strings.add(s);
                }
            }

            if (strings.size() > 0) {
                Iterator<String> it = strings.iterator();

                while (true) {
                    System.out.print(it.next());

                    if (it.hasNext()) {
                        System.out.print(",");
                    } else {
                        break;
                    }
                }
            }

            if (integers.size() > 0) {
                if (strings.size() > 0) {
                    System.out.print("|");
                }

                Iterator<Integer> it = integers.iterator();

                while (true) {
                    System.out.print(it.next());

                    if (it.hasNext()) {
                        System.out.print(",");
                    } else {
                        break;
                    }
                }
            }

            System.out.println();
        }
    }
}