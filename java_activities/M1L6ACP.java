import java.util.Scanner;
class M1L6ACP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int digits = String.valueOf(n).length();
        k = k % digits;
        int divisor = (int)Math.pow(10, k);
        int rotated = (n % divisor) * (int)Math.pow(10, digits - k) + n / divisor;
        System.out.println(rotated);
    }
}
