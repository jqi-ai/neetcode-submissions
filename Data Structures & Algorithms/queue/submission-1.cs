class Node {
    public int value;
    public Node prev;
    public Node next;
    public Node (int v, Node p, Node n)
    {
        this.value = v;
        this.prev = p;
        this.next = n;
    }
}
class Deque {
    public Node head;
    public Node tail;
    public Deque() {
        this.head = null;
        this.tail = null;
    }

    public bool isEmpty() {
        return this.head == null && this.tail == null; 
    }

    public void append(int value) {
        if (this.tail == null)
        {
            this.tail = new Node(value, null, null);
            this.head = this.tail;
        }
        else
        {
            var newTail = new Node(value, this.tail, null);
            this.tail.next = newTail;
            this.tail = newTail;
        }
        return;
    }

    public void appendleft(int value) {
        if (this.head == null)
        {
            this.head = new Node(value, null, null);
            this.tail = this.head;
        }
        else
        {
            var newHead = new Node(value, null, this.head);
            this.head.prev = newHead;
            this.head = newHead;
        }
        return;
    }

    public int pop() {
        if (this.tail == null)
        {
            return -1;
        }
        var res = this.tail;
        var prev = this.tail.prev;
        if (prev == null)
        {
            this.head = null;
            this.tail = null;
        }
        else 
        {
            this.tail = prev;
            this.tail.next = null;
        }
        return res.value;
    }

    public int popleft() {
        if (this.head == null)
        {
            return -1;
        }
        var res = this.head;
        var next = this.head.next;
        if (next == null)
        {
            this.head = null;
            this.tail = null;
        }
        else 
        {
            this.head = next;
            this.head.prev = null;
        }
        return res.value;
    }
}
