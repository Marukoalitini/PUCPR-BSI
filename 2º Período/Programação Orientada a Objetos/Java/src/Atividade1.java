import java.util.Random;
import java.util.Scanner;

public class Atividade1 {
    public static int[] retornarListaAleatoria(int tamanho){
        int[] lista = new int[tamanho];
        Random gerador = new Random();
        for (int i = 0; i < tamanho; i++){
            lista[i] = gerador.nextInt(0,1000);
        }
        return lista;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o tamanho da lista a ser criada");
        int tamanho = scanner.nextInt();
        int[] lista = retornarListaAleatoria(tamanho);
        for (int i = 0; i < lista.length; i++){
            if (lista[i] %3 == 0){
                System.out.println("O número " + lista[i] + " é divisível por 3.");
            }
            if (lista[i] % 2 == 0){
                System.out.println("O número " + lista[i] + " é par.");
            }
            else{
                System.out.println("O número " + lista[i] + " é impar.");
            }
        }
    }
}
