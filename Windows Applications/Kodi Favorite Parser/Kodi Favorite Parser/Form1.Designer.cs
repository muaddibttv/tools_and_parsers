namespace Kodi_Favorites_Parser
{
    partial class MainForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.gbSelectFavFile = new System.Windows.Forms.GroupBox();
            this.btnParseFile = new System.Windows.Forms.Button();
            this.lblFavCount = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.lblFavFile = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.btnSelectFile = new System.Windows.Forms.Button();
            this.pnlResults = new System.Windows.Forms.Panel();
            this.dgvFavs = new System.Windows.Forms.DataGridView();
            this.selectFavFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.gbEditor = new System.Windows.Forms.GroupBox();
            this.btnSaveEdit = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.tbThumb = new System.Windows.Forms.TextBox();
            this.tbShorcut = new System.Windows.Forms.TextBox();
            this.tbTitle = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnReset = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.rbYTMenuFile = new System.Windows.Forms.RadioButton();
            this.rbPlain = new System.Windows.Forms.RadioButton();
            this.label6 = new System.Windows.Forms.Label();
            this.btnMakeMenu = new System.Windows.Forms.Button();
            this.rbVideo = new System.Windows.Forms.RadioButton();
            this.rbChannel = new System.Windows.Forms.RadioButton();
            this.rbPlaylist = new System.Windows.Forms.RadioButton();
            this.rbYTVideo = new System.Windows.Forms.RadioButton();
            this.rbURL = new System.Windows.Forms.RadioButton();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.cbShortcut = new System.Windows.Forms.CheckBox();
            this.cbThumb = new System.Windows.Forms.CheckBox();
            this.cbTitle = new System.Windows.Forms.CheckBox();
            this.tbMenuFile = new System.Windows.Forms.TextBox();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.btnCleanChannels = new System.Windows.Forms.Button();
            this.btnCleanPlaylists = new System.Windows.Forms.Button();
            this.btnCleanVideos = new System.Windows.Forms.Button();
            this.cbGenForAll = new System.Windows.Forms.CheckBox();
            this.gbSelectFavFile.SuspendLayout();
            this.pnlResults.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvFavs)).BeginInit();
            this.gbEditor.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // gbSelectFavFile
            // 
            this.gbSelectFavFile.Controls.Add(this.btnCleanVideos);
            this.gbSelectFavFile.Controls.Add(this.btnCleanPlaylists);
            this.gbSelectFavFile.Controls.Add(this.btnCleanChannels);
            this.gbSelectFavFile.Controls.Add(this.label9);
            this.gbSelectFavFile.Controls.Add(this.btnParseFile);
            this.gbSelectFavFile.Controls.Add(this.lblFavCount);
            this.gbSelectFavFile.Controls.Add(this.label2);
            this.gbSelectFavFile.Controls.Add(this.lblFavFile);
            this.gbSelectFavFile.Controls.Add(this.label1);
            this.gbSelectFavFile.Controls.Add(this.btnSelectFile);
            this.gbSelectFavFile.Location = new System.Drawing.Point(12, 60);
            this.gbSelectFavFile.Name = "gbSelectFavFile";
            this.gbSelectFavFile.Size = new System.Drawing.Size(547, 145);
            this.gbSelectFavFile.TabIndex = 0;
            this.gbSelectFavFile.TabStop = false;
            this.gbSelectFavFile.Text = "Select Favorites XML File";
            // 
            // btnParseFile
            // 
            this.btnParseFile.Enabled = false;
            this.btnParseFile.Location = new System.Drawing.Point(96, 64);
            this.btnParseFile.Name = "btnParseFile";
            this.btnParseFile.Size = new System.Drawing.Size(75, 23);
            this.btnParseFile.TabIndex = 5;
            this.btnParseFile.Text = "Parse File";
            this.btnParseFile.UseVisualStyleBackColor = true;
            this.btnParseFile.Click += new System.EventHandler(this.btnParseFile_Click);
            // 
            // lblFavCount
            // 
            this.lblFavCount.AutoSize = true;
            this.lblFavCount.Location = new System.Drawing.Point(105, 97);
            this.lblFavCount.Name = "lblFavCount";
            this.lblFavCount.Size = new System.Drawing.Size(0, 13);
            this.lblFavCount.TabIndex = 4;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 97);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(87, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Favorites Count: ";
            // 
            // lblFavFile
            // 
            this.lblFavFile.AutoSize = true;
            this.lblFavFile.Location = new System.Drawing.Point(47, 38);
            this.lblFavFile.Name = "lblFavFile";
            this.lblFavFile.Size = new System.Drawing.Size(85, 13);
            this.lblFavFile.TabIndex = 2;
            this.lblFavFile.Text = "No File Selected";
            this.lblFavFile.TextChanged += new System.EventHandler(this.lblFavFile_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 38);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(29, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "File: ";
            // 
            // btnSelectFile
            // 
            this.btnSelectFile.Location = new System.Drawing.Point(15, 64);
            this.btnSelectFile.Name = "btnSelectFile";
            this.btnSelectFile.Size = new System.Drawing.Size(75, 23);
            this.btnSelectFile.TabIndex = 0;
            this.btnSelectFile.Text = "Select File";
            this.btnSelectFile.UseVisualStyleBackColor = true;
            this.btnSelectFile.Click += new System.EventHandler(this.btnSelectFile_Click);
            // 
            // pnlResults
            // 
            this.pnlResults.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.pnlResults.Controls.Add(this.dgvFavs);
            this.pnlResults.Location = new System.Drawing.Point(12, 376);
            this.pnlResults.Name = "pnlResults";
            this.pnlResults.Size = new System.Drawing.Size(1399, 312);
            this.pnlResults.TabIndex = 1;
            // 
            // dgvFavs
            // 
            this.dgvFavs.AllowUserToAddRows = false;
            this.dgvFavs.AllowUserToOrderColumns = true;
            this.dgvFavs.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvFavs.Dock = System.Windows.Forms.DockStyle.Fill;
            this.dgvFavs.Location = new System.Drawing.Point(0, 0);
            this.dgvFavs.Name = "dgvFavs";
            this.dgvFavs.Size = new System.Drawing.Size(1399, 312);
            this.dgvFavs.TabIndex = 0;
            this.dgvFavs.RowEnter += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgvFavs_RowEnter);
            // 
            // selectFavFileDialog
            // 
            this.selectFavFileDialog.FileName = "favourites.xml";
            this.selectFavFileDialog.Filter = "Kodi Favourites | favourites.xml";
            // 
            // gbEditor
            // 
            this.gbEditor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.gbEditor.Controls.Add(this.btnSaveEdit);
            this.gbEditor.Controls.Add(this.button1);
            this.gbEditor.Controls.Add(this.tbThumb);
            this.gbEditor.Controls.Add(this.tbShorcut);
            this.gbEditor.Controls.Add(this.tbTitle);
            this.gbEditor.Controls.Add(this.label5);
            this.gbEditor.Controls.Add(this.label4);
            this.gbEditor.Controls.Add(this.label3);
            this.gbEditor.Location = new System.Drawing.Point(565, 60);
            this.gbEditor.Name = "gbEditor";
            this.gbEditor.Size = new System.Drawing.Size(846, 145);
            this.gbEditor.TabIndex = 6;
            this.gbEditor.TabStop = false;
            this.gbEditor.Text = "Favourites Editor";
            // 
            // btnSaveEdit
            // 
            this.btnSaveEdit.Location = new System.Drawing.Point(422, 97);
            this.btnSaveEdit.Name = "btnSaveEdit";
            this.btnSaveEdit.Size = new System.Drawing.Size(75, 23);
            this.btnSaveEdit.TabIndex = 23;
            this.btnSaveEdit.Text = "Save";
            this.btnSaveEdit.UseVisualStyleBackColor = true;
            this.btnSaveEdit.Click += new System.EventHandler(this.btnSaveEdit_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(6, 97);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 22;
            this.button1.Text = "Reset";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // tbThumb
            // 
            this.tbThumb.Location = new System.Drawing.Point(83, 61);
            this.tbThumb.Name = "tbThumb";
            this.tbThumb.Size = new System.Drawing.Size(339, 20);
            this.tbThumb.TabIndex = 7;
            // 
            // tbShorcut
            // 
            this.tbShorcut.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tbShorcut.Location = new System.Drawing.Point(503, 35);
            this.tbShorcut.Multiline = true;
            this.tbShorcut.Name = "tbShorcut";
            this.tbShorcut.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.tbShorcut.Size = new System.Drawing.Size(337, 85);
            this.tbShorcut.TabIndex = 6;
            // 
            // tbTitle
            // 
            this.tbTitle.Location = new System.Drawing.Point(54, 35);
            this.tbTitle.Name = "tbTitle";
            this.tbTitle.Size = new System.Drawing.Size(368, 20);
            this.tbTitle.TabIndex = 5;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(15, 38);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(33, 13);
            this.label5.TabIndex = 4;
            this.label5.Text = "Title: ";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(15, 64);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(62, 13);
            this.label4.TabIndex = 3;
            this.label4.Text = "Thumbnail: ";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(447, 38);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(50, 13);
            this.label3.TabIndex = 2;
            this.label3.Text = "Shortcut:";
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.cbGenForAll);
            this.groupBox1.Controls.Add(this.btnReset);
            this.groupBox1.Controls.Add(this.panel1);
            this.groupBox1.Controls.Add(this.label6);
            this.groupBox1.Controls.Add(this.btnMakeMenu);
            this.groupBox1.Controls.Add(this.rbVideo);
            this.groupBox1.Controls.Add(this.rbChannel);
            this.groupBox1.Controls.Add(this.rbPlaylist);
            this.groupBox1.Controls.Add(this.rbYTVideo);
            this.groupBox1.Controls.Add(this.rbURL);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.cbShortcut);
            this.groupBox1.Controls.Add(this.cbThumb);
            this.groupBox1.Controls.Add(this.cbTitle);
            this.groupBox1.Controls.Add(this.tbMenuFile);
            this.groupBox1.Controls.Add(this.label10);
            this.groupBox1.Location = new System.Drawing.Point(12, 211);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(1399, 145);
            this.groupBox1.TabIndex = 7;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Tantrum.TV Menu Generator";
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(614, 97);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(75, 23);
            this.btnReset.TabIndex = 21;
            this.btnReset.Text = "Reset";
            this.btnReset.UseVisualStyleBackColor = true;
            this.btnReset.Click += new System.EventHandler(this.btnReset_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.rbYTMenuFile);
            this.panel1.Controls.Add(this.rbPlain);
            this.panel1.Location = new System.Drawing.Point(422, 45);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(136, 75);
            this.panel1.TabIndex = 20;
            // 
            // rbYTMenuFile
            // 
            this.rbYTMenuFile.AutoSize = true;
            this.rbYTMenuFile.Location = new System.Drawing.Point(3, 29);
            this.rbYTMenuFile.Name = "rbYTMenuFile";
            this.rbYTMenuFile.Size = new System.Drawing.Size(123, 17);
            this.rbYTMenuFile.TabIndex = 16;
            this.rbYTMenuFile.TabStop = true;
            this.rbYTMenuFile.Text = "TTV YouTube Menu";
            this.rbYTMenuFile.UseVisualStyleBackColor = true;
            // 
            // rbPlain
            // 
            this.rbPlain.AutoSize = true;
            this.rbPlain.Location = new System.Drawing.Point(3, 6);
            this.rbPlain.Name = "rbPlain";
            this.rbPlain.Size = new System.Drawing.Size(101, 17);
            this.rbPlain.TabIndex = 15;
            this.rbPlain.TabStop = true;
            this.rbPlain.Text = "Plain (For Skins)";
            this.rbPlain.UseVisualStyleBackColor = true;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(449, 26);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(80, 13);
            this.label6.TabIndex = 19;
            this.label6.Text = "Menu File Type";
            // 
            // btnMakeMenu
            // 
            this.btnMakeMenu.Location = new System.Drawing.Point(614, 68);
            this.btnMakeMenu.Name = "btnMakeMenu";
            this.btnMakeMenu.Size = new System.Drawing.Size(75, 23);
            this.btnMakeMenu.TabIndex = 6;
            this.btnMakeMenu.Text = "Generate";
            this.btnMakeMenu.UseVisualStyleBackColor = true;
            this.btnMakeMenu.Click += new System.EventHandler(this.btnMakeMenu_Click);
            // 
            // rbVideo
            // 
            this.rbVideo.AutoSize = true;
            this.rbVideo.Location = new System.Drawing.Point(183, 74);
            this.rbVideo.Name = "rbVideo";
            this.rbVideo.Size = new System.Drawing.Size(52, 17);
            this.rbVideo.TabIndex = 18;
            this.rbVideo.TabStop = true;
            this.rbVideo.Text = "Video";
            this.rbVideo.UseVisualStyleBackColor = true;
            // 
            // rbChannel
            // 
            this.rbChannel.AutoSize = true;
            this.rbChannel.Location = new System.Drawing.Point(271, 51);
            this.rbChannel.Name = "rbChannel";
            this.rbChannel.Size = new System.Drawing.Size(111, 17);
            this.rbChannel.TabIndex = 17;
            this.rbChannel.TabStop = true;
            this.rbChannel.Text = "YouTube Channel";
            this.rbChannel.UseVisualStyleBackColor = true;
            // 
            // rbPlaylist
            // 
            this.rbPlaylist.AutoSize = true;
            this.rbPlaylist.Location = new System.Drawing.Point(271, 74);
            this.rbPlaylist.Name = "rbPlaylist";
            this.rbPlaylist.Size = new System.Drawing.Size(104, 17);
            this.rbPlaylist.TabIndex = 16;
            this.rbPlaylist.TabStop = true;
            this.rbPlaylist.Text = "YouTube Playlist";
            this.rbPlaylist.UseVisualStyleBackColor = true;
            // 
            // rbYTVideo
            // 
            this.rbYTVideo.AutoSize = true;
            this.rbYTVideo.Location = new System.Drawing.Point(271, 97);
            this.rbYTVideo.Name = "rbYTVideo";
            this.rbYTVideo.Size = new System.Drawing.Size(99, 17);
            this.rbYTVideo.TabIndex = 15;
            this.rbYTVideo.TabStop = true;
            this.rbYTVideo.Text = "YouTube Video";
            this.rbYTVideo.UseVisualStyleBackColor = true;
            // 
            // rbURL
            // 
            this.rbURL.AutoSize = true;
            this.rbURL.Location = new System.Drawing.Point(183, 51);
            this.rbURL.Name = "rbURL";
            this.rbURL.Size = new System.Drawing.Size(47, 17);
            this.rbURL.TabIndex = 14;
            this.rbURL.TabStop = true;
            this.rbURL.Text = "URL";
            this.rbURL.UseVisualStyleBackColor = true;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(213, 26);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(113, 13);
            this.label8.TabIndex = 13;
            this.label8.Text = "Shortcut/URL Options";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(12, 26);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(77, 13);
            this.label7.TabIndex = 12;
            this.label7.Text = "Editor Includes";
            // 
            // cbShortcut
            // 
            this.cbShortcut.AutoSize = true;
            this.cbShortcut.Location = new System.Drawing.Point(15, 98);
            this.cbShortcut.Name = "cbShortcut";
            this.cbShortcut.Size = new System.Drawing.Size(93, 17);
            this.cbShortcut.TabIndex = 11;
            this.cbShortcut.Text = "Shortcut/URL";
            this.cbShortcut.UseVisualStyleBackColor = true;
            // 
            // cbThumb
            // 
            this.cbThumb.AutoSize = true;
            this.cbThumb.Location = new System.Drawing.Point(15, 75);
            this.cbThumb.Name = "cbThumb";
            this.cbThumb.Size = new System.Drawing.Size(85, 17);
            this.cbThumb.TabIndex = 10;
            this.cbThumb.Text = "Thumb/Icon";
            this.cbThumb.UseVisualStyleBackColor = true;
            // 
            // cbTitle
            // 
            this.cbTitle.AutoSize = true;
            this.cbTitle.Location = new System.Drawing.Point(15, 52);
            this.cbTitle.Name = "cbTitle";
            this.cbTitle.Size = new System.Drawing.Size(46, 17);
            this.cbTitle.TabIndex = 9;
            this.cbTitle.Text = "Title";
            this.cbTitle.UseVisualStyleBackColor = true;
            // 
            // tbMenuFile
            // 
            this.tbMenuFile.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tbMenuFile.Location = new System.Drawing.Point(695, 35);
            this.tbMenuFile.Multiline = true;
            this.tbMenuFile.Name = "tbMenuFile";
            this.tbMenuFile.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.tbMenuFile.Size = new System.Drawing.Size(698, 85);
            this.tbMenuFile.TabIndex = 6;
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(651, 38);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(38, 13);
            this.label10.TabIndex = 2;
            this.label10.Text = "Code: ";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(311, 69);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(122, 13);
            this.label9.TabIndex = 25;
            this.label9.Text = "Clean for YouTube Data";
            // 
            // btnCleanChannels
            // 
            this.btnCleanChannels.Enabled = false;
            this.btnCleanChannels.Location = new System.Drawing.Point(251, 92);
            this.btnCleanChannels.Name = "btnCleanChannels";
            this.btnCleanChannels.Size = new System.Drawing.Size(75, 23);
            this.btnCleanChannels.TabIndex = 26;
            this.btnCleanChannels.Text = "Channels";
            this.btnCleanChannels.UseVisualStyleBackColor = true;
            this.btnCleanChannels.Click += new System.EventHandler(this.btnCleanChannels_Click);
            // 
            // btnCleanPlaylists
            // 
            this.btnCleanPlaylists.Enabled = false;
            this.btnCleanPlaylists.Location = new System.Drawing.Point(332, 92);
            this.btnCleanPlaylists.Name = "btnCleanPlaylists";
            this.btnCleanPlaylists.Size = new System.Drawing.Size(75, 23);
            this.btnCleanPlaylists.TabIndex = 27;
            this.btnCleanPlaylists.Text = "Playlists";
            this.btnCleanPlaylists.UseVisualStyleBackColor = true;
            this.btnCleanPlaylists.Click += new System.EventHandler(this.btnCleanPlaylists_Click);
            // 
            // btnCleanVideos
            // 
            this.btnCleanVideos.Enabled = false;
            this.btnCleanVideos.Location = new System.Drawing.Point(413, 92);
            this.btnCleanVideos.Name = "btnCleanVideos";
            this.btnCleanVideos.Size = new System.Drawing.Size(75, 23);
            this.btnCleanVideos.TabIndex = 28;
            this.btnCleanVideos.Text = "Videos";
            this.btnCleanVideos.UseVisualStyleBackColor = true;
            this.btnCleanVideos.Click += new System.EventHandler(this.btnCleanVideos_Click);
            // 
            // cbGenForAll
            // 
            this.cbGenForAll.AutoSize = true;
            this.cbGenForAll.Location = new System.Drawing.Point(15, 121);
            this.cbGenForAll.Name = "cbGenForAll";
            this.cbGenForAll.Size = new System.Drawing.Size(151, 17);
            this.cbGenForAll.TabIndex = 22;
            this.cbGenForAll.Text = "Generate for All Favourites";
            this.cbGenForAll.UseVisualStyleBackColor = true;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1423, 700);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.gbEditor);
            this.Controls.Add(this.pnlResults);
            this.Controls.Add(this.gbSelectFavFile);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Kodi Favorites Parser";
            this.gbSelectFavFile.ResumeLayout(false);
            this.gbSelectFavFile.PerformLayout();
            this.pnlResults.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dgvFavs)).EndInit();
            this.gbEditor.ResumeLayout(false);
            this.gbEditor.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox gbSelectFavFile;
        private System.Windows.Forms.Button btnParseFile;
        private System.Windows.Forms.Label lblFavCount;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label lblFavFile;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnSelectFile;
        private System.Windows.Forms.Panel pnlResults;
        private System.Windows.Forms.DataGridView dgvFavs;
        private System.Windows.Forms.OpenFileDialog selectFavFileDialog;
        private System.Windows.Forms.GroupBox gbEditor;
        private System.Windows.Forms.TextBox tbThumb;
        private System.Windows.Forms.TextBox tbShorcut;
        private System.Windows.Forms.TextBox tbTitle;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button btnMakeMenu;
        private System.Windows.Forms.RadioButton rbVideo;
        private System.Windows.Forms.RadioButton rbChannel;
        private System.Windows.Forms.RadioButton rbPlaylist;
        private System.Windows.Forms.RadioButton rbYTVideo;
        private System.Windows.Forms.RadioButton rbURL;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.CheckBox cbShortcut;
        private System.Windows.Forms.CheckBox cbThumb;
        private System.Windows.Forms.CheckBox cbTitle;
        private System.Windows.Forms.TextBox tbMenuFile;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.RadioButton rbYTMenuFile;
        private System.Windows.Forms.RadioButton rbPlain;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button btnReset;
        private System.Windows.Forms.Button btnSaveEdit;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button btnCleanVideos;
        private System.Windows.Forms.Button btnCleanPlaylists;
        private System.Windows.Forms.Button btnCleanChannels;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.CheckBox cbGenForAll;
    }
}

