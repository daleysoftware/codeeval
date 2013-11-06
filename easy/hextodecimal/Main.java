package codeeval.easy.hextodecimal;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            String[] lineArray = line.split(" ");
            if (lineArray.length > 0) {
                String hex = lineArray[0];
                System.out.println(hexToDecimalInteger(hex));
            }
        }
    }

    public static int hexToDecimalInteger(String hex)
    {
        return Integer.parseInt(hex, 16);
    }
}