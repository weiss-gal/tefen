public abstract class Maze {
    public abstract int getHeight();
    public abstract int getWidth();
    /* Zero based addressing */
    public abstract boolean hasWall(int x, int y);

}
