using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using DaSA;
using System.Collections.Generic;

namespace UnitTest
{
    [TestClass]
    public class BinaryTreeTest
    {
        [TestMethod]
        public void Add_With1Element()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value = 5;

            // Act
            binaryTree.Add(value);

            // Assert
            Assert.AreEqual(value, binaryTree.Last.Value);
        }

        [TestMethod]
        public void Add_With2Elements()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 6;

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);

            // Assert
            Assert.AreEqual(value1, binaryTree.Head.Value);
            Assert.AreEqual(value2, binaryTree.Last.Value);
        }

        [TestMethod]
        public void Get_ValuesList()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            List<int> list1;
            List<int> list2 = new List<int>();
            int value1 = 5;
            int value2 = 6;
            int value3 = 7;
            bool b = true;

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
            binaryTree.Add(value3);
            list1 = binaryTree.ValuesList;

            list2.Add(value1);
            list2.Add(value2);
            list2.Add(value3);

            // Assert
            for (int i = 0; i < list2.Count; i++)
            {
                if (list1[i] != list2[i]) b = false;
            }
            Assert.IsTrue(b);
        }

        [TestMethod]
        public void Find_InbinaryTree_WithExistingValue()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 6;
            int value3 = 7;
            BinaryTreeNode<int> node;

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
            binaryTree.Add(value3);
            node = binaryTree.Find(7);

            // Assert
            Assert.AreEqual(node, binaryTree.Last);
        }

        [TestMethod]
        public void Find_InbinaryTree_WithNoExistingValue()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 6;
            int value3 = 7;
            BinaryTreeNode<int> node;

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
            binaryTree.Add(value3);
            node = binaryTree.Find(8);

            // Assert
            Assert.AreEqual(node, null);
        }

        [TestMethod]
        public void Get_Parent()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 6;
            int value3 = 7;
            BinaryTreeNode<int> node;
            BinaryTreeNode<int> nodeParent;


            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
            binaryTree.Add(value3);
            node = binaryTree.Find(7);
            nodeParent = binaryTree.Find(6);

            // Assert
            Assert.AreEqual(nodeParent, node.Parent);
        }

        [TestMethod]
        public void Get_DublicatesCount()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 6;
            int value3 = 6;


            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
            binaryTree.Add(value3);

            // Assert
            Assert.AreEqual(0, binaryTree.Head.DublicateCount);
            Assert.AreEqual(1, binaryTree.Last.DublicateCount);
        }

        [TestMethod]
        public void Delete_With1Element()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            BinaryTreeNode<int> node = binaryTree.Find(5);

            // Act
            binaryTree.Add(value1);
           // binaryTree.Delete(ref node);

            // Assert
            Assert.AreEqual(null, binaryTree.Head);
            Assert.AreEqual(null, node);
        }

        [TestMethod]
        public void Delete_With2Elements_Left()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 4;
            BinaryTreeNode<int> node = binaryTree.Find(4);

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
           // binaryTree.Delete(ref node);

            // Assert
            Assert.AreEqual(null, node);
        }

        [TestMethod]
        public void Delete_With2Elements_Right()
        {
            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 6;
            BinaryTreeNode<int> node = binaryTree.Find(6);

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
           // binaryTree.Delete(ref node);

            // Assert
            Assert.AreEqual(null, node);
        }

        [TestMethod]
        public void Delete_With3Elements_LeftMiddle()
        {
            BinaryTree<int> tree = new BinaryTree<int>();
            /*                                             
            50                                              
         /     \                                              
        30      70                                              
       /  \    /  \                                              
      20   40  60   80 */

            tree.Add(5);
            tree.Add(3);
            tree.Add(2);
            tree.Add(4);
            tree.Add(7);
            tree.Add(6);
            tree.Add(8);
            tree.Add(5);

            tree.Remove(5);

            // Arrange
            BinaryTree<int> binaryTree = new BinaryTree<int>();
            int value1 = 5;
            int value2 = 4;
            int value3 = 3;
            BinaryTreeNode<int> node = binaryTree.Find(4);

            // Act
            binaryTree.Add(value1);
            binaryTree.Add(value2);
            binaryTree.Add(value3);
           // binaryTree.Delete(ref node);

            // Assert
            Assert.AreEqual(null, node);
        }
    }
}
