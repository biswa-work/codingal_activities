class M1L4A1 {
    public static void main(String[] args) {
        boolean sunny = true;
        boolean cold = false;

        if (sunny) {
            if (cold)
                System.out.println("Wear a jacket");
            else
                System.out.println("Wear light clothes");
        } else {
            System.out.println("Carry an umbrella");
        }
    }
}
