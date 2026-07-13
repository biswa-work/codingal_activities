import java.util.Scanner;

class M1L6A1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean prime = n > 1;

        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                prime = false;
                break;
            }
        }

        System.out.println(prime ? "prime" : "not prime");
    }
}