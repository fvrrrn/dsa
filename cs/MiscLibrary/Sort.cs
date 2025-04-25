using System;
using System.Collections.Generic;
using System.Linq;

namespace MiscLibrary
{
    public static class Sort
    {
        public static void QuickSort<T>(this IList<T> list, int left, int right)
            where T : IComparable
        {
            T tmp;
            T pivot = list[(left + right) / 2];
            int i = left, j = right;
            while (i <= j)
            {
                while (Compare(list[i], pivot) == -1) i++;
                while (Compare(list[i], pivot) == 1) j--;
                if (i <= j)
                {
                    tmp = list[i];
                    list[i] = list[j];
                    list[j] = tmp;
                    i++; j--;
                }
            }
            if (left < j) list.QuickSort(left, j);
            if (right > i) list.QuickSort(i, right);
        }

        public static void MergeSort<T>(this IList<T> inputData)
            where T : IComparable
        {
            inputData.MergeSort(0, inputData.Count - 1);
        }

        public static void MergeSort<T>(this IList<T> inputData, int firstIndex, int lastIndex)
            where T : IComparable
        {
            // If the firstIndex is greater than the lastIndex then the recursion 
            // has divided the problem into a single item. Return back up the call 
            // stack.
            if (firstIndex >= lastIndex)
                return;

            int midIndex = (firstIndex + lastIndex) / 2;

            // Recursively divide the first and second halves of the inputData into
            // its two seperate parts.
            inputData.MergeSort(firstIndex, midIndex);
            inputData.MergeSort(midIndex + 1, lastIndex);

            // Merge the two remaining halves after dividing them in half.
            inputData.MergeExplicit(firstIndex, midIndex, lastIndex);
        }

        private static void MergeExplicit<T>(this IList<T> inputData, int firstIndex, int midIndex, int lastIndex)
            where T : IComparable
        {
            int currentLeft = firstIndex;
            int currentRight = midIndex + 1;

            T[] tempData = new T[(lastIndex - firstIndex) + 1];
            int tempPos = 0;

            // Check the items at the left most index of the two havles and compare
            // them. Add the items in ascending order into the tempData array.
            while (currentLeft <= midIndex && currentRight <= lastIndex)
                if (inputData.ElementAt(currentLeft).CompareTo(inputData.ElementAt(currentRight)) < 0)
                {
                    tempData[tempPos++] = inputData.ElementAt(currentLeft++);
                }
                else
                {
                    tempData[tempPos++] = inputData.ElementAt(currentRight++);
                }

            // If there are any remaining items to be added to the tempData array,
            // add them.

            while (currentLeft <= midIndex)
            {
                tempData[tempPos++] = inputData.ElementAt(currentLeft++);
            }

            while (currentRight <= lastIndex)
            {
                tempData[tempPos++] = inputData.ElementAt(currentRight++);
            }

            // Now that the items have been sorted, copy them back into the inputData
            // reference that was passed to this function.
            tempPos = 0;
            for (int i = firstIndex; i <= lastIndex; i++)
            {
                inputData.Insert(firstIndex, tempData.ElementAt(tempPos));
            }
        }

        public static int Compare<T>(T x, T y)
            where T : IComparable
        {
            return x.CompareTo(y);
        }
    }
}
