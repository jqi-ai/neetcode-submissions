public class MinHeap {
    private List<int> _heap { get; set; }
    public MinHeap() {
        this._heap = [];
    }
    private void BubbleUp(int index)
    {
        var parent = (int)Math.Floor((double)(index - 1) / 2);
        while (index > 0 && this._heap[parent] > this._heap[index])
        {
            var tmp = this._heap[parent];
            this._heap[parent] = this._heap[index];
            this._heap[index] = tmp;
            index = parent;
            parent = (int)Math.Floor((double)(index - 1) / 2);
        }
        return;
    }
    private void BubbleDown(int index){
        var child = 2 * index + 1;
        while (child < this._heap.Count)
        {
            if (child + 1 < this._heap.Count && this._heap[child] > this._heap[child + 1])
            {
                child += 1;
            }
            if (this._heap[child] >= this._heap[index])
            {
                break;
            }
            var tmp = this._heap[child];
            this._heap[child] = this._heap[index];
            this._heap[index] = tmp;
            index = child;
            child = 2 * index + 1;
        }
    }

    public void Push(int val) {
        this._heap.Add(val);
        this.BubbleUp(this._heap.Count - 1);
        return;
    }

    public int? Pop() {
        if (this._heap.Count <= 0)
        {
            return -1;
        }
        if (this._heap.Count == 1)
        {
            var res = this._heap[0];
            this._heap.RemoveAt(0);
            return res;
        }
        var root = this._heap[0];
        this._heap[0] = this._heap[this._heap.Count - 1];
        this._heap.RemoveAt(this._heap.Count - 1);
        this.BubbleDown(0);
        return root;
    }

    public int? Top() {
        if (this._heap.Count > 0) 
        {
            return this._heap[0];
        }
        return -1;
    }

    public void Heapify(List<int> nums) {
        this._heap = nums;
        foreach (int i in Enumerable.Range(0, (int)Math.Floor((double)this._heap.Count / 2)).Reverse())
        {
            this.BubbleDown(i);
        }
    }

}