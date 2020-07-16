package cedrus;
import java.util.*;

public class Block {
	public ArrayList<Boolean> index;
	public int height;					// this.height = this.predecessor.height + 1
	public int numberOfTransactions;
	public Block predecessor;			// Every block has a predecessor ; except the first bloc of the chain
	public ArrayList<Block> next;		// has 2 or less elements
	
	public Block() {
		
	}
}
