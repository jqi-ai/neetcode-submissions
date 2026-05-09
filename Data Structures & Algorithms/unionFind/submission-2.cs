public class UnionFind {
    private List<int> _parent;
    private List<int> _rank;
    private int _num;

    public UnionFind(int n) {
        this._parent = Enumerable.Range(0, n).ToList();
        this._rank = Enumerable.Repeat(0, n).ToList();
        this._num = n;
    }

    public int Find(int x) {
        if (this._parent[x] != x)
        {
            this._parent[x] = this.Find(this._parent[x]);
        }
        return this._parent[x];
    }

    public bool IsSameComponent(int x, int y) {
        return this.Find(x) == this.Find(y);
    }

    public bool Union(int x, int y) {
        var rootX = this.Find(x);
        var rootY = this.Find(y);
        if (rootX == rootY)
        {
            return false;
        }
        if (this._rank[rootX] < this._rank[rootY])
        {
            this._parent[rootX] = rootY;
        }
        else if (this._rank[rootY] < this._rank[rootX])
        {
            this._parent[rootY] = rootX;
        }
        else
        {
            this._parent[rootY] = rootX;
            this._rank[rootX] += 1;
        }
        this._num -= 1;
        return true; 
    }

    public int GetNumComponents() {
        return this._num;
    }
}