package codeeval.moderate.uricomp;

import java.io.*;
import java.net.URI;
import java.net.URISyntaxException;

public class Main
{
    public static void main (String[] args)
            throws IOException, URISyntaxException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (line.length() == 0) {
                continue;
            }

            String[] array = line.split(";");

            URI u1;
            URI u2;
            try {
                u1 = new URI(array[0].trim());
                u2 = new URI(array[1].trim());
            } catch (URISyntaxException e) {
                System.out.println("False");
                continue;
            }

            // TODO finish
        }

        in.close();
    }
}
