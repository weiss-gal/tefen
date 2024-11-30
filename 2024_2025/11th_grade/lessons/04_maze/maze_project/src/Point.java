class Point {
    public Point(int x, int y){
        this.x = x;
        this.y = y;

    }
    public final int x;
    public final int y;

    @Override
    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}