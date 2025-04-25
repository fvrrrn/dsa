namespace MyCollectionsLibrary
{
    /// <summary>
    /// My Linked List node that holds an element and references to other two nodes
    /// </summary>
    public class MyLinkedListNode<T>
    {
        /// <summary>
        /// The value stored at the node.
        /// </summary>
        public T Value { get; set; }

        /// <summary>
        /// Gets or sets parent of the node.
        /// </summary>
        public MyLinkedListNode<T> Parent { get; set; }

        /// <summary>
        /// Gets or sets child of the node.
        /// </summary>
        public MyLinkedListNode<T> Child { get; set; }

        /// <summary>
        /// Gets or sets reference to list this node is stored in.
        /// </summary>
        public MyLinkedList<T> List { get; set; }

        /// <summary>
        /// Gets or sets number of dublicates of current node
        /// </summary>
        public int DublicateCount { get; set; }

        /// <summary>
        /// Gets whether the node is a leaf (either has no children or no parents)
        /// </summary>
        public bool IsLeaf
        {
            get { return (Parent == null ^ Child == null); }
        }

        /// <summary>
        /// Gets whether the node is internal (has children and parents)
        /// </summary>
        public bool IsInternal
        {
            get { return (Parent != null && Child != null); }
        }

        /// <summary>
        /// Creates a new instance of a Binary Tree node
        /// </summary>
        public MyLinkedListNode(T value)
        {
            Value = value;
        }
    }
}
