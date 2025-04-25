using System;
using System.Collections;
using System.Collections.Generic;

namespace MyCollectionsLibrary
{
    /// <summary>
    /// Binary Search Tree data structure
    /// </summary>
    public class BSTree<T> : ICollection<T>
        where T : IComparable
    {
        /// <summary>
        /// Specifies the mode of scanning through the tree
        /// </summary>
        public enum TraversalMode { LNR = 0, RNL, NLR }

        /// <summary>
        /// Gets or sets the root of the tree (the top-most node)
        /// </summary>
        public virtual BSTreeNode<T> Root { get; set; }

        bool ICollection<T>.IsReadOnly
        {
            get { return false; }
        }

        /// <summary>
        /// Gets the number of elements stored in the tree
        /// </summary>
        public int Count { get; protected set; }

        /// <summary>
        /// Gets the depth of the tree
        /// </summary>
        public int Depth => DepthAt(Root);

        /// <summary>
        /// Gets or sets the traversal mode of the tree
        /// </summary>
        public virtual TraversalMode TraversalOrder { get; set; } = TraversalMode.LNR;

        /// <summary>
        /// Adds a new element to the tree
        /// </summary>
        public virtual void Add(T value)
        {
            BSTreeNode<T> node = new BSTreeNode<T>(value);
            this.Add(node);
        }

        /// <summary>
        /// Gets depth at specified node
        /// </summary>
        public int DepthAt(BSTreeNode<T> node)
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

        /// <summary>
        /// Adds a node to the tree
        /// </summary>
        public virtual void Add(BSTreeNode<T> node)
        {
            if (this.Root == null) //first element being added
            {
                this.Root = node; //set node as root of the tree
                node.Tree = this;
                Count++;
                return;
            }

            if (node.Parent == null)
                node.Parent = Root; //start at head

            switch (node.Value.CompareTo(node.Parent.Value))
            {
                case -1:
                    if (node.Parent.Left == null)
                    {
                        //insert in left
                        node.Parent.Left = node;
                        Count++;
                        //assign node to this binary tree
                        node.Tree = this;
                    }
                    else
                    {
                        node.Parent = node.Parent.Left; //scan down to left child
                        this.Add(node); //recursive call
                    }
                    break;
                case 0:
                    node.Parent.DublicateCount++;
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
        }

        /// <summary>
        /// Returns the first node in the tree with the parameter value.
        /// </summary>
        public virtual BSTreeNode<T> Find(T value)
        {
            BSTreeNode<T> node = this.Root;
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

        /// <summary>
        /// Returns whether a value is stored in the tree
        /// </summary>
        public virtual bool Contains(T value)
        {
            return (this.Find(value) != null);
        }

        /// <summary>
        /// Removes a value from the tree and returns whether the removal was successful.
        /// </summary>
        public virtual bool Remove(T value)
        {
            BSTreeNode<T> removeNode = Find(value);

            return this.Remove(removeNode);
        }

        /// <summary>
        /// Removes a node from the tree and returns whether the removal was successful.
        /// </summary>>
        public virtual bool Remove(BSTreeNode<T> node)
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
                        this.Root = node.Left;

                    if (node.IsLeftChild)
                        node.Parent.Left = node.Left;
                    else
                        node.Parent.Right = node.Left;
                }
                else //Has right child
                {
                    //Put left node in place of the node to be removed
                    node.Right.Parent = node.Parent; //update parent

                    if (wasHead)
                        this.Root = node.Right;

                    if (node.IsLeftChild)
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
                BSTreeNode<T> successorNode = node.Left;
                while (successorNode.Right != null)
                {
                    successorNode = successorNode.Right;
                }

                node.Value = successorNode.Value; //replace value

                this.Remove(successorNode); //recursively remove the inorder predecessor
            }


            return true;
        }

        /// <summary>
        /// Removes all the elements stored in the tree
        /// </summary>
        public virtual void Clear()
        {
            Root = null;
            Count = 0;
            ////Remove children first, then parent
            ////(Post-order traversal)
            //IEnumerator<T> enumerator = GetPostOrderEnumerator();
            //while (enumerator.MoveNext())
            //{
            //    this.Remove(enumerator.Current);
            //}
            //enumerator.Dispose();
        }

        /// <summary>
        /// Gets an output string of current tree
        /// </summary>
        public override string ToString()
        {
            if (Root == null) return "";
            return GetNodesLine(Root, "", "", "Center", true, false);
        }

        /// <summary>
        /// Gets recursively an output string with specified entry node
        /// </summary>
        protected string GetNodesLine(BSTreeNode<T> current, string output, string indent, string nodePosition, bool last, bool empty)
        {
            output += indent;
            if (last)
            {
                output += "└─";
                indent += "  ";
            }
            else
            {
                output += "├─";
                indent += "| ";
            }

            var stringValue = empty ? "-" : current.Value.ToString() + "(" + current.DublicateCount.ToString() + ")";

            output = new Func<string, string>((string value) =>
            {
                switch (nodePosition)
                {
                    // fancy lambda code
                    case "Left":
                        return output = new Func<string, string>((string s) =>
                        {
                            s += "L:";
                            s += value + Environment.NewLine;
                            return s;
                        })(output);
                    case "Right":
                        return output = new Func<string, string>((string s) =>
                        {
                            s += "R:";
                            s += value + Environment.NewLine;
                            return s;
                        })(output);
                    case "Center":
                        return output = value + Environment.NewLine;
                    default:
                        throw new NotImplementedException();
                }
            })(stringValue);

            if (!empty && (current.Left != null || current.Right != null))
            {
                if (current.Left != null)
                    output = GetNodesLine(current.Left, output, indent, "Left", false, false);
                else
                    output = GetNodesLine(current, output, indent, "Left", false, true);

                if (current.Right != null)
                    output = GetNodesLine(current.Right, output, indent, "Right", true, false);
                else
                    output = GetNodesLine(current, output, indent, "Right", true, true);
            }

            return output;
        }

        /// <summary>
        /// Returns an enumerator to scan through the elements stored in tree.
        /// The enumerator uses the traversal set in the TraversalMode property.
        /// </summary>
        public virtual IEnumerator<T> GetEnumerator()
        {
            switch (this.TraversalOrder)
            {
                case TraversalMode.LNR:
                    return GetInOrderEnumerator();
                case TraversalMode.RNL:
                    return GetPostOrderEnumerator();
                case TraversalMode.NLR:
                    return GetPreOrderEnumerator();
                default:
                    return GetInOrderEnumerator();
            }
        }

        /// <summary>
        /// Returns an enumerator to scan through the elements stored in tree.
        /// The enumerator uses the traversal set in the TraversalMode property.
        /// </summary>
        IEnumerator IEnumerable.GetEnumerator()
        {
            return this.GetEnumerator();
        }

        /// <summary>
        /// Returns an enumerator that visits node in the order: left child, parent, right child
        /// </summary>
        public virtual IEnumerator<T> GetInOrderEnumerator()
        {
            return new BinaryTreeLNREnumerator(this);
        }

        /// <summary>
        /// Returns an enumerator that visits node in the order: left child, right child, parent
        /// </summary>
        public virtual IEnumerator<T> GetPostOrderEnumerator()
        {
            return new BinaryTreeRNLEnumerator(this);
        }

        /// <summary>
        /// Returns an enumerator that visits node in the order: parent, left child, right child
        /// </summary>
        public virtual IEnumerator<T> GetPreOrderEnumerator()
        {
            return new BinaryTreeNLREnumerator(this);
        }

        /// <summary>
        /// Copies the elements in the tree to an array using the traversal mode specified.
        /// </summary>
        public virtual void CopyTo(T[] array)
        {
            this.CopyTo(array, 0);
        }

        /// <summary>
        /// Copies the elements in the tree to an array using the traversal mode specified.
        /// </summary>
        public virtual void CopyTo(T[] array, int startIndex)
        {
            IEnumerator<T> enumerator = this.GetEnumerator();

            for (int i = startIndex; i < array.Length; i++)
            {
                if (enumerator.MoveNext())
                    array[i] = enumerator.Current;
                else
                    break;
            }
        }

        /// <summary>
        /// Returns an inorder-traversal enumerator for the tree values
        /// </summary>
        internal class BinaryTreeLNREnumerator : IEnumerator<T>
        {
            private BSTreeNode<T> current;
            private BSTree<T> tree;
            internal Queue<BSTreeNode<T>> traverseQueue;

            public BinaryTreeLNREnumerator(BSTree<T> tree)
            {
                this.tree = tree;

                //Build queue
                traverseQueue = new Queue<BSTreeNode<T>>();
                VisitNode(this.tree.Root);
            }

            private void VisitNode(BSTreeNode<T> node)
            {
                if (node == null)
                    return;
                else
                {
                    VisitNode(node.Left);
                    traverseQueue.Enqueue(node);
                    VisitNode(node.Right);
                }
            }

            public T Current
            {
                get { return current.Value; }
            }

            object IEnumerator.Current
            {
                get { return Current; }
            }

            public void Dispose()
            {
                current = null;
                tree = null;
            }

            public void Reset()
            {
                current = null;
            }

            public bool MoveNext()
            {
                if (traverseQueue.Count > 0)
                    current = traverseQueue.Dequeue();
                else
                    current = null;

                return (current != null);
            }
        }

        /// <summary>
        /// Returns a postorder-traversal enumerator for the tree values
        /// </summary>
        internal class BinaryTreeRNLEnumerator : IEnumerator<T>
        {
            private BSTreeNode<T> current;
            private BSTree<T> tree;
            internal Queue<BSTreeNode<T>> traverseQueue;

            public BinaryTreeRNLEnumerator(BSTree<T> tree)
            {
                this.tree = tree;

                //Build queue
                traverseQueue = new Queue<BSTreeNode<T>>();
                VisitNode(this.tree.Root);
            }

            private void VisitNode(BSTreeNode<T> node)
            {
                if (node == null)
                    return;
                else
                {
                    VisitNode(node.Right);
                    traverseQueue.Enqueue(node);
                    VisitNode(node.Left);

                    //VisitNode(node.Left);
                    //VisitNode(node.Right);
                    //traverseQueue.Enqueue(node);
                }
            }

            public T Current
            {
                get { return current.Value; }
            }

            object IEnumerator.Current
            {
                get { return Current; }
            }

            public void Dispose()
            {
                current = null;
                tree = null;
            }

            public void Reset()
            {
                current = null;
            }

            public bool MoveNext()
            {
                if (traverseQueue.Count > 0)
                    current = traverseQueue.Dequeue();
                else
                    current = null;

                return (current != null);
            }
        }

        /// <summary>
        /// Returns an preorder-traversal enumerator for the tree values
        /// </summary>
        internal class BinaryTreeNLREnumerator : IEnumerator<T>
        {
            private BSTreeNode<T> current;
            private BSTree<T> tree;
            internal Queue<BSTreeNode<T>> traverseQueue;

            public BinaryTreeNLREnumerator(BSTree<T> tree)
            {
                this.tree = tree;

                //Build queue
                traverseQueue = new Queue<BSTreeNode<T>>();
                VisitNode(this.tree.Root);
            }

            private void VisitNode(BSTreeNode<T> node)
            {
                if (node == null)
                    return;
                else
                {
                    traverseQueue.Enqueue(node);
                    VisitNode(node.Left);
                    VisitNode(node.Right);
                }
            }

            public T Current
            {
                get { return current.Value; }
            }

            object IEnumerator.Current
            {
                get { return Current; }
            }

            public void Dispose()
            {
                current = null;
                tree = null;
            }

            public void Reset()
            {
                current = null;
            }

            public bool MoveNext()
            {
                if (traverseQueue.Count > 0)
                    current = traverseQueue.Dequeue();
                else
                    current = null;

                return (current != null);
            }
        }
    }
}
