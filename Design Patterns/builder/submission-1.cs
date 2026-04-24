public class Meal {
    private double cost;
    private bool takeOut;
    private string main;
    private string drink;

    public double getCost() {
        return this.cost;
    }

    public bool getTakeOut() {
        return this.takeOut;
    }

    public string getMain() {
        return this.main;
    }

    public string getDrink() {
        return this.drink;
    }

    public void setCost(double cost) {
        this.cost = cost;
    }

    public void setTakeOut(bool takeOut) {
        this.takeOut = takeOut;
    }

    public void setMain(string main) {
        this.main = main;
    }

    public void setDrink(string drink) {
        this.drink = drink;
    }
}

public class MealBuilder {

    Meal meal;
    public MealBuilder() {
        this.meal = new Meal();
    }

    public MealBuilder addCost(double cost) {
        this.meal.setCost(cost);
        return this;
    }

    public MealBuilder addTakeOut(bool takeOut) {
        this.meal.setTakeOut(takeOut);
        return this;
    }

    public MealBuilder addMainCourse(string main) {
        this.meal.setMain(main);
        return this;
    }

    public MealBuilder addDrink(string drink) {
        this.meal.setDrink(drink);
        return this;
    }

    public Meal build() {
        return this.meal;
    }
}
