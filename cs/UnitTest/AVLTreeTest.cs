using System;
using MyCollectionsLibrary;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace UnitTest
{
    [TestClass]
    public class AVLTreeTest
    {
        [TestMethod]
        public void TestMethod1()
        {
            var tree = new AVLTree<int>();

            // Act
            tree.Add(30);
            tree.Add(29);
            tree.Add(28);
        }
    }
}
