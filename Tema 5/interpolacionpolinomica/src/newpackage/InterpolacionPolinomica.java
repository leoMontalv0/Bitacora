
package newpackage;

public class InterpolacionPolinomica {
    public static void main(String[] args) {
        // Valores conocidos (x, y)
        double[] x = {1, 2, 4};
        double[] y = {1, 8, 64};

        // Valor donde se desea interpolar
        double xBuscado = 3;

        // Valor real conocido en x = 3 (si lo sabemos, por ejemplo si f(x)=x^2)
        double valorReal = 9;  // porque 3^2 = 9

        // Resultado de la interpolación
        double resultado = interpolarPolinomio(x, y, xBuscado);

        // Mostrar resultado
        System.out.printf("Valor interpolado en x = %.1f: %.4f\n", xBuscado, resultado);

        // Calcular y mostrar cuota de error
        double error = calcularError(valorReal, resultado);
        System.out.printf("Cuota de error estimada: %.4f\n", error);

        // Mostrar los puntos usados
        System.out.println("\nPuntos utilizados:");
        for (int i = 0; i < x.length; i++) {
            System.out.printf("x = %.1f, y = %.1f\n", x[i], y[i]);
        }
    }

    // Método de interpolación de Lagrange
    public static double interpolarPolinomio(double[] x, double[] y, double xBuscado) {
        double resultado = 0;

        for (int i = 0; i < x.length; i++) {
            double termino = y[i];

            for (int j = 0; j < x.length; j++) {
                if (j != i) {
                    termino *= (xBuscado - x[j]) / (x[i] - x[j]);
                }
            }

            resultado += termino;
        }

        return resultado;
    }

    // Método para calcular el error absoluto
    public static double calcularError(double valorReal, double valorInterpolado) {
        return Math.abs(valorReal - valorInterpolado);
    }

}
