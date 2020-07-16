package cedrus;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.TreeMap;

public class Blockchain {
	// Obviously each user has his personal blockchain, kepp in mind that there is no "global" blockchain
	
	// Implémenter une nouvelle collection pour hierarchiser les blocks ?
	
	
	TreeMap<ArrayList<Boolean>, ConstructingBlock> contructingBlocks; // The key is the block index
	
	public void swapMes() {
		for(ConstructingBlock cb:this.contructingBlocks.values()) {
			cb.swapMess();
		}
	}
	
	public void analyseMess() {
		for(ConstructingBlock cb: this.contructingBlocks.values()) {
			cb.analyseMess();
		}
	}
	
	
}
