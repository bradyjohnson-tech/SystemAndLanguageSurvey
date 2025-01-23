public class Main {
    public static void main(String[] args) { // In the C++ code the main method is not static which makes it a global method.
        // But being that this is Java we need a static entry-point. Further I do not think you will be testing multi-threading
        // scenarios that scale so this difference should not have an impact. If we did, I would still start from main, but I
        // would call from a task handler that would start and wait for tasks to finish.
        try {
            int number = 0;
            cinEmulator cinEmulator = new cinEmulator();

            do {
                System.out.print("Enter a positive number (0 or negative to exit): ");
                number = cinEmulator.handleInput();

                if (number <= 0) {
                    break;
                }
                if (isPrime(number)) {
                    System.out.println(number + " is a prime number.");
                } else {
                    System.out.println(number + " is not a prime number.");
                }
            } while (true);
        }finally {
            System.exit(0);  // This line makes me cringe.
        }
    }

    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }










}