using MyCollectionsLibrary;

namespace WindowsApp1
{
    class SBClientQueuer
    {
        public MyQueue<int> Queue { get; private set; }
        public SBServant[] Servants { get; private set; }

        public SBClientQueuer(int capacity)
        {
            Queue = new MyQueue<int>();
            Servants = new SBServant[capacity];
            for (int i = 0; i < Servants.Length; i++)
            {
                Servants[i] = new SBServant();
            }
        }

        public bool AddClient(int number)
        {
            return Queue.Push(number);
        }

        public bool AssignClient()
        {
            for (int i = 0; i < Servants.Length; i++)
            {
                if (Servants[i].IsAvailable())
                {
                    Servants[i].Add(Queue.Pop());
                    return true;
                }
            }
            return false;
        }

        public bool EaseServant(int servantIndex)
        {
            return Servants[servantIndex].Remove();
        }
    }
}
