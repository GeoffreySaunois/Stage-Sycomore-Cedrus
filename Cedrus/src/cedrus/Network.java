package cedrus;
import java.util.ArrayList;

import util.*;

public class Network {
	ArrayList<User> users;
	private int averageConnections;
	public static int totalStake;
	public static int tau;
	public static int mu;
	
	
	public Network(int nUsers) {
		
		this.initialize();
	}
	
	private void initialize() {
		
	}
	
	public void transfertMessages() {
		double p = this.averageConnections / this.users.size();
		for(User u: this.users) {
			for (User v:this.users) {
				if (u.id!=v.id && Probas.binom(1, p)==1){
					u.collectMes(v);
				}
			}
		}
		for(User u: this.users) {
			u.swapMes();
		}
	}
	
}
