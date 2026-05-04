public class Node {
    public Node next;
    public int value;
    public Node(int v, Node n) {
        this.value = v;
        this.next = n;
    }
}
public class LinkedList {
    Node head;
    public LinkedList() {
        this.head = null;
    }

    public int Get(int index) {
        var node = this.head;
        while (node != null && index > 0) {
            node = node.next;
            index -= 1;
        }
        if (index > 0 || node == null) {
            return -1;
        }
        return node.value;
    }

    public void InsertHead(int val) {
        var newHead = new Node(val, this.head);
        this.head = newHead;
        return;
    }

    public void InsertTail(int val) {
        if (this.head == null) {
            this.head = new Node(val, null);
            return;
        }
        var node = this.head;
        while (node.next != null) {
            node = node.next;
        }
        node.next = new Node(val, null);
        return;
    }

    public bool Remove(int index) {
        if (this.head == null) return false;
        if (index == 0) {
            this.head = this.head.next;
            return true;
        }
        var node = this.head;
        while (index > 1 && node.next != null) {
            index -= 1;
            node = node.next;
        }
        if (node.next == null) {
            return false;
        }
        node.next = node.next.next;
        return true;
    }

    public List<int> GetValues() {
        var node = this.head;
        var values = new List<int>();
        while (node != null) {
            values.Add(node.value);
            node = node.next;
        }
        return values;
    }
}