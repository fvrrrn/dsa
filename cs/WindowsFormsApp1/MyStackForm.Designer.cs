namespace WindowsApp1
{
    partial class MyStackForm
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
            this.ButtonPush = new System.Windows.Forms.Button();
            this.ButtonPop = new System.Windows.Forms.Button();
            this.ButtonPeek = new System.Windows.Forms.Button();
            this.textBoxPushedItem = new System.Windows.Forms.TextBox();
            this.textBoxPoppedItem = new System.Windows.Forms.TextBox();
            this.textBoxCurrentItem = new System.Windows.Forms.TextBox();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.ButtonCheckBrackets = new System.Windows.Forms.Button();
            this.textBoxBracketsString = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // ButtonPush
            // 
            this.ButtonPush.Location = new System.Drawing.Point(9, 10);
            this.ButtonPush.Name = "ButtonPush";
            this.ButtonPush.Size = new System.Drawing.Size(75, 23);
            this.ButtonPush.TabIndex = 0;
            this.ButtonPush.Text = "Push";
            this.ButtonPush.UseVisualStyleBackColor = true;
            this.ButtonPush.Click += new System.EventHandler(this.ButtonPush_Click);
            // 
            // ButtonPop
            // 
            this.ButtonPop.Location = new System.Drawing.Point(9, 39);
            this.ButtonPop.Name = "ButtonPop";
            this.ButtonPop.Size = new System.Drawing.Size(75, 23);
            this.ButtonPop.TabIndex = 1;
            this.ButtonPop.Text = "Pop";
            this.ButtonPop.UseVisualStyleBackColor = true;
            this.ButtonPop.Click += new System.EventHandler(this.ButtonPop_Click);
            // 
            // ButtonPeek
            // 
            this.ButtonPeek.Location = new System.Drawing.Point(9, 68);
            this.ButtonPeek.Name = "ButtonPeek";
            this.ButtonPeek.Size = new System.Drawing.Size(75, 23);
            this.ButtonPeek.TabIndex = 2;
            this.ButtonPeek.Text = "Peek";
            this.ButtonPeek.UseVisualStyleBackColor = true;
            this.ButtonPeek.Click += new System.EventHandler(this.ButtonPeek_Click);
            // 
            // textBoxPushedItem
            // 
            this.textBoxPushedItem.Location = new System.Drawing.Point(90, 12);
            this.textBoxPushedItem.Name = "textBoxPushedItem";
            this.textBoxPushedItem.Size = new System.Drawing.Size(100, 20);
            this.textBoxPushedItem.TabIndex = 3;
            // 
            // textBoxPoppedItem
            // 
            this.textBoxPoppedItem.Location = new System.Drawing.Point(90, 41);
            this.textBoxPoppedItem.Name = "textBoxPoppedItem";
            this.textBoxPoppedItem.Size = new System.Drawing.Size(100, 20);
            this.textBoxPoppedItem.TabIndex = 4;
            // 
            // textBoxCurrentItem
            // 
            this.textBoxCurrentItem.Location = new System.Drawing.Point(90, 70);
            this.textBoxCurrentItem.Name = "textBoxCurrentItem";
            this.textBoxCurrentItem.Size = new System.Drawing.Size(100, 20);
            this.textBoxCurrentItem.TabIndex = 5;
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.Location = new System.Drawing.Point(196, 12);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(81, 82);
            this.listBox1.TabIndex = 6;
            // 
            // ButtonCheckBrackets
            // 
            this.ButtonCheckBrackets.Location = new System.Drawing.Point(9, 138);
            this.ButtonCheckBrackets.Name = "ButtonCheckBrackets";
            this.ButtonCheckBrackets.Size = new System.Drawing.Size(268, 23);
            this.ButtonCheckBrackets.TabIndex = 7;
            this.ButtonCheckBrackets.Text = "Check brackets";
            this.ButtonCheckBrackets.UseVisualStyleBackColor = true;
            this.ButtonCheckBrackets.Click += new System.EventHandler(this.ButtonCheckBrackets_Click);
            // 
            // textBoxBracketsString
            // 
            this.textBoxBracketsString.Location = new System.Drawing.Point(9, 112);
            this.textBoxBracketsString.Name = "textBoxBracketsString";
            this.textBoxBracketsString.Size = new System.Drawing.Size(268, 20);
            this.textBoxBracketsString.TabIndex = 8;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(286, 171);
            this.Controls.Add(this.textBoxBracketsString);
            this.Controls.Add(this.ButtonCheckBrackets);
            this.Controls.Add(this.listBox1);
            this.Controls.Add(this.textBoxCurrentItem);
            this.Controls.Add(this.textBoxPoppedItem);
            this.Controls.Add(this.textBoxPushedItem);
            this.Controls.Add(this.ButtonPeek);
            this.Controls.Add(this.ButtonPop);
            this.Controls.Add(this.ButtonPush);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button ButtonPush;
        private System.Windows.Forms.Button ButtonPop;
        private System.Windows.Forms.Button ButtonPeek;
        private System.Windows.Forms.TextBox textBoxPushedItem;
        private System.Windows.Forms.TextBox textBoxPoppedItem;
        private System.Windows.Forms.TextBox textBoxCurrentItem;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.Button ButtonCheckBrackets;
        private System.Windows.Forms.TextBox textBoxBracketsString;
    }
}

