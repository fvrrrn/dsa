namespace WindowsApp1
{
    partial class MyLinkedListForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.TextBoxInput1 = new System.Windows.Forms.TextBox();
            this.ButtonAddFirst = new System.Windows.Forms.Button();
            this.ButtonAddLast = new System.Windows.Forms.Button();
            this.ButtonAddAfter = new System.Windows.Forms.Button();
            this.ButtonAddBefore = new System.Windows.Forms.Button();
            this.TextBoxInput2 = new System.Windows.Forms.TextBox();
            this.ButtonRemove = new System.Windows.Forms.Button();
            this.LabelOutput = new System.Windows.Forms.Label();
            this.LabelCount = new System.Windows.Forms.Label();
            this.LabelFirst = new System.Windows.Forms.Label();
            this.LabelLast = new System.Windows.Forms.Label();
            this.ButtonClear = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(36, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Node:";
            // 
            // TextBoxInput1
            // 
            this.TextBoxInput1.Location = new System.Drawing.Point(51, 7);
            this.TextBoxInput1.Name = "TextBoxInput1";
            this.TextBoxInput1.Size = new System.Drawing.Size(19, 20);
            this.TextBoxInput1.TabIndex = 1;
            // 
            // ButtonAddFirst
            // 
            this.ButtonAddFirst.Location = new System.Drawing.Point(12, 32);
            this.ButtonAddFirst.Name = "ButtonAddFirst";
            this.ButtonAddFirst.Size = new System.Drawing.Size(58, 23);
            this.ButtonAddFirst.TabIndex = 2;
            this.ButtonAddFirst.Text = "Add First";
            this.ButtonAddFirst.UseVisualStyleBackColor = true;
            this.ButtonAddFirst.Click += new System.EventHandler(this.ButtonAddFirst_Click);
            // 
            // ButtonAddLast
            // 
            this.ButtonAddLast.Location = new System.Drawing.Point(76, 32);
            this.ButtonAddLast.Name = "ButtonAddLast";
            this.ButtonAddLast.Size = new System.Drawing.Size(57, 23);
            this.ButtonAddLast.TabIndex = 3;
            this.ButtonAddLast.Text = "Add Last";
            this.ButtonAddLast.UseVisualStyleBackColor = true;
            this.ButtonAddLast.Click += new System.EventHandler(this.ButtonAddLast_Click);
            // 
            // ButtonAddAfter
            // 
            this.ButtonAddAfter.Location = new System.Drawing.Point(139, 34);
            this.ButtonAddAfter.Name = "ButtonAddAfter";
            this.ButtonAddAfter.Size = new System.Drawing.Size(75, 23);
            this.ButtonAddAfter.TabIndex = 7;
            this.ButtonAddAfter.Text = "Add After";
            this.ButtonAddAfter.UseVisualStyleBackColor = true;
            this.ButtonAddAfter.Click += new System.EventHandler(this.ButtonAddAfter_Click);
            // 
            // ButtonAddBefore
            // 
            this.ButtonAddBefore.Location = new System.Drawing.Point(139, 5);
            this.ButtonAddBefore.Name = "ButtonAddBefore";
            this.ButtonAddBefore.Size = new System.Drawing.Size(75, 23);
            this.ButtonAddBefore.TabIndex = 6;
            this.ButtonAddBefore.Text = "Add Before";
            this.ButtonAddBefore.UseVisualStyleBackColor = true;
            this.ButtonAddBefore.Click += new System.EventHandler(this.ButtonAddBefore_Click);
            // 
            // TextBoxInput2
            // 
            this.TextBoxInput2.Location = new System.Drawing.Point(220, 21);
            this.TextBoxInput2.Name = "TextBoxInput2";
            this.TextBoxInput2.Size = new System.Drawing.Size(41, 20);
            this.TextBoxInput2.TabIndex = 8;
            // 
            // ButtonRemove
            // 
            this.ButtonRemove.Location = new System.Drawing.Point(78, 4);
            this.ButtonRemove.Name = "ButtonRemove";
            this.ButtonRemove.Size = new System.Drawing.Size(55, 23);
            this.ButtonRemove.TabIndex = 9;
            this.ButtonRemove.Text = "Remove";
            this.ButtonRemove.UseVisualStyleBackColor = true;
            this.ButtonRemove.Click += new System.EventHandler(this.ButtonRemove_Click);
            // 
            // LabelOutput
            // 
            this.LabelOutput.AutoSize = true;
            this.LabelOutput.Location = new System.Drawing.Point(12, 70);
            this.LabelOutput.Name = "LabelOutput";
            this.LabelOutput.Size = new System.Drawing.Size(35, 13);
            this.LabelOutput.TabIndex = 11;
            this.LabelOutput.Text = "label3";
            // 
            // LabelCount
            // 
            this.LabelCount.AutoSize = true;
            this.LabelCount.Location = new System.Drawing.Point(12, 94);
            this.LabelCount.Name = "LabelCount";
            this.LabelCount.Size = new System.Drawing.Size(38, 13);
            this.LabelCount.TabIndex = 12;
            this.LabelCount.Text = "Count:";
            // 
            // LabelFirst
            // 
            this.LabelFirst.AutoSize = true;
            this.LabelFirst.Location = new System.Drawing.Point(84, 94);
            this.LabelFirst.Name = "LabelFirst";
            this.LabelFirst.Size = new System.Drawing.Size(29, 13);
            this.LabelFirst.TabIndex = 13;
            this.LabelFirst.Text = "First:";
            // 
            // LabelLast
            // 
            this.LabelLast.AutoSize = true;
            this.LabelLast.Location = new System.Drawing.Point(149, 94);
            this.LabelLast.Name = "LabelLast";
            this.LabelLast.Size = new System.Drawing.Size(30, 13);
            this.LabelLast.TabIndex = 14;
            this.LabelLast.Text = "Last:";
            // 
            // ButtonClear
            // 
            this.ButtonClear.Location = new System.Drawing.Point(209, 65);
            this.ButtonClear.Name = "ButtonClear";
            this.ButtonClear.Size = new System.Drawing.Size(51, 23);
            this.ButtonClear.TabIndex = 15;
            this.ButtonClear.Text = "Clear";
            this.ButtonClear.UseVisualStyleBackColor = true;
            this.ButtonClear.Click += new System.EventHandler(this.ButtonClear_Click);
            // 
            // MyLinkedListForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(272, 114);
            this.Controls.Add(this.ButtonClear);
            this.Controls.Add(this.LabelLast);
            this.Controls.Add(this.LabelFirst);
            this.Controls.Add(this.LabelCount);
            this.Controls.Add(this.LabelOutput);
            this.Controls.Add(this.ButtonRemove);
            this.Controls.Add(this.TextBoxInput2);
            this.Controls.Add(this.ButtonAddAfter);
            this.Controls.Add(this.ButtonAddBefore);
            this.Controls.Add(this.ButtonAddLast);
            this.Controls.Add(this.ButtonAddFirst);
            this.Controls.Add(this.TextBoxInput1);
            this.Controls.Add(this.label1);
            this.Name = "MyLinkedListForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MyLinkedListForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox TextBoxInput1;
        private System.Windows.Forms.Button ButtonAddFirst;
        private System.Windows.Forms.Button ButtonAddLast;
        private System.Windows.Forms.Button ButtonAddAfter;
        private System.Windows.Forms.Button ButtonAddBefore;
        private System.Windows.Forms.TextBox TextBoxInput2;
        private System.Windows.Forms.Button ButtonRemove;
        private System.Windows.Forms.Label LabelOutput;
        private System.Windows.Forms.Label LabelCount;
        private System.Windows.Forms.Label LabelFirst;
        private System.Windows.Forms.Label LabelLast;
        private System.Windows.Forms.Button ButtonClear;
    }
}