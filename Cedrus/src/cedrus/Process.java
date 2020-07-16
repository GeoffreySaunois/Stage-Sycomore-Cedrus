package cedrus;

public class Process {
	Network network;
	int time;
	
	public static int maxNumberOfTransactions;
	
	public void transfertMessages() {
		this.network.transfertMessages();
		time++;
	}
}
