using System.Collections;
using System.Collections.Generic;

namespace MyCollectionsLibrary
{
    /// <summary>
    /// My Linked List data structure
    /// </summary>
    public class MyLinkedList<T> : IEnumerable<T>
    {
        /// <summary>
        /// Specifies the enumeration order
        /// </summary>
        public enum OrderMode { Towards = 0, Backwards }
        private OrderMode orderMode = OrderMode.Towards;

        /// <summary>
        /// Gets or sets the first element of the list (the top-most node).
        /// </summary>
        public virtual MyLinkedListNode<T> First { get; set; }

        /// <summary>
        /// Gets or sets last element of the list (the lower-most node).
        /// </summary>
        public virtual MyLinkedListNode<T> Last { get; private set; }

        /// <inheritdoc />
        public virtual int Count { get; private set; }

        /// <summary>
        /// Creates a new instance of my Linked List.
        /// </summary>
        public MyLinkedList()
        {
        }        

        /// <summary>
        /// Adds a new node with given value to the list before its head.
        /// Returns this node if addition was successful.
        /// </summary>
        public virtual MyLinkedListNode<T> AddFirst(T value)
        {
            MyLinkedListNode<T> node = new MyLinkedListNode<T>(value);
            return this.AddFirst(node);
        }

        /// <summary>
        /// Adds a node to the list before its head.
        /// Returns this node if addition was successful.
        /// </summary>
        public virtual MyLinkedListNode<T> AddFirst(MyLinkedListNode<T> node)
        {
            if (First == null)
            {
                First = node;
                First.List = this;
                Last = First;
            }
            else
            {
                node.Child = First;
                First.Parent = node;
                First = node;
                First.List = this;
            }
            Count++;

            return First;
        }

        /// <summary>
        /// Adds a new node with the given value to the list after its last element.
        /// Returns this node if addition was successful.
        /// </summary>
        public virtual MyLinkedListNode<T> AddLast(T value)
        {
            MyLinkedListNode<T> node = new MyLinkedListNode<T>(value);
            return this.AddLast(node);
        }

        /// <summary>
        /// Adds a node to the list after its last element.
        /// Returns this node if addition was successful.
        /// </summary>
        public virtual MyLinkedListNode<T> AddLast(MyLinkedListNode<T> node)
        {
            if (First == null)
            {
                First = node;
                First.List = this;
                Count++;
                return Last = First;
            }
            else
            {
                Last.Child = node;
                node.Parent = Last;
                Count++;
                return Last = node;
            }
        }

        /// <summary>
        /// Adds a new node with the given value before another node in the list with specified value.
        /// Returns this node if addition was successful.
        /// </summary>
        /// <param name="value1">Value in list.</param>
        /// <param name="value2">Node with this value.</param>
        public virtual MyLinkedListNode<T> AddBefore(T value1, T value2)
        {
            MyLinkedListNode<T> node1 = this.Find(value1);
            MyLinkedListNode<T> node2 = new MyLinkedListNode<T>(value2);
            return this.AddBefore(node1, node2);
        }

        /// <summary>
        /// Adds a new node with the given value before another node in the list.
        /// Returns this node if addition was successful.
        /// </summary>
        /// <param name="node1">Node in list.</param>
        /// <param name="value">Node with this value.</param>
        public virtual MyLinkedListNode<T> AddBefore(MyLinkedListNode<T> node1, T value)
        {
            MyLinkedListNode<T> node2 = new MyLinkedListNode<T>(value);
            return this.AddBefore(node1, node2);
        }

        /// <summary>
        /// Adds a node before another node in the list before given node.
        /// Returns this node if addition was successful.
        /// </summary>
        /// <param name="node1">Node in list.</param>
        /// <param name="node2">Node with this value.</param>
        public virtual MyLinkedListNode<T> AddBefore(MyLinkedListNode<T> node1, MyLinkedListNode<T> node2)
        {
            // Case 0 node2 is null
            if (node2 == null)
            {
                return null;
            }

            // Case 1 List is empty; return null because operation was not successful
            if (First == null)
            {
                return null;
            }

            // Case 2 Node1 not found or null 
            if (node1 == null)
            {
                return null;
            }

            // Case 3 node1 is head -> adding before head 
            if (First == node1)
            {
                return AddFirst(node2);
            }

            // Case 4 Node1 is not null and it is not head
            MyLinkedListNode<T> current = First;
            while (current != null)
            {
                if (current == node1)
                {
                    // Example: insert (5) before (2) in (3)<->(2)
                    // current = (2)

                    node2.Parent = current.Parent;
                    // (3)<-(5) (2)

                    current.Parent = node2;
                    // (3)<-(5)<-(2)

                    node2.Child = current;
                    // (3)<-(5)<->(2)

                    node2.Parent.Child = node2;
                    // (3)<->(5)<->(2)

                    node2.List = this;

                    Count++;
                    return node2;
                }
                else
                {
                    current = current.Child;
                }
            }
            // Case 5 Given node does not exist in current list
            return null;
        }

        /// <summary>
        /// Adds a new node with the given value after another node in the list with specified value.
        /// </summary>
        /// <returns>Returns this node if addition was successful.</returns>
        /// <param name="value1">Value in list.</param>
        /// <param name="value2">Node with this value.</param>
        public virtual MyLinkedListNode<T> AddAfter(T value1, T value2)
        {
            MyLinkedListNode<T> node1 = this.Find(value1);
            MyLinkedListNode<T> node2 = new MyLinkedListNode<T>(value2);
            return AddAfter(node1, node2);
        }

        /// <summary>
        /// Adds a new node with the given value after another node in the list.
        /// </summary> 
        /// <returns>This node if addition was successful.</returns> 
        /// <param name="node1">Node in list.</param>
        /// <param name="value">Node with this value.</param>
        public virtual MyLinkedListNode<T> AddAfter(MyLinkedListNode<T> node1, T value)
        {
            MyLinkedListNode<T> node2 = new MyLinkedListNode<T>(value);
            return AddAfter(node1, node2);
        }

        /// <summary>
        /// Adds a node before another node in the list after given node.
        /// Returns this node if addition was successful.
        /// </summary>
        /// <param name="node1">Node in list.</param>
        /// <param name="node2">Node.</param>
        public virtual MyLinkedListNode<T> AddAfter(MyLinkedListNode<T> node1, MyLinkedListNode<T> node2)
        {
            // Case 0 node2 is null
            if (node2 == null)
            {
                return null;
            }

            // Case 1 List is empty; return null because operation was not successful
            if (First == null)
            {
                return null;
            }

            // Case 2 Node1 not found or null 
            if (node1 == null)
            {
                return null;
            }

            // Case 3 Searching the given node in nodes
            MyLinkedListNode<T> current = First;
            while (current != null)
            {
                if (current == node1)
                {
                    // Example: insert 5 after (3) in (3)<->(2)
                    // current = (3)

                    // Case where node is found and it is last element
                    if (current.Child == null)
                    {
                        return this.AddLast(node2);
                    }

                    node2.Child = current.Child;
                    // (3) (5)->(2)
                    // ^---------|

                    node2.Parent = current;
                    // (3)<-(5)->(2)
                    // ^----------|

                    node2.Child.Parent = node2;
                    // (3)<-(5)<->(2)

                    node2.Parent.Child = node2;
                    // (3)<->(5)<->(2)

                    node2.List = this;

                    Count++;
                    return node2;
                }
                else
                {
                    current = current.Child;
                }
            }
            // Case 4 Given node does not exist in current list
            return null;
        }

        /// <summary>
        /// Removes a value from the list and returns nullable node if the removal was successful.
        /// </summary>
        public virtual MyLinkedListNode<T> Remove(T value)
        {
            if (First == null) return null;

            MyLinkedListNode<T> current = First;
            while (current != null)
            {
                if (value.Equals(current.Value))
                {
                    // if head is last element
                    if (First.Child == null)
                    {
                        var v = First;
                        First = null;
                        Last = null;
                        Count--;
                        return v;
                    }

                    // case 2 Removing last element
                    if (current.Child == null)
                    {
                        // remove dependency
                        current.Parent.Child = null;

                        // reset last link
                        Last = current.Parent;

                        // remove last element
                        Count--;
                        return current;
                    }

                    // There are 3 cases:
                    // 1) head is set to remove
                    // 2) last element (tail) is set to remove
                    // 3) element with child and parent is set to remove

                    // case 1 Removing head
                    if (current.Parent == null)
                    {

                        // remove dependency
                        current.Child.Parent = null;

                        // set new head to its child
                        First = current.Child;

                        // remove head
                        Count--;
                        return current;
                    }

                    // case 3 Removing regular element
                    // Example: remove 5 in (3)<->(5)<->(2)
                    // (5).Parent = (5).Child 
                    // which is (3)->(2)
                    current.Parent = current.Child;

                    // (5).Child.Parent = (5).Parent;
                    // which is (3)<->(2)
                    current.Child.Parent = current.Parent;

                    // now securely remove
                    Count--;
                    return current;
                }
                current = current.Child;
            }
            return null;
        }

        /// <summary>
        /// Removes specific node from the list and returns this node if the removal was successful.
        /// </summary>
        public virtual MyLinkedListNode<T> Remove(MyLinkedListNode<T> node)
        {
            if (First == null) return null;

            // There are 3 cases:
            // 1) head is set to remove
            // 2) last element (tail) is set to remove
            // 3) element with child and parent is set to remove

            // case 1 Removing head
            if (node == First)
            {
                if (First.Child == null)
                {
                    First = null;
                    Last = null;
                    Count--;
                    return node;
                }

                // creating temporary variable
                var tmp = First.Child;

                // remove dependency
                tmp.Parent = null;

                // set new head to its child
                First = tmp;

                // remove head
                Count--;
                return node;
            }

            // case 2 Removing last element
            if (node == Last)
            {
                // creating temporary variable
                var tmp = Last.Parent;

                // remove dependency
                tmp.Child = null;

                // reset last link
                Last = tmp;

                // remove last element
                Count--;
                return node;
            }

            // case 3 Removing regular element
            MyLinkedListNode<T> current = First;
            while (current != null)
            {
                if (node == current)
                {
                    // Example: remove 5 in (3)<->(5)<->(2)
                    // (5).Parent = (5).Child 
                    // which is (3)->(2)
                    current.Parent = current.Child;

                    // (5).Child.Parent = (5).Parent;
                    // which is (3)<->(2)
                    current.Child.Parent = current.Parent;

                    // now securely remove
                    Count--;
                    return node;
                }
            }
            return null;
        }

        /// <summary>
        /// Returns the first node in the list with the parameter value.
        /// </summary>
        public virtual MyLinkedListNode<T> Find(T value)
        {
            if (First == null) return null;

            MyLinkedListNode<T> current = First;
            while (current != null)
            {
                if (value.Equals(current.Value)) return current;
                current = current.Child;
            }

            return null;
        }

        /// <summary>
        /// Removes all elements from collection
        /// </summary>
        public virtual void Clear()
        {
            MyLinkedListNode<T> current = First;
            while (current != null)
            {
                MyLinkedListNode<T> temp = current;
                current = current.Child;
                temp = null;
            }

            First = null;
            Count = 0;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        /// <inheritdoc />
        public virtual IEnumerator<T> GetEnumerator()
        {
            switch (orderMode)
            {
                case OrderMode.Towards:
                    return new LinkedListTowardsEnumerator(this);
                case OrderMode.Backwards:
                    return new LinkedListBackwardsEnumerator(this);
                default:
                    return new LinkedListTowardsEnumerator(this);
            }
        }

        /// <summary>
        /// Returns first to last enumerator
        /// </summary>
        internal class LinkedListTowardsEnumerator : IEnumerator<T>
        {
            private MyLinkedListNode<T> current;
            private MyLinkedList<T> list;

            public LinkedListTowardsEnumerator(MyLinkedList<T> list)
            {
                this.list = list;
            }

            public T Current => current.Value;

            object IEnumerator.Current => Current;

            public void Dispose()
            {
                current = null;
                list = null;
            }

            public void Reset()
            {
                current = null;
            }

            public bool MoveNext()
            {
                // if list is empty
                if (list.First == null) return false;

                // enumeration starts
                if (current == null) { current = list.First; return true; }

                // if current node is last stop enumeration
                if (current.Child == null) return false;

                current = current.Child;

                return true;
            }
        }

        /// <summary>
        /// Returns last to first enumerator
        /// </summary>
        internal class LinkedListBackwardsEnumerator : IEnumerator<T>
        {
            private MyLinkedListNode<T> current;
            private MyLinkedList<T> list;

            public LinkedListBackwardsEnumerator(MyLinkedList<T> list)
            {
                this.list = list;
            }

            public T Current => current.Value;

            object IEnumerator.Current => Current;

            public void Dispose()
            {
                current = null;
                list = null;
            }

            public void Reset()
            {
                current = null;
            }

            public bool MoveNext()
            {
                if (list.Last == null) return false;

                if (current == null) { current = list.Last; return true; }

                if (current.Parent == null) return false;

                current = current.Parent;

                return true;
            }
        }
    }
}
