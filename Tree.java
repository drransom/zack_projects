import java.util.*;

public class Tree<v> {
  Node<v> root;
  public Tree() {
    root = new Node<v>();
  }

  public Tree(ArrayList<Pair<v>> pairsIn) {
    root = new Node<v>();
    for (int i = 0; i < pairsIn.size(); i++) {
      insert(pairsIn.get(i).key, pairsIn.get(i).val);
    }
  }

  public void insert(Integer keyIn, v valIn) {
    if (root.val == null) {
      root.setKey(keyIn);
      root.setValue(valIn);
    } else {
      root.insert(keyIn, valIn);
    }
  }

  public void printTree() {
    root.printSubtree();
  }

  public Integer size() {
    return root.size();
  }

  public Boolean includesValue(v valIn) {
    return root.includesValue(valIn);
  }

  public Boolean includesKey(Integer keyIn) {
    return root.includesKey(keyIn);
  }

  public v getValueAt(Integer keyIn) {
    return root.getValueAt(keyIn);
  }

  public class Node<v> {
    Integer key = 0;
    v val = null;
    Node<v> left = null;
    Node<v> right = null;
    public Node() {};
    public Node(Integer keyIn, v valIn) {
      key = keyIn;
      val = valIn;
    }

    public void setKey(Integer keyIn) {
      key = keyIn;
    }

    public void setValue(v valIn) {
      val = valIn;
    }

    public void insert(Integer keyIn, v valIn) {
      if (key == keyIn) {
        return;
      }
      else if (keyIn < key) {
        if (left == null) {
          left = new Node<v>(keyIn, valIn);
        }
        else {
          left.insert(keyIn, valIn);
        }
      }
      else {
        if (right == null) {
          right = new Node<v>(keyIn, valIn);
        }
        else {
          right.insert(keyIn, valIn);
        }
      }
    }
    public Integer size() {
      Integer localSize = 1;
      if (left != null) {
        localSize += left.size();
      }
      if (right != null) {
        localSize += right.size();
      }
      return localSize;
    }

    public boolean includesValue(v valIn) {
      if (val == valIn) {
        return true;
      }
      else if (left != null && left.includesValue(valIn)) {
        return true;
      }
      else if (right != null && right.includesValue(valIn)) {
        return true;
      }
      return false;
    }

    public boolean includesKey(Integer keyIn) {
      if (key == keyIn) {
        return true;
      }
      else if (key > keyIn) {
        return (left != null && left.includesKey(keyIn));
      }
      else {
        return (right != null && right.includesKey(keyIn));
      }
    }

    public v getValueAt(Integer keyIn) {
      if (key == keyIn) {
        return val;
      }
      else if (key > keyIn) {
        if (left != null) {
          return left.getValueAt(keyIn);
        }
        else {
          return null;
        }
      }
      else {
        if (right != null) {
          return right.getValueAt(keyIn);
        }
        else {
          return null;
        }
      }
    }

    public void printSubtree() {
      if (left != null) {
        left.printSubtree();
      }
      System.out.println(val);
      if (right != null) {
        right.printSubtree();
      }
    }
  }
}
