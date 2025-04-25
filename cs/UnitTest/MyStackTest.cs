using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using MyCollectionsLibrary;

namespace UnitTest
{
    [TestClass]
    public class MyStackTest
    {
        [TestMethod]
        public void Push_1Item_ReturnFirst()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int item1 = 5;

            // Act
            myStack.Push(item1);

            // Assert
            Assert.AreEqual(item1, myStack.Peek());
        }

        [TestMethod]
        public void Push_2Items_ReturnFirst()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int item1 = 5;
            int item2 = 6;

            // Act
            myStack.Push(item1);
            myStack.Push(item2);

            // Assert
            Assert.AreEqual(item2, myStack.Peek());
        }

        [TestMethod]
        public void Push_3Items_ReturnFirst()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int item1 = 5;
            int item2 = 6;
            int item3 = 7;

            // Act
            myStack.Push(item1);
            myStack.Push(item2);
            myStack.Push(item3);

            // Assert
            Assert.AreEqual(item3, myStack.Peek());
        }

        [TestMethod]
        public void Pop_WithNoItems_ReturnNullReferenceException()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            bool b = false;

            // Act
            try
            {
                myStack.Pop();
            }
            catch (NullReferenceException)
            {
                b = true;
            }

            // Assert
            Assert.IsTrue(b);
        }

        [TestMethod]
        public void Pop_1Item_ReturnLast()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int item1 = 5;
            int item2 = 6;

            // Act
            myStack.Push(item1);
            myStack.Push(item2);
            myStack.Pop();

            // Assert
            Assert.AreEqual(item1, myStack.Peek());
        }

        [TestMethod]
        public void Pop_1Item_ReturnStackEmpty()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int item1 = 5;

            // Act
            myStack.Push(item1);
            myStack.Pop();

            // Assert
            Assert.AreEqual(0, myStack.Count);
        }

        [TestMethod]
        public void Peek_WithNoItems_ReturnNullReferenceException()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            bool b = false;

            // Act
            try
            {
                myStack.Peek();
            }
            catch (NullReferenceException)
            {
                b = true;
            }

            // Assert
            Assert.IsTrue(b);
        }

        [TestMethod]
        public void Peek_With1Item_ReturnLast()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int item1 = 1;

            // Act
            myStack.Push(item1);

            // Assert
            Assert.AreEqual(item1, myStack.Peek());
        }

        [TestMethod]
        public void Peek_With2Items_ReturnStackNotChanged()
        {
            // Arrange
            MyStack<int> myStack = new MyStack<int>();
            int c;
            int item1 = 1;
            int item2 = 2;

            // Act
            myStack.Push(item1);
            myStack.Push(item2);
            c = 2;

            // Assert
            Assert.AreEqual(c, myStack.Count);
        }
    }
}
