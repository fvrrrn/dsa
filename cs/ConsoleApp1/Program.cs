using MiscLibrary;
using MyCollectionsLibrary;
using System;

namespace ConsoleApp1
{
    class Program
    {
        static BSTree<int> btree = new BSTree<int>
            {
                20, 10, 30, 5, 15, 13, 19, 25, 23, 28, 40, 35
            };

        static Concordance concordance = new Concordance();

        static void Main()
        {
            RoadMap rd = new RoadMap(5, 8);
            rd.AddRoad(0, 1);
            rd.AddRoad(4, 3);
            rd.AddRoad(4, 0);
            rd.AddRoad(2, 3);
            rd.AddRoad(4, 1);
            rd.AddRoad(1, 3);
            rd.AddRoad(1, 2);
            rd.AddRoad(2, 0);

            rd.AddRoad(1, 0);
            rd.AddRoad(3, 4);
            rd.AddRoad(0, 4);
            rd.AddRoad(3, 2);
            rd.AddRoad(1, 4);
            rd.AddRoad(3, 1);
            rd.AddRoad(2, 1);
            rd.AddRoad(0, 2);

            rd.SetTownCost(0, 3);
            rd.SetTownCost(1, 6);
            rd.SetTownCost(2, 1);
            rd.SetTownCost(3, 7);
            rd.SetTownCost(4, 6);

            
            Console.WriteLine(rd.TryReach());


            //MyLinekdList<int> ses = new MyLinekdList<int>();
            //ses.AddToFront(5);

            //int[] array = new int[] { 4,9,7,6,2,3 };
            //foreach (var item in array) Console.Write(item + " ");
            //Console.WriteLine();
            //array = CompSort(array);

            //TowerOfHanoi(4, 'a', 'c', 'b');
            //BtreeTest();
            //string[] s = Concordance.Parse("Peter Piper picked a peck of pickled peppers A peck of pickled " +
            //    "peppers Peter Piper picked If Peter Piper picked a peck of " +
            //    "pickled peppers where is the peck that Peter Piper picked");
            //foreach (string item in s)
            //    concordance.Add(item);

            //ConcordanceTest();
            Console.ReadKey();
        }

        public static T[] CompSort<T>(T[] array)
            where T : IComparable
        {
            int count = 0;
            int gap = array.Length;
            bool swapped = true;
            while (gap > 1 || swapped)
            {
                if (gap > 1)
                    gap = (int)(gap / 1.247330950103979);

                int i = 0;
                swapped = false;
                while (i + gap < array.Length)
                {
                    if (array[i].CompareTo(array[i + gap]) > 0)
                    {
                        T t = array[i];
                        array[i] = array[i + gap];
                        array[i + gap] = t;
                        swapped = true;
                        count++;
                    }
                    i++;
                }
            }
            return array;
        }

        static void TowerOfHanoi(int n, char from_rod, char to_rod, char aux_rod)
        {
            if (n == 1)
            {
                Console.WriteLine("Move disk 1 from rod " + from_rod + " to rod " + to_rod);
                return;
            }
            TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
            Console.WriteLine("Move disk " + n + " from rod " + from_rod + " to rod " + to_rod);
            TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
        }

        static void ConcordanceTest()
        {
            Console.Clear();
            Console.WriteLine(concordance.ToString());

            Console.WriteLine();

            string[] s = Console.ReadLine().Split();

            switch (s[0])
            {
                case "add":
                    concordance.Add(Console.ReadLine());
                    break;
                case "remove":
                    concordance.Remove(Console.ReadLine());
                    break;
                case "clear":
                    concordance.Clear();
                    break;
                case "lnr":
                    concordance.TraversalOrder = BSTree<string>.TraversalMode.LNR;
                    foreach (var item in concordance) Console.Write(item + " ");
                    Console.ReadKey();
                    break;
                case "rnl":
                    concordance.TraversalOrder = BSTree<string>.TraversalMode.RNL;
                    foreach (var item in concordance) Console.Write(item + " ");
                    Console.ReadKey();
                    break;
                case "nlr":
                    concordance.TraversalOrder = BSTree<string>.TraversalMode.NLR;
                    foreach (var item in concordance) Console.Write(item + " ");
                    Console.ReadKey();
                    break;
                case "exit":
                    return;
            }

            ConcordanceTest();
        }

        static void BtreeTest()
        {
            Console.Clear();
            Console.Write(btree.ToString());

            Console.WriteLine("Count: " + btree.Count);
            Console.WriteLine("Depth: " + btree.Depth);
            Console.WriteLine();

            string[] s = Console.ReadLine().Split();

            switch (s[0])
            {
                case "add":
                    btree.Add(int.Parse(s[1]));
                    break;
                case "remove":
                    btree.Remove(int.Parse(s[1]));
                    break;
                case "clear":
                    btree.Clear();
                    break;
                case "lnr":
                    btree.TraversalOrder = BSTree<int>.TraversalMode.LNR;
                    foreach (var item in btree) Console.Write(item.ToString() + " ");
                    Console.ReadKey();
                    break;
                case "rnl":
                    btree.TraversalOrder = BSTree<int>.TraversalMode.RNL;
                    foreach (var item in btree) Console.Write(item.ToString() + " ");
                    Console.ReadKey();
                    break;
                case "nlr":
                    btree.TraversalOrder = BSTree<int>.TraversalMode.NLR;
                    foreach (var item in btree) Console.Write(item.ToString() + " ");
                    Console.ReadKey();
                    break;
                case "exit":
                    return;
            }

            BtreeTest();
        }
    }
}
