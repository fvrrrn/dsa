using System;
using System.Windows.Forms;

namespace WindowsApp1
{
    public partial class MyQueueForm : Form
    {
        private SBClientQueuer sbQueuer;
        private Random random;
        private Timer timer;
        private float multiplier;

        public MyQueueForm()
        {
            InitializeComponent();
            multiplier = trackBar1.Value / 5;
            sbQueuer = new SBClientQueuer(3);
            random = new Random();
            timer = new Timer();
            timer.Tick += Timer_Tick;
            timer.Interval = (int)(1000 * multiplier);
            timer.Start();
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            if (sbQueuer.Servants[0].CurrentClient == -1)
            {
                if (sbQueuer.Queue.Count != 0)
                {
                    sbQueuer.Servants[0].Add(sbQueuer.Queue.Pop());
                }
                else
                {
                    label1.Text = "Available";
                    textBox1.Text = "";
                }
                UpdateListBox();
            }
            else
            {
                label1.Text = sbQueuer.Servants[0].ElapsedTime.ToString();
                textBox1.Text = sbQueuer.Servants[0].CurrentClient.ToString();
            }

            if (sbQueuer.Servants[1].CurrentClient == -1)
            {
                if (sbQueuer.Queue.Count != 0)
                {
                    sbQueuer.Servants[1].Add(sbQueuer.Queue.Pop());
                }
                else
                {
                    label2.Text = "Available";
                    textBox2.Text = "";
                }
                UpdateListBox();
            }
            else
            {
                
                label2.Text = sbQueuer.Servants[1].ElapsedTime.ToString();
                textBox2.Text = sbQueuer.Servants[1].CurrentClient.ToString();
            }

            if (sbQueuer.Servants[2].CurrentClient == -1)
            {
                if (sbQueuer.Queue.Count != 0)
                {
                    sbQueuer.Servants[2].Add(sbQueuer.Queue.Pop());
                }
                else
                {
                    label3.Text = "Available";
                    textBox3.Text = "";
                }
                UpdateListBox();
            }
            else
            {
                label3.Text = sbQueuer.Servants[2].ElapsedTime.ToString();
                textBox3.Text = sbQueuer.Servants[2].CurrentClient.ToString();
            }

            timer.Enabled = true;
        }

        private void ButtonAddClient_Click(object sender, EventArgs e)
        {
            sbQueuer.AddClient(random.Next(11));
            UpdateListBox();
        }

        private void UpdateListBox()
        {
            listBox1.Items.Clear();
            foreach (var item in sbQueuer.Queue)
            {
                listBox1.Items.Add(item);
            }
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            multiplier = (trackBar1.Value * 1.0f) / 5;
            timer.Interval = (int)(1000 * multiplier);
            foreach (SBServant servant in sbQueuer.Servants)
                servant.Timer.Interval = (int)(1000 * multiplier);
        }
    }
}
