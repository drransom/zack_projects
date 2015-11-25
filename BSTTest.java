import java.util.*;

public class BSTTest {
  public static void main(String[] args) {
    Pair<Integer> pair;
    Integer sign;
    ArrayList<Pair<Integer>> pairList = new ArrayList<Pair<Integer>>();
    for (int i = 0; i < 2000; i++) {
      sign = i % 2 == 0 ? -1 : 1;
      pair = new Pair<Integer>(i, sign * i);
      pairList.add(pair);
    }
    Tree<Integer> myTree = new Tree<Integer>(pairList);
    // Tree<Integer> myTree = new Tree<Integer>();
    // myTree.insert(8, 5);
    // myTree.insert(2, 7);
    // System.out.println(myTree.getValueAt(8));
    // System.out.println(myTree.getValueAt(2));
    // System.out.println(myTree.size());
    // System.out.println(myTree.includesValue(6));
    // System.out.println(myTree.includesValue(0));
    myTree.printTree();
  }
}
