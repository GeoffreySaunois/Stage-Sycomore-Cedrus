package cedrus;
import java.util.*;
import util.*;

public class User {
	
	public int id;
	public int stake;
	public Blockchain blockchain;
	

	
	public User() {
		
	}
	
	public void collectMes(User u) {
		Iterator<ConstructingBlock> maCol = this.blockchain.contructingBlocks.values().iterator();
		Iterator<ConstructingBlock> pasMaCol = u.blockchain.contructingBlocks.values().iterator();
		while(maCol.hasNext()&&pasMaCol.hasNext()) {
			ConstructingBlock cb = maCol.next();
			ConstructingBlock cb2 = pasMaCol.next();
			
			if(cb.height==cb2.height) {
				for(Message m: cb2.toSendMessages) {
					if(!cb.alreadySeen.contains(m)) {
						cb.alreadySeen.add(m);
						cb.newMessages.add(m);
					}
				}
				continue;
			}
			if(cb.height>cb2.height) {
				// The message concerns a past block, we don't take it into account.
				continue;
			}
			if(cb.height<cb2.height) {
				//Trouble's starting
				//Ok : on remonte la chain de block jusqu'à h = cb.height+1, plus on fait cb.next = monBlock.deepcopy();
				//Puis faut actualiser les leafBlocks
				//Puis faut ajouter les messages de toSend
			}

		}
	}
	
	public void swapMess() {
		this.blockchain.swapMes();
	}
	
	/*
	 * Doit :
	 * Ajouter le nouveau block à la blockchain
	 * Regarder les conditions split / merge
	 * Créer les constructingBlocks correspondants
	 */
	public void addNewBlock(Block b) {

	}
	
	public void addNewContructingBlock() {
		
	}
	
//	public void analyseMess() {
//		
//	}
	
	
	public void addBlock(Message m) {
		
	}
}
