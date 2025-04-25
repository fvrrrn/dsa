using System;
using System.Collections.Generic;
using System.Text;
using MyCollectionsLibrary;

namespace MiscLibrary
{
    public class Concordance : BSTree<string>
    {
        private Queue<BSTreeNode<string>> traverseQueue;

        public static string[] Parse(string s)
        {
            return s.ToLower().Split();
        }

        public override string ToString()
        {
            string s = "";
            traverseQueue = new Queue<BSTreeNode<string>>();
            VisitNode(Root);

            while (traverseQueue.Count > 0)
            {
                BSTreeNode<string> tmp = traverseQueue.Dequeue();

                s += tmp.Value + ".........." + (tmp.DublicateCount + 1) + Environment.NewLine;
            }

            return s;
        }

        private void VisitNode(BSTreeNode<string> node)
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

        public override IEnumerator<string> GetEnumerator()
        {
            traverseQueue = new Queue<BSTreeNode<string>>();
            VisitNode(Root);

            while (traverseQueue.Count > 0)
            {
                BSTreeNode<string> tmp = traverseQueue.Dequeue();

                yield return tmp.Value + " " + (tmp.DublicateCount + 1);
            }
        }
    }
}
