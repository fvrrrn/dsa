using System.Collections;
using System.Collections.Generic;

namespace MyCollectionsLibrary
{
    /// <summary>
    /// My Stack data structure
    /// </summary>
    public class MyStack<T> : IEnumerable<T>
    {
        private MyLinkedList<T> llist;

        /// <summary>
        /// Gets the number of elements stored in stack.
        /// </summary>
        public int Count => llist.Count;

        /// <summary>
        /// Creates a new instance of My Stack.
        /// </summary>
        public MyStack()
        {
            llist = new MyLinkedList<T>();
        }

        /// <summary>
        /// Pushes a new element to last added in stack.
        /// </summary>
        public void Push(T item)
        {
            llist.AddFirst(item);
        }

        /// <summary>
        /// Removes last element from stack.
        /// </summary>
        public T Pop()
        {
            return llist.Remove(llist.First).Value;
        }

        /// <summary>
        /// Gets last added element in stack.
        /// </summary>
        public T Peek()
        {
            return llist.First.Value;
        }

        /// <returns>
        /// Returns true if stack is empty.
        /// </returns>
        public bool IsEmpty()
        {
            return Count == 0 ? true : false;
        }

        /// <inheritdoc />
        public IEnumerator<T> GetEnumerator()
        {
            return llist.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
