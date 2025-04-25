using System;
using System.Windows.Forms;
using MyCollectionsLibrary;

namespace WindowsApp1
{
    public partial class MyLinkedListForm : Form
    {
        MyLinkedList<int> llist;
        public MyLinkedListForm()
        {
            InitializeComponent();
            llist = new MyLinkedList<int>();
        }

        private void ButtonAddFirst_Click(object sender, EventArgs e)
        {
            llist.AddFirst(int.Parse(TextBoxInput1.Text));
            UpdateResult();
        }

        private void ButtonAddLast_Click(object sender, EventArgs e)
        {
            llist.AddLast(int.Parse(TextBoxInput1.Text));
            UpdateResult();
        }

        private void ButtonAddBefore_Click(object sender, EventArgs e)
        {
            llist.AddBefore(int.Parse(TextBoxInput2.Text), int.Parse(TextBoxInput1.Text));
            UpdateResult();
        }

        private void ButtonAddAfter_Click(object sender, EventArgs e)
        {
            llist.AddAfter(int.Parse(TextBoxInput2.Text), int.Parse(TextBoxInput1.Text));
            UpdateResult();
        }

        private void ButtonRemove_Click(object sender, EventArgs e)
        {
            llist.Remove(int.Parse(TextBoxInput1.Text));
            UpdateResult();
        }

        public void UpdateResult()
        {
            LabelOutput.Text = "";
            foreach (var item in llist)
                LabelOutput.Text += item.ToString() + "<->";
            LabelCount.Text = llist.Count.ToString();
            LabelFirst.Text = "First: " + llist.First.Value.ToString();
            LabelLast.Text = "Last: " + llist.Last.Value.ToString();
        }

        private void ButtonClear_Click(object sender, EventArgs e)
        {
            llist.Clear();
            UpdateResult();
        }
    }
}
