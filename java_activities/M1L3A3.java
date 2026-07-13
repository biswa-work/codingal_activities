import java.util.Scanner;
class M1L3A3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int marks = sc.nextInt();
        if (marks > 90)
            System.out.println("O");
        else if (marks > 80)
            System.out.println("A+");
        else if (marks > 70)
            System.out.println("A");
        else if (marks > 60)
            System.out.println("B");
        else
            System.out.println("C");
    }
}
