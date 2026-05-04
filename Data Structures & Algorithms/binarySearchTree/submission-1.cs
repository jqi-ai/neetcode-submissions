class Node
{
    public int Key;
    public int Value;
    public Node Left;
    public Node Right;
    public Node(int key, int value, Node left, Node right)
    {
        this.Key = key;
        this.Value = value;
        this.Left = left;
        this.Right = right;
    }
}
class TreeMap {
    public Node Root;

    public TreeMap() {
        this.Root = null;
    }

    public void Insert(int key, int val) {
        if (this.Root == null)
        {
            this.Root = new Node(key, val, null, null);
        }
        else
        {
            this.InsertHelper(this.Root, key, val);
        }
    }

    private void InsertHelper(Node node, int key, int value)
    {
        if (key < node.Key)
        {
            if (node.Left == null)
            {
                node.Left = new Node(key, value, null, null);
            }
            else
            {
                this.InsertHelper(node.Left, key, value);
            }
        }
        else if (key > node.Key)
        {
            if (node.Right == null)
            {
                node.Right = new Node(key, value, null, null);
            }
            else
            {
                this.InsertHelper(node.Right, key, value);
            }
        }
        else
        {
            node.Value = value;
        }
    }

    public int Get(int key) {
        return this.GetHelper(this.Root, key);
    }
    private int GetHelper(Node node, int key)
    {
        if (node is null)
        {
            return -1;
        }
        if (key < node.Key)
        {
            return this.GetHelper(node.Left, key);
        }
        else if (key > node.Key)
        {
            return this.GetHelper(node.Right, key);
        }
        else 
        {
            return node.Value;
        }
    }

    public int GetMin() {
        if (this.Root == null)
        {
            return -1;
        }
        var node = this.FindMinNode(this.Root);
        return node.Value;
    }
    private Node FindMinNode(Node node)
    {
        while (node.Left != null)
        {
            node = node.Left;
        }
        return node;
    }

    public int GetMax() {
        if (this.Root == null)
        {
            return -1;
        }
        var node = this.FindMaxNode(this.Root);
        return node.Value;
    }
    private Node FindMaxNode(Node node)
    {
        while (node.Right != null)
        {
            node = node.Right;
        }
        return node;
    }

    public void Remove(int key) {
        this.Root = this.RemoveHelper(this.Root, key);
        return;
    }

    private Node RemoveHelper(Node node, int key)
    {
        if (node == null)
        {
            return null;
        }
        if (key < node.Key)
        {
            node.Left = this.RemoveHelper(node.Left, key);
        }
        else if (key > node.Key)
        {
            node.Right = this.RemoveHelper(node.Right, key);
        }
        else
        {
            if (node.Left == null && node.Right == null)
            {
                return null;
            }
            if (node.Left == null)
            {
                return node.Right;
            }
            if (node.Right == null)
            {
                return node.Left;
            }
            var minNode = this.FindMinNode(node.Right);
            node.Key = minNode.Key;
            node.Value = minNode.Value;
            node.Right = this.RemoveHelper(node.Right, minNode.Key);
        }
        return node;
    }

    public List<int> GetInorderKeys() {
        return this.Traversal(this.Root);
    }

    private List<int> Traversal(Node node)
    {
        if (node == null)
        {
            return [];
        }
        return this.Traversal(node.Left).Concat([node.Key]).Concat(this.Traversal(node.Right)).ToList();
    }
}
