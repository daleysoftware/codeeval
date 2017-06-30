public class PrimePalindrome
{
    public static void main (String[] args)
    {
        int largestPrimePalindrome = 2;

        // 1 is not prime.
        for (int i = 3; i < 1000; i++) {
            if (isPrime(i) && isPalindrome(i)) {
                largestPrimePalindrome = i;
            }
        }

        System.out.println(largestPrimePalindrome);
    }

    public static boolean isPrime(int n)
    {
        int root = (int) Math.sqrt(n);

        for (int i = 2; i <= root; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static boolean isPalindrome(int n)
    {
        String str = Integer.toString(n);
        return isPalindrome(str);
    }

    public static boolean isPalindrome(String str)
    {
        char[] array = str.toCharArray();

        for (int i = 0; i < array.length/2; i++) {
            if (array[i] != array[array.length-i-1]) {
                return false;
            }
        }

        return true;
    }
}
