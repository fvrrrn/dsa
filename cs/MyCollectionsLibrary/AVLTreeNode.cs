using System;
using System.Collections.Generic;
using System.Text;

namespace MyCollectionsLibrary
{
    public class AVLTreeNode<T> : BSTreeNode<T>
        where T : IComparable
    {
        public new AVLTreeNode<T> Left { get; set; }
        public new AVLTreeNode<T> Right { get; set; }
        // depricate dublicated nodes or move in another class

        /// <summary>
        /// Gets or sets balance factor
        /// </summary>
        internal int BalanceFactor { get; set; }

        public AVLTreeNode(T value) : base(value)
        {
        }
    }
}
