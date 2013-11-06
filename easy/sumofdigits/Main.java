package codeeval.easy.sumofdigits;

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
            line = line.trim();

            if (line.length() > 0) {
                System.out.println(sumOfDigits(Integer.parseInt(line)));
            }
        }
    }

    public static int sumOfDigits(int n)
    {
        String nString = Integer.toString(n);
        int sum = 0;

        for (int i = 0; i < nString.length(); i++) {
            int digit = nString.charAt(i)-48;
            sum += digit;
        }

        return sum;
    }
}
