import java.util.Scanner;
class M1L2ACP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        System.out.println((year % 400 == 0 || year % 4 == 0 && year % 100 != 0) ? "Leap Year" : "Not Leap Year");
    }
}
