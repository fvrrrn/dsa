using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using MyCollectionsLibrary;

namespace UnitTest
{
    [TestClass]
    public class MyLinekdListTest
    {
        [TestMethod]
        public void AddToFront_WithNoElements_ReturnsThisAsFirst()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();
            int value = 1;

            // Act
            listTest.AddToFront(value);

            // Assert
            Assert.AreEqual(listTest.First.Value, value);
        }

        [TestMethod]
        public void AddToFront_WithOneElement_ReturnsThisAsFirst()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();
            int value1 = 1;
            int value2 = 2;

            // Act
            listTest.AddToFront(value1);
            listTest.AddToFront(value2);

            // Assert
            Assert.AreEqual(listTest.First.Value, value2);
        }

        [TestMethod]
        public void GetAt_WithNoElements_ReturnsNull()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();
            int index = 1;

            // Act
            var item = listTest.GetAt(index);

            // Assert
            Assert.AreEqual(null, item);
        }

        [TestMethod]
        public void GetAt_With1Element_ReturnsElement()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();
            int index = 0;
            int value = 5;

            // Act
            listTest.AddToFront(value);
            var item = listTest.GetAt(index);

            // Assert
            Assert.AreEqual(value, item.Value);
        }

        [TestMethod]
        public void GetAt_With1ElementAndIndexOutOfRange_ReturnsNull()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();
            int index = 1;
            int value = 5;

            // Act
            listTest.AddToFront(value);
            var item = listTest.GetAt(index);

            // Assert
            Assert.AreEqual(null, item);
        }

        [TestMethod]
        public void GetAt_With2ElementsIndex1_ReturnsLast()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();
            int index = 1;
            int value1 = 5;
            int value2 = 6;

            // Act
            listTest.AddToFront(value2);
            listTest.AddToFront(value1);
            var item = listTest.GetAt(index);
            

            // Assert
            Assert.AreEqual(listTest.Last, item);
        }

        [TestMethod]
        public void SplitAt_WithEmptyList_ReturnsEmptyList()
        {
            // Arrange
            MyLinekdList<int> listTest = new MyLinekdList<int>();

            // Act

            // Assert
            Assert.AreEqual(listTest, listTest.SplitAt(1));
        }

        [TestMethod]
        public void ConcatAt_With2Lists_ReturnsLast()
        {
            // Arrange
            MyLinekdList<int> listTest1 = new MyLinekdList<int>();
            var listTest2 = new MyLinekdList<int>();
            var result = new MyLinekdList<int>();
            int index = 1;
            int value1 = 5;
            int value2 = 6;

            // Act
            result.AddToBack(5);
            result.AddToBack(7);
            result.AddToBack(8);
            listTest1.AddToFront(value2);
            listTest1.AddToFront(value1);
            listTest2.AddToBack(7);
            listTest2.AddToBack(8);


            // Assert
            Assert.AreEqual(result, listTest1.ConcatAt(listTest2, index));
        }

        [TestMethod]
        public void RemoveAt_With1Element_ReturnsElement()
        {
            // Arrange
            var listTest = new MyLinekdList<int>();
            int index = 0;
            int value = 5;

            // Act
            listTest.AddToBack(value);
            var result = listTest.RemoveAt(index);

            // Assert
            Assert.AreEqual(value, result.Value);
        }

        [TestMethod]
        public void SplitAt_With1Element_ReturnsElement()
        {
            // Arrange
            var listTest1 = new MyLinekdList<int>();
            var listTest2 = new MyLinekdList<int>();

            int index = 0;
            int value = 5;

            // Act
            listTest1.AddToBack(value);
            listTest2.AddToBack(value);
            var result = listTest1.SplitAt(index);           

            // Assert
            Assert.AreEqual(listTest2, result);
        }

        [TestMethod]
        public void ConcatAt_With2Lists_ReturnsConcatedList()
        {
            // Arrange
            var listTest1 = new MyLinekdList<int>();
            var listTest2 = new MyLinekdList<int>();
            var result = new MyLinekdList<int>();
            int index = 1;
            int value1 = 5;
            int value2 = 6;

            // Act
            result.AddToBack(5);
            result.AddToBack(7);
            result.AddToBack(8);
            listTest1.AddToFront(value2);
            listTest1.AddToFront(value1);
            listTest2.AddToBack(7);
            listTest2.AddToBack(8);


            // Assert
            Assert.AreEqual(result, listTest1.ConcatAt(listTest2, index));
        }
    }
}
