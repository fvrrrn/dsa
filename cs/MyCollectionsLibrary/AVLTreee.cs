using System;

namespace MyCollectionsLibrary
{
    public class AVLTreee<T>
        where T : IComparable
    {
        public virtual AVLTreeeNode<T> Root { get; set; }

        public int Count { get; protected set; }

        public int Depth => DepthAt(Root);

        public int DepthAt(AVLTreeeNode<T> node)
        {
            if (node == null)
                return 0;
            else
            {
                int lDepth = DepthAt(node.Left);
                int rDepth = DepthAt(node.Right);
                return lDepth > rDepth ? lDepth + 1 : rDepth + 1;
            }
        }

        public void Add(T value)
        {
            AVLTreeeNode<T> node = new AVLTreeeNode<T>(value);
            this.Add(node);
        }

        public void Add(AVLTreeeNode<T> node)
        {
            if (this.Root == null)
            {
                this.Root = node;
                node.Tree = this;
                Count++;
                return;
            }

            if (node.Parent == null)
                node.Parent = Root;

            switch (node.Value.CompareTo(node.Parent.Value))
            {
                case -1:
                    if (node.Parent.Left == null)
                    {
                        node.Parent.Left = node;
                        Count++;
                        node.Tree = this;
                    }
                    else
                    {
                        node.Parent = node.Parent.Left;
                        this.Add(node);
                    }
                    break;
                case 0:
                    break;
                case 1:
                    if (node.Parent.Right == null)
                    {
                        node.Parent.Right = node; //insert in right
                        Count++;
                        node.Tree = this; //assign node to this binary tree
                    }
                    else
                    {
                        node.Parent = node.Parent.Right;
                        this.Add(node);
                    }
                    break;
            }
            UpdateBalance(Root);
        }

        public AVLTreeeNode<T> Find(T value)
        {
            AVLTreeeNode<T> node = this.Root;
            while (node != null)
            {
                switch (value.CompareTo(node.Value))
                {
                    case -1:
                        node = node.Left;
                        break;
                    case 0:
                        return node;
                    case 1:
                        node = node.Right;
                        break;
                }
            }

            return null;
        }

        public bool Remove(T value)
        {
            AVLTreeeNode<T> removeNode = Find(value);

            return this.Remove(removeNode);
        }

        public virtual bool Remove(AVLTreeeNode<T> node)
        {
            if (node == null || node.Tree != this)
                return false; //value doesn't exist or not of this tree

            //Note whether the node to be removed is the root of the tree
            bool wasHead = (node == Root);

            if (this.Count == 1)
            {
                this.Root = null; //only element was the root
                node.Tree = null;

                Count--; //decrease total element count
            }
            else if (node.IsLeaf) //Case 1: No Children
            {
                //Remove node from its parent
                if (node.IsLeftChild)
                    node.Parent.Left = null;
                else
                    node.Parent.Right = null;

                node.Tree = null;
                node.Parent = null;

                Count--; //decrease total element count
            }
            else if (node.ChildCount == 1) //Case 2: One Child
            {
                if (node.HasLeftChild)
                {
                    //Put left child node in place of the node to be removed
                    node.Left.Parent = node.Parent; //update parent

                    if (wasHead)
                        this.Root = node.Left; //update root reference if needed

                    if (node.IsLeftChild) //update the parent's child reference
                        node.Parent.Left = node.Left;
                    else
                        node.Parent.Right = node.Left;
                }
                else //Has right child
                {
                    //Put left node in place of the node to be removed
                    node.Right.Parent = node.Parent; //update parent

                    if (wasHead)
                        this.Root = node.Right; //update root reference if needed

                    if (node.IsLeftChild) //update the parent's child reference
                        node.Parent.Left = node.Right;
                    else
                        node.Parent.Right = node.Right;
                }

                node.Tree = null;
                node.Parent = null;
                node.Left = null;
                node.Right = null;

                Count--; //decrease total element count
            }
            else //Case 3: Two Children
            {
                //Find inorder predecessor (right-most node in left subtree)
                AVLTreeeNode<T> successorNode = node.Left;
                while (successorNode.Right != null)
                {
                    successorNode = successorNode.Right;
                }

                node.Value = successorNode.Value; //replace value

                this.Remove(successorNode); //recursively remove the inorder predecessor
            }


            return true;
        }

        private AVLTreeeNode<T> RightRotate(AVLTreeeNode<T> node)
        {
            AVLTreeeNode<T> node1 = node.Left;
            AVLTreeeNode<T> node2 = node1.Right;

            // Perform rotation  
            node1.Right = node;
            node.Left = node2;

            return node1;
        }

        private AVLTreeeNode<T> LeftRotate(AVLTreeeNode<T> x)
        {
            AVLTreeeNode<T> y = x.Right;
            AVLTreeeNode<T> T2 = y.Left;

            // Perform rotation  
            y.Left = x;
            x.Right = T2;

            return y;
        }

        private int GetBalanceFacror(AVLTreeeNode<T> node)
        {
            if (node == null)
                return 0;

            return DepthAt(node.Left) - DepthAt(node.Right);
        }

        private void UpdateBalance(AVLTreeeNode<T> node)
        {
            if (node != null)
            {
                node.BalanceFactor = DepthAt(node.Left) - DepthAt(node.Right);

                if (node.BalanceFactor >= 2 || node.BalanceFactor <= -2)
                    Balance(node);

                UpdateBalance(node.Left);
                UpdateBalance(node.Right);
            }
        }

        public void Balance(AVLTreeeNode<T> node)
        {
            if (node.BalanceFactor > 1)
            {
                if (DepthAt(node.Left.Left) - DepthAt(node.Left.Right) >= 0)
                    LeftLeftCase(node);
                else
                    LeftRightCase(node);
            }
            else if (node.BalanceFactor < -1)
            {
                if (DepthAt(node.Right.Left) - DepthAt(node.Right.Right) <= 0)
                    RightRightCase(node);
                else
                    RightLeftCase(node);
            }
            UpdateBalance(Root);
        }

        private void LeftLeftCase(AVLTreeeNode<T> node)
        {
            AVLTreeeNode<T> tmp1 = node.Left;
            AVLTreeeNode<T> tmp2 = tmp1.Right;

            tmp1.Right = node;
            node.Left = tmp2;
            node = tmp1;
            node.Parent = node.Parent.Parent;
            Root = node.Parent == null ? node : Root;
        }

        private void RightRightCase(AVLTreeeNode<T> node)
        {
            AVLTreeeNode<T> tmp1 = node.Right;
            AVLTreeeNode<T> tmp2 = tmp1.Left;

            tmp1.Left = node;
            node.Right = tmp2;
            node = tmp1;
        }

        private void LeftRightCase(AVLTreeeNode<T> node)
        {
            RightRightCase(node.Left);
            LeftLeftCase(node);
        }


        private void RightLeftCase(AVLTreeeNode<T> node)
        {
            LeftLeftCase(node.Right);
            RightRightCase(node);
        }

        public string ToLNRString()
        {
            return ToLNRString("", Root);
        }

        public string ToLNRString(string output, AVLTreeeNode<T> node)
        {
            if (node == null)
                return output;
            else
            {
                ToLNRString(output, node.Left);
                output += node.Value;
                ToLNRString(output, node.Right);
            }
            return output;
        }

        public string ToRNLString()
        {
            return ToRNLString("", Root);
        }

        public string ToRNLString(string output, AVLTreeeNode<T> node)
        {
            if (node == null)
                return output;
            else
            {
                ToRNLString(output, node.Right);
                output += node.Value;
                ToRNLString(output, node.Left);
            }
            return output;
        }
    }
}
