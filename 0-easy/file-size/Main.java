import java.io.IOException;
import java.io.File;

public class Main
{
    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        System.out.println(file.length());
    }
}
