package codeeval.moderate.detectingcycles;

import java.io.*;
import java.util.*;

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

            String[] lineArray = line.split(" ");
            int[] sequence = new int[lineArray.length];

            //System.out.println(">>> " + line);
            for (int i = 0; i < sequence.length; i++) {
                sequence[i] = Integer.parseInt(lineArray[i]);
            }

            // Need to remove duplicates, since the tortoise and the hare algorithm does
            // not handle them properly.
            int[] noDuplicatesSequence = new int[sequence.length];
            int[] elementFrequency = new int[sequence.length];

            int currentElement = 0;

            noDuplicatesSequence[0] = sequence[0];
            elementFrequency[0] = 1;

            for (int i = 1; i < sequence.length; i++) {
                int current = sequence[i];

                if (current == noDuplicatesSequence[currentElement]) {
                    elementFrequency[currentElement]++;
                } else {
                    currentElement++;
                    noDuplicatesSequence[currentElement] = current;
                    elementFrequency[currentElement] = 1;
                }
            }

            /*for (int i = 0; i < noDuplicatesSequence.length; i++) {
                System.out.println(noDuplicatesSequence[i] + " " + elementFrequency[i]);
            }*/

            CycleInformation ci = detectFirstCycle(
                    noDuplicatesSequence,
                    currentElement+1);

            if (ci == null) {
                // No repeating sequence. It must be the corner case where the last digit
                // is repeated.
                System.out.println(noDuplicatesSequence[currentElement]);
                continue;
            }

            for (int i = 0; i < ci.cycleLength(); i++) {
                int index = ci.startingPoint() + i;

                int current = noDuplicatesSequence[index];
                int frequency = elementFrequency[index];

                for (int j = 0; j < frequency; j++) {
                    System.out.print(current);

                    if (j != frequency - 1) {
                        System.out.print(" ");
                    }
                }

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
     *
     * See Wikipedia's description of the tortoise and the hare algorithm:
     * http://en.wikipedia.org/wiki/Floyd%27s_cycle-finding_algorithm#Tortoise_and_hare
     *
     * N.B. cannot have any repeated elements in the sequence.
     *
     * @return A pair containing two integers: mu and lambda. Mu is the starting position
     * of the cycle and lambda is the length of the cycle.
     */
    public static CycleInformation detectFirstCycle(int[] sequence, int length)
    {
        // Dump the sequence into a hash map to serve as the function f().
        HashMap<Integer, Integer> f = new HashMap<Integer, Integer>();

        for (int i = 1; i < length; i++) {
            f.put(sequence[i-1], sequence[i]);
        }

        // Standard tortoise and hare algorithm follows.
        int tortoise = f.get(sequence[0]);
        if (!f.containsKey(tortoise)) {
            return null;
        }
        int hare = f.get(tortoise);

        while (tortoise != hare) {
            tortoise = f.get(tortoise);

            // Watch for the case when we reach the end of the sequence and we haven't
            // found a repeating pattern.
            if (!f.containsKey(hare)) {
                return null;
            } else {
                hare = f.get(hare);

                if (!f.containsKey(hare)) {
                    return null;
                }

                hare = f.get(hare);
            }
        }

        int mu = 0;
        tortoise = sequence[0];
        while (tortoise != hare) {
            tortoise = f.get(tortoise);
            hare = f.get(hare);
            mu++;
        }

        int lambda = 1;
        hare = f.get(tortoise);
        while (tortoise != hare) {
            hare = f.get(hare);
            lambda++;
        }

        // starting point, length == mu, lambda.
        return new CycleInformation(mu, lambda);
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
