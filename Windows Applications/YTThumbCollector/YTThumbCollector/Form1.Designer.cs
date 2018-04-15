namespace YTThumbCollector
{
    partial class TheForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(TheForm));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.label1 = new System.Windows.Forms.Label();
            this.tbVideoIDList = new System.Windows.Forms.TextBox();
            this.rbVideoID = new System.Windows.Forms.RadioButton();
            this.rbVideoName = new System.Windows.Forms.RadioButton();
            this.label2 = new System.Windows.Forms.Label();
            this.btnReset = new System.Windows.Forms.Button();
            this.btnRun = new System.Windows.Forms.Button();
            this.panelWorking = new System.Windows.Forms.Panel();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.lblWorking = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.tbFolder = new System.Windows.Forms.TextBox();
            this.btnSaveLocation = new System.Windows.Forms.Button();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.rbInOrder = new System.Windows.Forms.RadioButton();
            this.menuStrip1.SuspendLayout();
            this.panelWorking.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(913, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.exitToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "File";
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(92, 22);
            this.exitToolStripMenuItem.Text = "Exit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.exitToolStripMenuItem_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 55);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(70, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Video ID List:";
            // 
            // tbVideoIDList
            // 
            this.tbVideoIDList.Location = new System.Drawing.Point(89, 52);
            this.tbVideoIDList.Multiline = true;
            this.tbVideoIDList.Name = "tbVideoIDList";
            this.tbVideoIDList.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.tbVideoIDList.Size = new System.Drawing.Size(222, 243);
            this.tbVideoIDList.TabIndex = 2;
            // 
            // rbVideoID
            // 
            this.rbVideoID.AutoSize = true;
            this.rbVideoID.Location = new System.Drawing.Point(480, 53);
            this.rbVideoID.Name = "rbVideoID";
            this.rbVideoID.Size = new System.Drawing.Size(66, 17);
            this.rbVideoID.TabIndex = 3;
            this.rbVideoID.TabStop = true;
            this.rbVideoID.Text = "Video ID";
            this.rbVideoID.UseVisualStyleBackColor = true;
            // 
            // rbVideoName
            // 
            this.rbVideoName.AutoSize = true;
            this.rbVideoName.Location = new System.Drawing.Point(480, 76);
            this.rbVideoName.Name = "rbVideoName";
            this.rbVideoName.Size = new System.Drawing.Size(83, 17);
            this.rbVideoName.TabIndex = 4;
            this.rbVideoName.TabStop = true;
            this.rbVideoName.Text = "Video Name";
            this.rbVideoName.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(336, 55);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(138, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Image Naming Convention: ";
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(339, 272);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(75, 23);
            this.btnReset.TabIndex = 7;
            this.btnReset.Text = "Clear List";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // btnRun
            // 
            this.btnRun.Location = new System.Drawing.Point(420, 272);
            this.btnRun.Name = "btnRun";
            this.btnRun.Size = new System.Drawing.Size(75, 23);
            this.btnRun.TabIndex = 8;
            this.btnRun.Text = "Collect!";
            this.btnRun.UseVisualStyleBackColor = true;
            this.btnRun.Click += new System.EventHandler(this.btnRun_Click);
            // 
            // panelWorking
            // 
            this.panelWorking.Controls.Add(this.pictureBox1);
            this.panelWorking.Controls.Add(this.lblWorking);
            this.panelWorking.Location = new System.Drawing.Point(584, 52);
            this.panelWorking.Name = "panelWorking";
            this.panelWorking.Size = new System.Drawing.Size(304, 243);
            this.panelWorking.TabIndex = 9;
            this.panelWorking.Visible = false;
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.pictureBox1.Image = global::YTThumbCollector.Properties.Resources.loading_progress;
            this.pictureBox1.Location = new System.Drawing.Point(38, 44);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(231, 196);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 1;
            this.pictureBox1.TabStop = false;
            // 
            // lblWorking
            // 
            this.lblWorking.Dock = System.Windows.Forms.DockStyle.Top;
            this.lblWorking.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblWorking.Location = new System.Drawing.Point(0, 0);
            this.lblWorking.Name = "lblWorking";
            this.lblWorking.Size = new System.Drawing.Size(304, 41);
            this.lblWorking.TabIndex = 0;
            this.lblWorking.Text = "Working? NO!";
            this.lblWorking.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(339, 140);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(82, 13);
            this.label3.TabIndex = 10;
            this.label3.Text = "Save Location: ";
            // 
            // tbFolder
            // 
            this.tbFolder.Location = new System.Drawing.Point(420, 137);
            this.tbFolder.Name = "tbFolder";
            this.tbFolder.ReadOnly = true;
            this.tbFolder.Size = new System.Drawing.Size(143, 20);
            this.tbFolder.TabIndex = 11;
            // 
            // btnSaveLocation
            // 
            this.btnSaveLocation.Location = new System.Drawing.Point(488, 163);
            this.btnSaveLocation.Name = "btnSaveLocation";
            this.btnSaveLocation.Size = new System.Drawing.Size(75, 23);
            this.btnSaveLocation.TabIndex = 12;
            this.btnSaveLocation.Text = "Browse";
            this.btnSaveLocation.UseVisualStyleBackColor = true;
            this.btnSaveLocation.Click += new System.EventHandler(this.btnSaveLocation_Click);
            // 
            // rbInOrder
            // 
            this.rbInOrder.AutoSize = true;
            this.rbInOrder.Location = new System.Drawing.Point(480, 99);
            this.rbInOrder.Name = "rbInOrder";
            this.rbInOrder.Size = new System.Drawing.Size(103, 17);
            this.rbInOrder.TabIndex = 13;
            this.rbInOrder.TabStop = true;
            this.rbInOrder.Text = "Numbered Order";
            this.rbInOrder.UseVisualStyleBackColor = true;
            // 
            // TheForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(913, 333);
            this.Controls.Add(this.rbInOrder);
            this.Controls.Add(this.btnSaveLocation);
            this.Controls.Add(this.tbFolder);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.panelWorking);
            this.Controls.Add(this.btnRun);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.rbVideoName);
            this.Controls.Add(this.rbVideoID);
            this.Controls.Add(this.tbVideoIDList);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "TheForm";
            this.Text = "YouTube Thumbnail Collector";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.panelWorking.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tbVideoIDList;
        private System.Windows.Forms.RadioButton rbVideoID;
        private System.Windows.Forms.RadioButton rbVideoName;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btnReset;
        private System.Windows.Forms.Button btnRun;
        private System.Windows.Forms.Panel panelWorking;
        private System.Windows.Forms.Label lblWorking;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbFolder;
        private System.Windows.Forms.Button btnSaveLocation;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.RadioButton rbInOrder;
    }
}

