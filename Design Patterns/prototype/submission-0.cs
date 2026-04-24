public interface IShape {
    IShape Clone();
}

public class Rectangle : IShape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int GetWidth() {
        return this.width;
    }

    public int GetHeight() {
        return this.height;
    }

    public IShape Clone() {
        // Write your code here
        IShape newMe = new Rectangle(this.GetWidth(), this.GetHeight());
        return newMe;
    }
}

public class Square : IShape {
    private int length;

    public Square(int length) {
        this.length = length;
    }

    public int GetLength() {
        return this.length;
    }

    public IShape Clone() {
        // Write your code here
        IShape newMe = new Square(this.GetLength());
        return newMe;
    }
}

public class Test {
    public List<IShape> CloneShapes(List<IShape> shapes) {
        // Write your code here
        return shapes.Select(shape => shape.Clone()).ToList();
    }
}
