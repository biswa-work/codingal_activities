import java.io.File;

public class Main {
    public static void main(String[] args) {
        File folder = new File(".");
        
        for (String file : folder.list()) {
            System.out.println(file);
        }
    }
}