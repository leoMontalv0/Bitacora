package newpackage;

public class InterpolacionLineal {
    public static double interpolar(double x0, double y0, double x1, double y1, double x) {
        double m = (y1 - y0) / (x1 - x0);
        return y0 + m * (x - x0);
    }
}
