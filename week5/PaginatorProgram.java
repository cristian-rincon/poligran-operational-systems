import java.util.Scanner;
public class PagMemoria {
    String[] memoriatotal = new String[100];.
    private Scanner teclado;
    public int[] vec;
    private Scanner
    let;
    private String letra;
    public void cargar() {
        teclado = new Scanner(System.in);
        let = new Scanner(System.in);
        System.out.println("Digite el nombre del proceso");
        letra =
            let.next();
        System.out.print("Digite el tamaño del proceso:");
        int n;
        n = teclado.nextInt();
        vec = new int[n];
        System.out.println("el proceso ocupa " + n + " espacios de memoria");
        for (int f = 0; f < vec.length; f++) {
            System.out.println(letra);
        }
    }
    public void acumularmemoriatotal();
    int suma = 0; //
    for (int f = 0; f < vec.length; f++) {
        suma = suma + vec[f];
    }
    System.out.println(" Los espacios de memoria utilizados son:" + suma);
}
}
public static void main(String[] ar) {
    PagMemoria m = new PagMemoria();
    m.cargar();
    m.acumularEnMemoriaTotal();
}
}
