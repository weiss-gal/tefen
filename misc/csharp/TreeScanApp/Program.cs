namespace BinNode {
    public class BinNode <T> {
        private BinNode<T> left;
        private T value;
        private BinNode<T> right;

        public BinNode(BinNode<T> left, T value, BinNode<T> right) {
            this.left = left;
            this.value = value;
            this.right = right;
        }

        public BinNode(T value) {
            this.value = value;
            this.right = null;
            this.left = null;
        }

        public BinNode<T> getLeft() {
            return left;
        }

        public void setLeft(BinNode<T> left) {
            this.left = left;
        }

        public T getValue() {
            return value;
        }

        public void setValue(T value) {

            this.value = value;

        }

        public BinNode<T> getRight() {

            return right;

        }

        public void setRight(BinNode<T> right) {

            this.right = right;

        }
    }

    class TreeScan {
        static string preOrder(BinNode<string> node) {
            string left = "";
            if (node.getLeft() != null) {
                left = preOrder(node.getLeft());
            }

            string right = "";
            if (node.getRight() != null) {
                right = preOrder(node.getRight());
            }
            
            return node.getValue() + left + right;
        }

        static string inOrder(BinNode<string> node) {
            string left = "";
            if (node.getLeft() != null) {
                left = inOrder(node.getLeft());
            }

            string right = "";
            if (node.getRight() != null) {
                right = inOrder(node.getRight());
            }
            
            return left + node.getValue() + right;
        }

        static void Main(string[] args){
            var c_node = new BinNode<string>("C");
            var e_node = new BinNode<string>("E");
            var a_node= new BinNode<string>(e_node, "A", c_node);
            var b_node = new BinNode<string>("B");
            var d_node = new BinNode<string>(b_node, "D", a_node);

            Console.WriteLine("pre-order: " + preOrder(d_node));
            Console.WriteLine("in-order: " + inOrder(d_node));
        }
    }
}