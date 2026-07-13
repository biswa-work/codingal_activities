import java.util.Scanner;
class M1L4ACP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rating = sc.nextInt();
        if (rating >= 8)
            System.out.println("Excellent");
        else if (rating >= 5)
            System.out.println("Good");
        else
            System.out.println("Poor");
    }
}
