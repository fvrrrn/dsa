using System;
using System.Windows.Forms;
using MiscLibrary;

namespace WindowsApp1
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            labelResult.Text = "";
        }

        private void ButtonCalculate_Click(object sender, EventArgs e)
        {
            labelResult.Text = RPNParser.CalculateRPN(
                RPNParser.ToRPN(textBoxInput.Text)
                ).ToString();
        }
    }
}
