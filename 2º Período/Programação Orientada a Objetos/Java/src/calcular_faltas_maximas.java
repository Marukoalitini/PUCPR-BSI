import java.util.Scanner;

public class calcular_faltas_maximas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Insira a quantidade de aulas de PO totais do semestre: ");
        int aulas_totais = scanner.nextInt();
        int faltas_maximas = (int) (aulas_totais * 0.25);
        System.out.println("A quantidade máxima de faltas que você pode ter esse semestre em PO é de: " + faltas_maximas);


    }
}
