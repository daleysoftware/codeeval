public class SumOfPrimes
{
    public static void main (String[] args)
    {
        int sum = 0;
        int primesSummed = 0;
        int currentNumber = 2;

        while (primesSummed < 1000) {
            if (isPrime(currentNumber)) {
                sum += currentNumber;
                primesSummed++;
            }

            currentNumber++;
        }

        System.out.println(sum);
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
}
