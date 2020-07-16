package util;
import java.util.Random;

public class Probas {
	private static Random rand = new Random();
	
	public static int binom(int n, double d) {
		int r = 0;
		for (int k=0; k<n; k++) {
			if (rand.nextDouble()<d) {
				r++;
			}
		}
		return r;
	}
}
	
	
	
	
	
	
	
// �ventuellement utile si on fait des loi binomiales avec un n grand beaucoup de fois de suite
// Pour le cacul des cumulatives il faut d�volopper autour de l'esp�rence de la binomiale pour minimiser les erreurs
//	public TreeMap<IntFloat, ArrayList<Float>> cumulatives;
//	
//	public int binom(int n, float p) {
//		if (n<1) {
//			System.out.println("n doit �tre strictement positif");
//			return -1;
//		}
//		if (!(0<=p && p<=1)) {
//			System.out.println("p doit �tre entre 0 et 1");
//			return -1;
//		}
//		
//	}
//	
//	private void computeBoundBinom(int n, float p) {
//		ArrayList<Double> cumulativeLaw = new ArrayList<Double>();
//		Double bound = Math.pow(a, b);
//		for (int k=0; k<n; k++) {
//			
//		}
//	}
//	
//	private int dichotomicSearch() {
//		
//	}
//	
//	public int binomEq(int n, float p, int k) {
//		if (n<1) {
//			System.out.println("n doit �tre strictement positif");
//			return -1;
//		}
//		if (!(0<=p && p<=1)) {
//			System.out.println("p doit �tre entre 0 et 1");
//			return -1;
//		}
//		if (!(0<=k && k<=n)) {
//			System.out.println("k doit �tre compris entre 0 et n");
//			return -1;
//		}
