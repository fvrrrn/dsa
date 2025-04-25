using System.Windows.Forms;

namespace WindowsApp1
{
    class SBServant
    {
        public Timer Timer { get; set; }
        public int ElapsedTime { get; private set; }
        public int CurrentClient { get; private set; }
        private System.Random random; 

        public SBServant()
        {
            CurrentClient = -1;
            random = new System.Random();
            Timer = new Timer();
            Timer.Tick += Timer_Tick;
        }

        private void SetTimer()
        {
            ElapsedTime = random.Next(31);
            Timer.Interval = 1000;
            Timer.Enabled = true;
            Timer.Start();
        }

        private void Timer_Tick(object sender, System.EventArgs e)
        {
            if (ElapsedTime > 0) { ElapsedTime--; }
            else Remove();
        }

        public bool IsAvailable()
        {
            return CurrentClient == -1 ? true : false;
        }

        public bool Add(int clientNumber)
        {
            if (IsAvailable())
            {
                SetTimer();
                this.CurrentClient = clientNumber; return true;
            }
            else
            {
                return false;
            }
        }

        public bool Remove()
        {
            if (IsAvailable()) return false;
            CurrentClient = -1; return true; 
        }
    }
}
