using System;

namespace MyCollectionsLibrary
{
    public class AVLTreeeNode<T>
        where T : IComparable
    {
        public T Value { get; set; }

        public AVLTreeeNode<T> Left { get; set; }

        public AVLTreeeNode<T> Right { get; set; }

        public AVLTreeeNode<T> Parent { get; set; }

        public AVLTreee<T> Tree { get; set; }

        public bool IsLeaf
        {
            get { return ChildCount == 0; }
        }

        public bool IsInternal
        {
            get { return ChildCount > 0; }
        }

        public bool IsLeftChild
        {
            get { return this.Parent != null && this.Parent.Left == this; }
        }

        public bool IsRightChild
        {
            get { return this.Parent != null && this.Parent.Right == this; }
        }

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

        public bool HasLeftChild
        {
            get { return (this.Left != null); }
        }

        public bool HasRightChild
        {
            get { return (this.Right != null); }
        }

        public int BalanceFactor { get; set; }

        public AVLTreeeNode(T value)
        {
            this.Value = value;
        }
    }
}
