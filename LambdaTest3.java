public class LambdaTest3 {
    private static void main(String [] args) {
        Operaciones op = (num1, num2) -> System.out.println(num1 + num2);
        LambdaTest3 objeto = new LambdaTest3();
        objeto.miMetodo (op, 10 10);

    }
    public void miMetodo (Operaciones op, int num1,int num2){
        op.ImprimirSuma(num1, num2);
    }
}
