public class DynamicArray {
    private List<int> _array;
    private int _size;
    private int _capacity;
    
    public DynamicArray(int capacity) {
        this._array = new List<int>(capacity);
        this._size = 0;
        this._capacity = capacity;
    }

    public int Get(int i) {
        return this._array[i];
    }

    public void Set(int i, int n) {
        this._array[i] = n;
        return;
    }

    public void PushBack(int n) {
        if (this._size == this._capacity)
        {
            this.Resize();
        }
        this._array.Add(n);
        this._size += 1;
        return;
    }

    public int PopBack() {
        if (this._array.Count <= 0)
        {
            return -1;
        }
        var poped = this._array[this._array.Count - 1];
        this._array.RemoveAt(this._array.Count - 1);
        this._size -= 1;
        return poped;
    }

    private void Resize() {
        this._capacity = 2 * this._capacity;
        var _array_new = new List<int>(this._capacity);
        _array_new.AddRange(this._array);
        this._array = _array_new;
    }

    public int GetSize() {
        return this._size;
    }

    public int GetCapacity() {
        return this._capacity;
    }
}
