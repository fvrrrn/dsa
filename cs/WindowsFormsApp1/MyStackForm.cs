using System;
using MyCollectionsLibrary;
using MiscLibrary;
using System.Windows.Forms;

namespace WindowsApp1
{
    public partial class MyStackForm : Form
    {
        MyStack<int> myIntStack;

        public MyStackForm()
        {
            myIntStack = new MyStack<int>();
            InitializeComponent();
        }

        private void ButtonPush_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBoxPushedItem.Text, out int result))
            {
                myIntStack.Push(result);
            }
            UpdateListBox();
        }

        private void ButtonPop_Click(object sender, EventArgs e)
        {
            if (myIntStack.IsEmpty()) { MessageBox.Show("Stack is empty."); return; }
            textBoxPoppedItem.Text = myIntStack.Pop().ToString();
            UpdateListBox();
        }

        private void ButtonPeek_Click(object sender, EventArgs e)
        {
            if (myIntStack.IsEmpty()) { MessageBox.Show("Stack is empty."); return; }
            textBoxCurrentItem.Text = myIntStack.Peek().ToString();
            UpdateListBox();
        }

        private void ButtonCheckBrackets_Click(object sender, EventArgs e)
        {
            if (BracketParser.Parse(textBoxBracketsString.Text))
                MessageBox.Show("Brackets sequence is correct");
            else
                MessageBox.Show("Brackets sequence is incorrect");
        }

        private void UpdateListBox()
        {
            listBox1.Items.Clear();
            foreach (var item in myIntStack)
            {
                listBox1.Items.Add(item);
            }
        }
    }
}
