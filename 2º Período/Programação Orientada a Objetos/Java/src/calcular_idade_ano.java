import java.util.Scanner;

public class calcular_idade_ano {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o ano em que você nasceu :");
        int ano_nasc = scanner.nextInt();
        System.out.print("Digite o mês em que você nasceu: ");
        int mes_nasc = scanner.nextInt();
        System.out.print("Digite o ano atual: ");
        int ano_atual = scanner.nextInt();
        System.out.print("Digite o mês atual: ");
        int mes_atual = scanner.nextInt();
        int idade = (int) ((ano_atual-ano_nasc)*12+ mes_atual-mes_nasc)/12;
        System.out.println("Sua idade atual é de " + idade + " anos");

    }
}
