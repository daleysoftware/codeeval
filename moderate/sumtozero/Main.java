package codeeval.moderate.sumtozero;

import java.io.*;
import java.util.*;

// TODO (MP) this is breaking the memory limit. Needs improvement.
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

            String[] sArray = line.split(",");
            int[] iArray = new int[sArray.length];

            for (int i = 0; i < iArray.length; i++) {
                iArray[i] = Integer.parseInt(sArray[i]);
            }

            Set<int[]> set = findCombinations(iArray, 4);

            int count = 0;
            for (int[] array : set) {
                int sum = 0;
                for (int i : array) {
                    sum += i;
                }

                if (sum == 0) {
                    count++;
                }
            }

            System.out.println(count);
        }

        in.close();
    }

   /**
    * Given an array of a particular length, choose length elements and form the set of
    * possible combinations.
    *
    * Implementation:
    *
    * After finding all permutations of the given array for the given length, add those
    * elements to a hash set. Exclude certain permuations based the hash code.
    *
    * This is perhaps not the most efficient implementation, but it is simple and easy to
    * code.
    */
   private static Set<int[]> findCombinations(int[] array, int length)
   {
       Map<Integer, IntegerArray> working = new HashMap<Integer, IntegerArray>();
       findCombinations(array, 0, length, working);

       Set<int[]> result = new HashSet<int[]>();

       for (int key : working.keySet()) {
           IntegerArray value = working.get(key);
           result.add(value._array);
       }

       return result;
   }

   private static void findCombinations(int[] array, int index, int length,
                                        Map<Integer, IntegerArray> result)
   {
       if (index == length) {
           IntegerArray ia = new IntegerArray(Arrays.copyOfRange(array, 0, length));
           int hashCode = ia.hashCode();

           if (!result.containsKey(hashCode)) {
               result.put(hashCode, ia);
           }

           return;
       }

       for (int i = index; i < array.length; i++) {
           swap(array, i, index);
           findCombinations(array, index+1, length, result);
           swap(array, i, index);
       }
   }

   private static void swap(int[] array, int index1, int index2)
   {
       int tmp = array[index1];
       array[index1] = array[index2];
       array[index2] = tmp;
   }

    /**
     * A class that represents an integer array. Implements various comparision functions
     * used for hashing.
     */
    private static class IntegerArray implements Comparable<IntegerArray>
    {
        private final int[] _array;

        public IntegerArray(int[] array)
        {
            Arrays.sort(array);
            _array = array;
        }

        @Override
        public int hashCode()
        {
            return toString().hashCode();
        }

        @Override
        public String toString()
        {
            StringBuilder sb = new StringBuilder();

            for (int i : _array) {
                sb.append(Integer.toString(i));
            }

            return sb.toString();
        }

        @Override
        public int compareTo(IntegerArray array)
        {
            return array.hashCode() == hashCode() ? 0 : -1;
        }
    }
}
