using System.Collections;
using System.Collections.Generic;

namespace MyCollectionsLibrary
{
    /// <summary>
    /// My Queue data structure
    /// </summary>
    public class MyQueue<T> : IEnumerable<T>
    {
        private MyLinkedList<T> llist;

        /// <summary>
        /// Gets the number of elements stored in queue.
        /// </summary>
        public int Count => llist.Count;

        /// <summary>
        /// Creates a new instance of My Queue.
        /// </summary>
        public MyQueue()
        {
            llist = new MyLinkedList<T>();
        }

        /// <summary>
        /// Pushes a new element to last added in queue.
        /// </summary>
        public bool Push(T item)
        {
            return llist.AddLast(item) != null;
        }

        /// <summary>
        /// Removes last element from queue.
        /// </summary>
        public T Pop()
        {
            return llist.Remove(llist.Last).Value;
        }

        /// <summary>
        /// Gets last added element in queue.
        /// </summary>
        public T Peek()
        {
            return llist.Last.Value;
        }

        /// <summary>
        /// Removes all elements from collection
        /// </summary>
        public void Clear()
        {
            llist.Clear();
        }

        /// <returns>
        /// Returns true if queue is empty.
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
