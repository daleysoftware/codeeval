package codeeval.easy.famouswriter;

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

            if (line.length() == 0) {
                continue;
            }

            String[] lineArray = line.split("\\|");

            String encoded = lineArray[0];
            String keyString = lineArray[1].trim();

            StringBuilder sb = new StringBuilder();

            for (String s : keyString.split(" ")) {
                int i = Integer.parseInt(s);
                sb.append(encoded.charAt(i-1));
            }

            System.out.println(sb.toString());
        }
    }

}