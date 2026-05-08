public class Graph {
    private Dictionary<int, HashSet<int>> _g;
    public Graph() {
        this._g = new();
    }

    public void AddEdge(int src, int dst) {
        if (!this._g.ContainsKey(src) )
        {            this._g[src] = new();
        }
        if (!this._g.ContainsKey(dst))
        {            this._g[dst] = new();
        }
        this._g[src].Add(dst);
        return;
    }

    public bool RemoveEdge(int src, int dst) {
        if (!this._g.ContainsKey(src) || !this._g.ContainsKey(dst))
        {            return false;
        }
        return this._g[src].Remove(dst);
    }

    public bool HasPath(int src, int dst) {
        var visited = new HashSet<int>();
        return this.Dfs(src, dst, visited);
    }

    private bool Dfs(int src, int dst, HashSet<int> visited)
    {
        if (src == dst)
        {
            return true;
        }
        visited.Add(src);
        foreach (var neighbor in (this._g[src]))
        {
            if (!visited.Contains(neighbor) )
            {
                if (this.Dfs(neighbor, dst, visited))
                {
                    return true;
                }
            }
        }
        return false;
    }

}
