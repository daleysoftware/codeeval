import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class DetectingCycles
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

            String[] lineArray = line.split(" ");
            int[] sequence = new int[lineArray.length];

            for (int i = 0; i < sequence.length; i++) {
                sequence[i] = Integer.parseInt(lineArray[i]);
            }

            CycleInformation ci = detectFirstCycle(sequence);

            for (int i = 0; i < ci.cycleLength(); i++) {
                System.out.print(sequence[ci.startingPoint() + i]);

                if (i != ci.cycleLength() - 1) {
                    System.out.print(" ");
                }
            }

            System.out.println();
        }

        in.close();
    }

    /**
     * Detect the first cycle in the given sequence.
     */
    public static CycleInformation detectFirstCycle(int[] sequence)
    {
        for (int starting = 0; starting < sequence.length-1; starting++) {
            for (int length = 1; length < sequence.length; length++) {
                if (isValidCycle(sequence, starting, length)) {
                    return new CycleInformation(starting, length);
                }
            }
        }

        return new CycleInformation(0, sequence.length);
    }

    private static boolean isValidCycle(int[] sequence, int starting, int length)
    {
        int current = starting + length;
        boolean foundMatch = false;

        while (current < sequence.length) {
            if (!subArraysMatch(sequence, starting, current, length)) {
                return false;
            }

            foundMatch = true;
            current += length;
        }

        return foundMatch;
    }

    private static boolean subArraysMatch(int[] sequence, int startingA, int startingB,
                                          int length)
    {
        for (int i = 0; i < length; i++) {
            int indexA = startingA + i;
            int indexB = startingB + i;

            if (indexA >= sequence.length || indexB >= sequence.length) {
                return false;
            }

            if (sequence[indexA] != sequence[indexB]) {
                return false;
            }
        }

        return true;
    }

    /**
     * Could use Sun's pair class instead, but CodeEval doesn't support that.
     */
    private static class CycleInformation
    {
        private final int _startingPoint;
        private final int _cycleLength;

        public CycleInformation(int startingPoint, int cycleLength)
        {
            _startingPoint = startingPoint;
            _cycleLength = cycleLength;
        }

        public int startingPoint()
        {
            return _startingPoint;
        }

        public int cycleLength()
        {
            return _cycleLength;
        }
    }
}
