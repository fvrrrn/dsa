using System;
using System.Collections.Generic;
using System.Text;

namespace MyCollectionsLibrary
{
    public class AVLTree<T> : BSTree<T>
        where T : IComparable
    {
        /// <summary>
        /// A utility function to Right rotate subtree rooted with y 
        /// </summary>
        /// <param name="node">Rooted node</param>
        /// <returns>Returns rotated node if successful</returns>
        private BSTreeNode<T> RightRotate(BSTreeNode<T> node)
        {
            BSTreeNode<T> node1 = (BSTreeNode<T>)node.Left;
            BSTreeNode<T> node2 = node1.Right;

            // Perform rotation  
            node1.Right = node;
            node.Left = node2;

            return node1;
        }

        /// <summary>
        /// A utility function to Left rotate subtree rooted with x 
        /// </summary>
        /// <param name="x">Rooted node</param>
        /// <returns>Returns rotated node if successful</returns>
        private BSTreeNode<T> LeftRotate(BSTreeNode<T> x)
        {
            BSTreeNode<T> y = x.Right;
            BSTreeNode<T> T2 = y.Left;

            // Perform rotation  
            y.Left = x;
            x.Right = T2;

            return y;
        }

        /// <summary>
        /// Returns balance factor of node  
        /// </summary>
        /// <param name="node"></param>
        /// <returns>Balance factor of node </returns>
        private int GetBalanceFacror(BSTreeNode<T> node)
        {
            if (node == null)
                return 0;

            return DepthAt(node.Left) - DepthAt(node.Right);
        }

        private void UpdateBalance(AVLTreeNode<T> node)
        {
            if (node != null)
            {
                node.BalanceFactor = DepthAt(node.Left) - DepthAt(node.Right);

                if (node.BalanceFactor >= 2 || node.BalanceFactor <= -2)
                    //GoBalance(ref node);

                UpdateBalance(node.Left);
                UpdateBalance(node.Right);
            }
        }

        /// <summary>
        /// Adds a new element to the tree
        /// </summary>
        public override void Add(T value)
        {
            BSTreeNode<T> node = new BSTreeNode<T>(value);
            Add(node);
        }

        /// <summary>
        /// Adds a node to the tree
        /// </summary>
        public override void Add(BSTreeNode<T> node)
        {
            base.Add(node);
            //UpdateBalance
        }
    }
}
