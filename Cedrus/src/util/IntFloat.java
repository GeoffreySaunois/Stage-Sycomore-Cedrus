package util;

import java.util.Comparator;


public class IntFloat {
	public Integer n;
	public Float p;
	
	
	public static Comparator<IntFloat> sortByCoordinates = new Comparator<IntFloat>() {
		@Override
		public int compare(IntFloat u, IntFloat v) {
			if(u.p!=v.p) {
				return Float.compare(u.p, v.p);
			}
			else {
				return u.n-v.n;
			}
		}
	};
}
