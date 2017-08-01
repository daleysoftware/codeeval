import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Iterator;
import java.util.LinkedList;

class ColumnNames
{
    public static void main(String[] args) throws Exception
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            int number = Integer.parseInt(line.trim());
            System.out.println(convertToExcelColumnName(number));
        }

        in.close();
    }

    private static final int OFFSET = (int) 'A';

    private static String convertToExcelColumnName(int number)
    {
        number--;
        LinkedList<Character> result = new LinkedList<>();

        while (number >= 0) {
            int quotient = number / 26;
            int remainder = number % 26;
            result.add((char) (OFFSET + remainder));
            number = quotient - 1;
        }

        StringBuilder sb = new StringBuilder();

        Iterator it = result.descendingIterator();
        while(it.hasNext()){
            sb.append(it.next());
        }

        return sb.toString();
    }
}
