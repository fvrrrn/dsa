using System;

namespace MyCollectionsLibrary
{
    /// <summary>
    /// A Binary Tree node that holds an element and references to other tree nodes
    /// </summary>
    public class BSTreeNode<T>
        where T : IComparable
    {
        /// <summary>
        /// The value stored at the node
        /// </summary>
        public T Value { get; set; }

        /// <summary>
        /// Gets or sets the left child node
        /// </summary>
        public virtual BSTreeNode<T> Left { get; set; }

        /// <summary>
        /// Gets or sets the right child node
        /// </summary>
        public virtual BSTreeNode<T> Right { get; set; }

        /// <summary>
        /// Gets or sets the parent node
        /// </summary>
        public virtual BSTreeNode<T> Parent { get; set; }

        /// <summary>
        /// Gets or sets the Binary Tree the node belongs to
        /// </summary>
        public virtual BSTree<T> Tree { get; set; }

        /// <summary>
        /// Gets whether the node is a leaf (has no children)
        /// </summary>
        public bool IsLeaf
        {
            get { return ChildCount == 0; }
        }

        /// <summary>
        /// Gets whether the node is internal (has children nodes)
        /// </summary>
        public bool IsInternal
        {
            get { return ChildCount > 0; }
        }

        /// <summary>
        /// Gets whether the node is the left child of its parent
        /// </summary>
        public bool IsLeftChild
        {
            get { return this.Parent != null && this.Parent.Left == this; }
        }

        /// <summary>
        /// Gets whether the node is the right child of its parent
        /// </summary>
        public bool IsRightChild
        {
            get { return this.Parent != null && this.Parent.Right == this; }
        }

        /// <summary>
        /// Gets the number of children this node has
        /// </summary>
        public int ChildCount
        {
            get
            {
                int count = 0;

                if (this.Left != null)
                    count++;

                if (this.Right != null)
                    count++;

                return count;
            }
        }

        /// <summary>
        /// Gets whether the node has a left child node
        /// </summary>
        public bool HasLeftChild
        {
            get { return (this.Left != null); }
        }

        /// <summary>
        /// Gets whether the node has a right child node
        /// </summary>
        public bool HasRightChild
        {
            get { return (this.Right != null); }
        }

        /// <summary>
        /// Gets or sets number of dublicates of current node
        /// </summary>
        public virtual int DublicateCount { get; set; }

        /// <summary>
        /// Creates a new instance of a Binary Tree node
        /// </summary>
        public BSTreeNode(T value)
        {
            this.Value = value;
        }
    }
}
