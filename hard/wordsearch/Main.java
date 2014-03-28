package codeeval.hard.wordsearch;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class Main
{
    private static final char[][] _grid =
            {
                    {'A', 'B', 'C', 'E'},
                    {'S', 'F', 'C', 'S'},
                    {'A', 'D', 'E', 'E'}
            };

    public static void main (String[] args)
            throws IOException
    {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;

        while ((line = in.readLine()) != null) {
            line = line.trim();

            if (hasMatchingWord(_grid, line.toCharArray())) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        }
    }

    private static boolean hasMatchingWord(char[][] grid, char[] word)
    {
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 5; col++) {
                if (hasMatchingWord(grid, word, 0, row, col)) {
                    return true;
                }
            }
        }

        return false;
    }

    private static boolean hasMatchingWord(char[][] grid, char[] word, int index,
                                           int row, int col)
    {
        if (row < 0 || row == 3 || col < 0 || col == 4) {
            return false;
        }

        return (grid[row][col] == word[index]) && ((index+1 == word.length) ||
                hasMatchingWord(grid, word, index+1, (row+1), (col)  ) ||
                hasMatchingWord(grid, word, index+1, (row-1), (col)  ) ||
                hasMatchingWord(grid, word, index+1, (row)  , (col-1)) ||
                hasMatchingWord(grid, word, index+1, (row)  , (col+1)));
    }
}
