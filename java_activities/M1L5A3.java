import java.util.Scanner;
class M1L5A3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int n;
        do {
            n = sc.nextInt();
            if (n != 0) {
                if (n > max) max = n;
                if (n < min) min = n;
            }
        } while (n != 0);
        System.out.println("Maximum: " + max);
        System.out.println("Minimum: " + min);
    }
}
