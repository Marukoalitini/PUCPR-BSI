import java.util.Scanner;

public class calcular_idade_meses {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Insira sua Idade");
        int idade = scanner.nextInt();
        int idade_em_meses = 12 * idade;
        System.out.println("Sua idade em meses é de: " + idade_em_meses + " meses.");
    }
}
