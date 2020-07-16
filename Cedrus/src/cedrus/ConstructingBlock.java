package cedrus;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;

import util.Probas;

public class ConstructingBlock extends Block{
	
	
	public ArrayList<Message> newMessages;
	public ArrayList<Message> toSendMessages;
	public LinkedHashSet<Message> alreadySeen;
	public LinkedHashMap<Integer, Integer> weightPerTransaction; // The key (Integer) is the transaction index
	public ArrayList<Integer> votePerRound;
	
	//public TreeMap<Integer, User> validPreviousCommitee; Simulation without malicious nodes
	//public TreeMap<Integer, User> maliciousUsers;	
	
	public ConstructingBlock() {
		super();
		
	}
	
	private void computeVoteUntil(int n, int userStake) {
		while(this.votePerRound.size()<n) {
			this.votePerRound.add(Probas.binom(userStake, Network.tau / Network.totalStake));
		}
	}
	
	public void analyseMess() {		// Analyse every new messages received
		
	}
	
	public void swapMess() {
		this.toSendMessages = this.newMessages;
		this.newMessages = new ArrayList<Message>();
	}
}
