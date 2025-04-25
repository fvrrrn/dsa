using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using MyCollectionsLibrary;

namespace UnitTest
{
    [TestClass]
    public class MyHashSetTest
    {
        [TestMethod]
        public void AddLetterA()
        {
            // Arrange
            MyHashSet<int> myHashSet = new MyHashSet<int>();
            
            // Act
            myHashSet.Add("a", 1);

            // Assert
            Assert.AreEqual(1, myHashSet["a"]);
        }

        [TestMethod]
        public void AddLetterZ()
        {
            // Arrange
            MyHashSet<int> myHashSet = new MyHashSet<int>();

            // Act
            myHashSet.Add("z", 1);

            // Assert
            Assert.AreEqual(1, myHashSet["z"]);
        }

        [TestMethod]
        public void AddLettersAZ()
        {
            // Arrange
            MyHashSet<int> myHashSet = new MyHashSet<int>();

            // Act
            myHashSet.Add("az", 1);

            // Assert
            Assert.AreEqual(1, myHashSet["az"]);
        }

        [TestMethod]
        public void AddLettersZA()
        {
            // Arrange
            MyHashSet<int> myHashSet = new MyHashSet<int>();

            // Act
            myHashSet.Add("za", 1);

            // Assert
            Assert.AreEqual(1, myHashSet["za"]);
        }

        [TestMethod]
        public void AddLettersZAF()
        {
            // Arrange
            MyHashSet<int> myHashSet = new MyHashSet<int>();

            // Act
            myHashSet.Add("zaf", 1);

            // Assert
            Assert.AreEqual(1, myHashSet["zaf"]);
        }
    }
}
