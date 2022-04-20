public class LambdaTest2 {
  public static void main (String [] args){
      Operaciones op = (num1, num2) -> System.out.println(num1 + num2);
      op.ImprimirSuma(5, 10);
  }  
}
