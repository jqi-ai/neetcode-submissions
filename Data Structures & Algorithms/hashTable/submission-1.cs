public class Node {
    public int Key;
    public int Value;
    public Node Next;
    public Node(int k, int v, Node n = null) {
        this.Key = k;
        this.Value = v;
        this.Next = n;
    }
}
public class HashTable {
    private int capacity;
    private int size;
    private List<Node> table;
    public HashTable(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.table = new List<Node>(Enumerable.Repeat<Node>(null, capacity));
    }
    private int Hash(int key) {
        return key % this.capacity;
    }

    public void Insert(int key, int value) {
        var hash = this.Hash(key);
        var head = this.table[hash];
        while (head != null) {
            if (head.Key == key) {
                head.Value = value;
                return;
            }
            head = head.Next;
        }
        var newNode = new Node(key, value, this.table[hash]);
        this.table[hash] = newNode;
        this.size += 1;
        if ((double)this.size / this.capacity >= 0.5) {
            this.Resize();
        }
        return;
    }

    public int Get(int key) {
        var hash = this.Hash(key);
        var head = this.table[hash];
        while (head != null){
            if (head.Key == key) {
                return head.Value;
            }
            head = head.Next;
        }
        return -1;
    }

    public bool Remove(int key) {
        var hash = this.Hash(key);
        var head = this.table[hash];
        if (head != null && head.Key == key)
        {
            this.table[hash] = head.Next;
            this.size -= 1;
            return true;
        }
        while (head?.Next != null)
        {
            if (head.Next.Key == key)
            {
                head.Next = head.Next.Next;
                this.size -= 1;
                return true;
            }
            head = head.Next;
        }
        return false;
    }

    public int GetSize() { return this.size; }

    public int GetCapacity() { return this.capacity; }

    public void Resize() {
        var oldTable = this.table;
        this.capacity *= 2;
        this.size = 0;
        this.table = new List<Node>(Enumerable.Repeat<Node>(null, capacity));
        foreach (var head in oldTable)
        {
            var node = head;
            while (node != null)
            {
                this.Insert(node.Key, node.Value);
                node = node.Next;
            }
        }
        return;
    }
}
