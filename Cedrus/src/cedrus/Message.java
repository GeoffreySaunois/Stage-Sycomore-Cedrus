package cedrus;

import java.util.ArrayList;

public class Message {
	public User user;
	public ArrayList<Boolean> blockIndex;
	public int round;
	public int vote;
//	public ArrayList<Integer> transactionsSet;  // In the case we want to study the agglomeration of transactions
	public TransactionsSet transactionsSet;
	public ArrayList<Message> history;  // Examine the relevance of this field ; maybe replace it by the hash of previous messages
//	public int id;
	
	
	public boolean roundEnded = false;
	
	public Message(User user, ArrayList<Integer> blockIndex, int round, int vote, int transactionSet, ArrayList<Message> history) {
		this.user = user;
		this.blockIndex = blockIndex;
		this.round = round;
		this.vote = vote;
		this.transactionsSet = new TransactionsSet(transactionSet);
		this.history = history;
//		this.computeId();
	}
	
//	private void computeId() {
//		this.id = this.user.hashCode();
//		this.id+= this.blockIndex.hashCode();
//		this.id+= (47*this.round + 11)*(17*this.transactionsSet.index + 37);
//		this.id+= this.history.hashCode();
//		
//		System.out.println(this.user.hashCode() +" "+ this.id);
//	}
	
}
