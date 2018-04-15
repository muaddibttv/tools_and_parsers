namespace Tantrum_IPTV_Editor
{
    partial class Editor
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

      

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        /// 
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Editor));
            this.menuStrip = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.newListToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openFileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openURLToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.importToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.importKodiIPTVListToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.importSimpleIPTVListToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exportToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exportKodiIPTVListToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exportSimpleIPTVListToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.optionsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reporrtDuplicatesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.helpToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.documentationHowToToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStrip = new System.Windows.Forms.ToolStrip();
            this.toolStripButton1 = new System.Windows.Forms.ToolStripButton();
            this.toolStripOpenFile = new System.Windows.Forms.ToolStripButton();
            this.toolStripOpenURL = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripSave = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripNew = new System.Windows.Forms.ToolStripButton();
            this.toolStripRemove = new System.Windows.Forms.ToolStripButton();
            this.toolStripDuplicate = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripBtnCopyName = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator6 = new System.Windows.Forms.ToolStripSeparator();
            this.toolStripBtnClearDuplicates = new System.Windows.Forms.ToolStripButton();
            this.toolStripBtnVerifyLinks = new System.Windows.Forms.ToolStripButton();
            this.toolStripBtnRemoveDeadLinks = new System.Windows.Forms.ToolStripButton();
            this.toolStripBtnExportHosts = new System.Windows.Forms.ToolStripButton();
            this.toolStripSeparator7 = new System.Windows.Forms.ToolStripSeparator();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.channelsGrid = new System.Windows.Forms.DataGridView();
            this.panel1 = new System.Windows.Forms.Panel();
            this.label5 = new System.Windows.Forms.Label();
            this.tbChannelNumber = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.tbtvgEPG = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tbtvgLogo = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.tbStream = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tbChannelTags = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tbChannelName = new System.Windows.Forms.TextBox();
            this.openFile = new System.Windows.Forms.OpenFileDialog();
            this.saveFile = new System.Windows.Forms.SaveFileDialog();
            this.directoryEntry1 = new System.DirectoryServices.DirectoryEntry();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.importFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.saveHostsFile = new System.Windows.Forms.SaveFileDialog();
            this.importSimpleFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.saveSimpleFile = new System.Windows.Forms.SaveFileDialog();
            this.menuStrip.SuspendLayout();
            this.toolStrip.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.channelsGrid)).BeginInit();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip
            // 
            this.menuStrip.BackColor = System.Drawing.Color.White;
            this.menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.importToolStripMenuItem,
            this.exportToolStripMenuItem,
            this.optionsToolStripMenuItem,
            this.helpToolStripMenuItem});
            this.menuStrip.Location = new System.Drawing.Point(0, 0);
            this.menuStrip.Name = "menuStrip";
            this.menuStrip.Size = new System.Drawing.Size(920, 24);
            this.menuStrip.TabIndex = 0;
            this.menuStrip.Text = "menuStrip1";
            this.menuStrip.ItemClicked += new System.Windows.Forms.ToolStripItemClickedEventHandler(this.menuStrip_ItemClicked);
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.newListToolStripMenuItem,
            this.openFileToolStripMenuItem,
            this.openURLToolStripMenuItem,
            this.toolStripSeparator1,
            this.saveToolStripMenuItem,
            this.toolStripSeparator2,
            this.exitToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // newListToolStripMenuItem
            // 
            this.newListToolStripMenuItem.Image = global::Tantrum_IPTV_Editor.Properties.Resources.document_new;
            this.newListToolStripMenuItem.Name = "newListToolStripMenuItem";
            this.newListToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.newListToolStripMenuItem.Text = "New List";
            this.newListToolStripMenuItem.Click += new System.EventHandler(this.newListToolStripMenuItem_Click);
            // 
            // openFileToolStripMenuItem
            // 
            this.openFileToolStripMenuItem.Image = global::Tantrum_IPTV_Editor.Properties.Resources.document_open;
            this.openFileToolStripMenuItem.Name = "openFileToolStripMenuItem";
            this.openFileToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.openFileToolStripMenuItem.Text = "&Open List...";
            this.openFileToolStripMenuItem.Click += new System.EventHandler(this.openPlaylist);
            // 
            // openURLToolStripMenuItem
            // 
            this.openURLToolStripMenuItem.Image = global::Tantrum_IPTV_Editor.Properties.Resources.applications_internet;
            this.openURLToolStripMenuItem.Name = "openURLToolStripMenuItem";
            this.openURLToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.openURLToolStripMenuItem.Text = "Open &URL...";
            this.openURLToolStripMenuItem.Click += new System.EventHandler(this.openURL);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(149, 6);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.Image = global::Tantrum_IPTV_Editor.Properties.Resources.document_save_as;
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.saveToolStripMenuItem.Text = "&Save as...";
            this.saveToolStripMenuItem.Click += new System.EventHandler(this.savePlaylist);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            this.toolStripSeparator2.Size = new System.Drawing.Size(149, 6);
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Image = global::Tantrum_IPTV_Editor.Properties.Resources.emblem_unreadable;
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(152, 22);
            this.exitToolStripMenuItem.Text = "&Exit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.exitToolStripMenuItem_Click);
            // 
            // importToolStripMenuItem
            // 
            this.importToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.importKodiIPTVListToolStripMenuItem,
            this.importSimpleIPTVListToolStripMenuItem});
            this.importToolStripMenuItem.Name = "importToolStripMenuItem";
            this.importToolStripMenuItem.Size = new System.Drawing.Size(55, 20);
            this.importToolStripMenuItem.Text = "Import";
            // 
            // importKodiIPTVListToolStripMenuItem
            // 
            this.importKodiIPTVListToolStripMenuItem.Enabled = false;
            this.importKodiIPTVListToolStripMenuItem.Name = "importKodiIPTVListToolStripMenuItem";
            this.importKodiIPTVListToolStripMenuItem.Size = new System.Drawing.Size(197, 22);
            this.importKodiIPTVListToolStripMenuItem.Text = "Import Kodi IPTV List";
            this.importKodiIPTVListToolStripMenuItem.Click += new System.EventHandler(this.importKodiIPTVListToolStripMenuItem_Click);
            // 
            // importSimpleIPTVListToolStripMenuItem
            // 
            this.importSimpleIPTVListToolStripMenuItem.Enabled = false;
            this.importSimpleIPTVListToolStripMenuItem.Name = "importSimpleIPTVListToolStripMenuItem";
            this.importSimpleIPTVListToolStripMenuItem.Size = new System.Drawing.Size(197, 22);
            this.importSimpleIPTVListToolStripMenuItem.Text = "Import Simple IPTV List";
            this.importSimpleIPTVListToolStripMenuItem.Click += new System.EventHandler(this.importSimpleIPTVListToolStripMenuItem_Click);
            // 
            // exportToolStripMenuItem
            // 
            this.exportToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.exportKodiIPTVListToolStripMenuItem,
            this.exportSimpleIPTVListToolStripMenuItem});
            this.exportToolStripMenuItem.Name = "exportToolStripMenuItem";
            this.exportToolStripMenuItem.Size = new System.Drawing.Size(52, 20);
            this.exportToolStripMenuItem.Text = "Export";
            // 
            // exportKodiIPTVListToolStripMenuItem
            // 
            this.exportKodiIPTVListToolStripMenuItem.Enabled = false;
            this.exportKodiIPTVListToolStripMenuItem.Name = "exportKodiIPTVListToolStripMenuItem";
            this.exportKodiIPTVListToolStripMenuItem.Size = new System.Drawing.Size(194, 22);
            this.exportKodiIPTVListToolStripMenuItem.Text = "Export Kodi IPTV List";
            this.exportKodiIPTVListToolStripMenuItem.Click += new System.EventHandler(this.savePlaylist);
            // 
            // exportSimpleIPTVListToolStripMenuItem
            // 
            this.exportSimpleIPTVListToolStripMenuItem.Enabled = false;
            this.exportSimpleIPTVListToolStripMenuItem.Name = "exportSimpleIPTVListToolStripMenuItem";
            this.exportSimpleIPTVListToolStripMenuItem.Size = new System.Drawing.Size(194, 22);
            this.exportSimpleIPTVListToolStripMenuItem.Text = "Export Simple IPTV List";
            this.exportSimpleIPTVListToolStripMenuItem.Click += new System.EventHandler(this.saveSimplePlaylist);
            // 
            // optionsToolStripMenuItem
            // 
            this.optionsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.reporrtDuplicatesToolStripMenuItem});
            this.optionsToolStripMenuItem.Name = "optionsToolStripMenuItem";
            this.optionsToolStripMenuItem.Size = new System.Drawing.Size(61, 20);
            this.optionsToolStripMenuItem.Text = "Options";
            // 
            // reporrtDuplicatesToolStripMenuItem
            // 
            this.reporrtDuplicatesToolStripMenuItem.Name = "reporrtDuplicatesToolStripMenuItem";
            this.reporrtDuplicatesToolStripMenuItem.Size = new System.Drawing.Size(167, 22);
            this.reporrtDuplicatesToolStripMenuItem.Text = "Report Duplicates";
            this.reporrtDuplicatesToolStripMenuItem.Click += new System.EventHandler(this.reporrtDuplicatesToolStripMenuItem_Click);
            // 
            // helpToolStripMenuItem
            // 
            this.helpToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aboutToolStripMenuItem,
            this.documentationHowToToolStripMenuItem});
            this.helpToolStripMenuItem.Name = "helpToolStripMenuItem";
            this.helpToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.helpToolStripMenuItem.Text = "&Help";
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.Image = global::Tantrum_IPTV_Editor.Properties.Resources.dialog_information;
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(206, 22);
            this.aboutToolStripMenuItem.Text = "&About";
            this.aboutToolStripMenuItem.Click += new System.EventHandler(this.aboutToolStripMenuItem_Click);
            // 
            // documentationHowToToolStripMenuItem
            // 
            this.documentationHowToToolStripMenuItem.Name = "documentationHowToToolStripMenuItem";
            this.documentationHowToToolStripMenuItem.Size = new System.Drawing.Size(206, 22);
            this.documentationHowToToolStripMenuItem.Text = "Documentation(How To)";
            this.documentationHowToToolStripMenuItem.Click += new System.EventHandler(this.documentationHowToToolStripMenuItem_Click);
            // 
            // toolStrip
            // 
            this.toolStrip.BackColor = System.Drawing.Color.White;
            this.toolStrip.ImageScalingSize = new System.Drawing.Size(24, 24);
            this.toolStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripButton1,
            this.toolStripOpenFile,
            this.toolStripOpenURL,
            this.toolStripSeparator3,
            this.toolStripSave,
            this.toolStripSeparator4,
            this.toolStripNew,
            this.toolStripRemove,
            this.toolStripDuplicate,
            this.toolStripSeparator5,
            this.toolStripBtnCopyName,
            this.toolStripSeparator6,
            this.toolStripBtnClearDuplicates,
            this.toolStripBtnVerifyLinks,
            this.toolStripBtnRemoveDeadLinks,
            this.toolStripBtnExportHosts,
            this.toolStripSeparator7});
            this.toolStrip.Location = new System.Drawing.Point(0, 24);
            this.toolStrip.Name = "toolStrip";
            this.toolStrip.Size = new System.Drawing.Size(920, 31);
            this.toolStrip.TabIndex = 1;
            this.toolStrip.Text = "toolStrip1";
            this.toolStrip.ItemClicked += new System.Windows.Forms.ToolStripItemClickedEventHandler(this.toolStrip_ItemClicked);
            // 
            // toolStripButton1
            // 
            this.toolStripButton1.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripButton1.Image = global::Tantrum_IPTV_Editor.Properties.Resources.document_new;
            this.toolStripButton1.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripButton1.Name = "toolStripButton1";
            this.toolStripButton1.Size = new System.Drawing.Size(28, 28);
            this.toolStripButton1.Text = "New IPTV List";
            this.toolStripButton1.Click += new System.EventHandler(this.toolStripButton1_Click);
            // 
            // toolStripOpenFile
            // 
            this.toolStripOpenFile.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripOpenFile.Image = global::Tantrum_IPTV_Editor.Properties.Resources.document_open;
            this.toolStripOpenFile.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripOpenFile.Name = "toolStripOpenFile";
            this.toolStripOpenFile.Size = new System.Drawing.Size(28, 28);
            this.toolStripOpenFile.Text = "Open &File...";
            this.toolStripOpenFile.Click += new System.EventHandler(this.openPlaylist);
            // 
            // toolStripOpenURL
            // 
            this.toolStripOpenURL.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripOpenURL.Image = global::Tantrum_IPTV_Editor.Properties.Resources.applications_internet;
            this.toolStripOpenURL.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripOpenURL.Margin = new System.Windows.Forms.Padding(5, 1, 5, 2);
            this.toolStripOpenURL.Name = "toolStripOpenURL";
            this.toolStripOpenURL.Size = new System.Drawing.Size(28, 28);
            this.toolStripOpenURL.Text = "Open &URL...";
            this.toolStripOpenURL.Click += new System.EventHandler(this.openURL);
            // 
            // toolStripSeparator3
            // 
            this.toolStripSeparator3.Name = "toolStripSeparator3";
            this.toolStripSeparator3.Size = new System.Drawing.Size(6, 31);
            // 
            // toolStripSave
            // 
            this.toolStripSave.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripSave.Enabled = false;
            this.toolStripSave.Image = global::Tantrum_IPTV_Editor.Properties.Resources.document_save_as;
            this.toolStripSave.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripSave.Margin = new System.Windows.Forms.Padding(5, 1, 5, 2);
            this.toolStripSave.Name = "toolStripSave";
            this.toolStripSave.Size = new System.Drawing.Size(28, 28);
            this.toolStripSave.Text = "&Save";
            this.toolStripSave.Click += new System.EventHandler(this.savePlaylist);
            // 
            // toolStripSeparator4
            // 
            this.toolStripSeparator4.Name = "toolStripSeparator4";
            this.toolStripSeparator4.Size = new System.Drawing.Size(6, 31);
            // 
            // toolStripNew
            // 
            this.toolStripNew.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripNew.Enabled = false;
            this.toolStripNew.Image = global::Tantrum_IPTV_Editor.Properties.Resources.list_add;
            this.toolStripNew.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripNew.Margin = new System.Windows.Forms.Padding(5, 1, 0, 2);
            this.toolStripNew.Name = "toolStripNew";
            this.toolStripNew.Size = new System.Drawing.Size(28, 28);
            this.toolStripNew.Text = "New Channel";
            this.toolStripNew.Click += new System.EventHandler(this.toolStripNew_Click);
            // 
            // toolStripRemove
            // 
            this.toolStripRemove.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripRemove.Enabled = false;
            this.toolStripRemove.Image = global::Tantrum_IPTV_Editor.Properties.Resources.list_remove;
            this.toolStripRemove.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripRemove.Margin = new System.Windows.Forms.Padding(5, 1, 0, 2);
            this.toolStripRemove.Name = "toolStripRemove";
            this.toolStripRemove.Size = new System.Drawing.Size(28, 28);
            this.toolStripRemove.Text = "Remove Channel";
            this.toolStripRemove.Click += new System.EventHandler(this.toolStripRemove_Click);
            // 
            // toolStripDuplicate
            // 
            this.toolStripDuplicate.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripDuplicate.Enabled = false;
            this.toolStripDuplicate.Image = global::Tantrum_IPTV_Editor.Properties.Resources.edit_copy;
            this.toolStripDuplicate.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripDuplicate.Margin = new System.Windows.Forms.Padding(5, 1, 0, 2);
            this.toolStripDuplicate.Name = "toolStripDuplicate";
            this.toolStripDuplicate.Size = new System.Drawing.Size(28, 28);
            this.toolStripDuplicate.Text = "Duplicate Channel";
            this.toolStripDuplicate.Click += new System.EventHandler(this.toolStripDuplicate_Click);
            // 
            // toolStripSeparator5
            // 
            this.toolStripSeparator5.Name = "toolStripSeparator5";
            this.toolStripSeparator5.Size = new System.Drawing.Size(6, 31);
            // 
            // toolStripBtnCopyName
            // 
            this.toolStripBtnCopyName.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripBtnCopyName.Enabled = false;
            this.toolStripBtnCopyName.Image = global::Tantrum_IPTV_Editor.Properties.Resources.copy_name;
            this.toolStripBtnCopyName.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripBtnCopyName.Name = "toolStripBtnCopyName";
            this.toolStripBtnCopyName.Size = new System.Drawing.Size(28, 28);
            this.toolStripBtnCopyName.Text = "Copy Name to EPG";
            this.toolStripBtnCopyName.Click += new System.EventHandler(this.toolStripBtnCopyName_Click);
            // 
            // toolStripSeparator6
            // 
            this.toolStripSeparator6.Name = "toolStripSeparator6";
            this.toolStripSeparator6.Size = new System.Drawing.Size(6, 31);
            // 
            // toolStripBtnClearDuplicates
            // 
            this.toolStripBtnClearDuplicates.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripBtnClearDuplicates.Enabled = false;
            this.toolStripBtnClearDuplicates.Image = global::Tantrum_IPTV_Editor.Properties.Resources.clearduplicates;
            this.toolStripBtnClearDuplicates.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripBtnClearDuplicates.Margin = new System.Windows.Forms.Padding(5, 1, 0, 2);
            this.toolStripBtnClearDuplicates.Name = "toolStripBtnClearDuplicates";
            this.toolStripBtnClearDuplicates.Size = new System.Drawing.Size(28, 28);
            this.toolStripBtnClearDuplicates.Text = "Clear Duplicate Hosts";
            this.toolStripBtnClearDuplicates.Click += new System.EventHandler(this.toolStripBtnClearDuplicates_Click);
            // 
            // toolStripBtnVerifyLinks
            // 
            this.toolStripBtnVerifyLinks.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripBtnVerifyLinks.Enabled = false;
            this.toolStripBtnVerifyLinks.Image = global::Tantrum_IPTV_Editor.Properties.Resources.check_links;
            this.toolStripBtnVerifyLinks.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripBtnVerifyLinks.Name = "toolStripBtnVerifyLinks";
            this.toolStripBtnVerifyLinks.Size = new System.Drawing.Size(28, 28);
            this.toolStripBtnVerifyLinks.Text = "Verify Links";
            this.toolStripBtnVerifyLinks.Click += new System.EventHandler(this.toolStripBtnVerifyLinks_Click);
            // 
            // toolStripBtnRemoveDeadLinks
            // 
            this.toolStripBtnRemoveDeadLinks.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripBtnRemoveDeadLinks.Enabled = false;
            this.toolStripBtnRemoveDeadLinks.Image = global::Tantrum_IPTV_Editor.Properties.Resources.remove_links;
            this.toolStripBtnRemoveDeadLinks.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripBtnRemoveDeadLinks.Name = "toolStripBtnRemoveDeadLinks";
            this.toolStripBtnRemoveDeadLinks.Size = new System.Drawing.Size(28, 28);
            this.toolStripBtnRemoveDeadLinks.Text = "Remove Dead Links";
            this.toolStripBtnRemoveDeadLinks.Click += new System.EventHandler(this.toolStripBtnRemoveDeadLinks_Click);
            // 
            // toolStripBtnExportHosts
            // 
            this.toolStripBtnExportHosts.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.toolStripBtnExportHosts.Enabled = false;
            this.toolStripBtnExportHosts.Image = ((System.Drawing.Image)(resources.GetObject("toolStripBtnExportHosts.Image")));
            this.toolStripBtnExportHosts.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.toolStripBtnExportHosts.Name = "toolStripBtnExportHosts";
            this.toolStripBtnExportHosts.Size = new System.Drawing.Size(28, 28);
            this.toolStripBtnExportHosts.Text = "Exports Hosts for Validation";
            this.toolStripBtnExportHosts.Click += new System.EventHandler(this.toolStripBtnExportHosts_Click);
            // 
            // toolStripSeparator7
            // 
            this.toolStripSeparator7.Name = "toolStripSeparator7";
            this.toolStripSeparator7.Size = new System.Drawing.Size(6, 31);
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.FixedPanel = System.Windows.Forms.FixedPanel.Panel2;
            this.splitContainer1.IsSplitterFixed = true;
            this.splitContainer1.Location = new System.Drawing.Point(0, 55);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.channelsGrid);
            this.splitContainer1.Panel1MinSize = 400;
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.panel1);
            this.splitContainer1.Panel2MinSize = 280;
            this.splitContainer1.Size = new System.Drawing.Size(920, 512);
            this.splitContainer1.SplitterDistance = 635;
            this.splitContainer1.TabIndex = 2;
            this.splitContainer1.SplitterMoved += new System.Windows.Forms.SplitterEventHandler(this.splitContainer1_SplitterMoved);
            // 
            // channelsGrid
            // 
            this.channelsGrid.AllowUserToResizeRows = false;
            this.channelsGrid.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.channelsGrid.BackgroundColor = System.Drawing.SystemColors.Control;
            this.channelsGrid.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.channelsGrid.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.channelsGrid.Dock = System.Windows.Forms.DockStyle.Fill;
            this.channelsGrid.Location = new System.Drawing.Point(0, 0);
            this.channelsGrid.MultiSelect = false;
            this.channelsGrid.Name = "channelsGrid";
            this.channelsGrid.ReadOnly = true;
            this.channelsGrid.RowHeadersVisible = false;
            this.channelsGrid.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.FullRowSelect;
            this.channelsGrid.Size = new System.Drawing.Size(635, 512);
            this.channelsGrid.TabIndex = 0;
            this.channelsGrid.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.channelsGrid_CellContentClick);
            this.channelsGrid.SelectionChanged += new System.EventHandler(this.channelsGrid_SelectionChanged);
            // 
            // panel1
            // 
            this.panel1.AutoSize = true;
            this.panel1.BackColor = System.Drawing.Color.White;
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.tbChannelNumber);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Controls.Add(this.tbtvgEPG);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.tbtvgLogo);
            this.panel1.Controls.Add(this.label6);
            this.panel1.Controls.Add(this.tbStream);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.tbChannelTags);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.tbChannelName);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(281, 512);
            this.panel1.TabIndex = 0;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 68);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(89, 13);
            this.label5.TabIndex = 24;
            this.label5.Text = "Channel Number:";
            // 
            // tbChannelNumber
            // 
            this.tbChannelNumber.Location = new System.Drawing.Point(15, 84);
            this.tbChannelNumber.Name = "tbChannelNumber";
            this.tbChannelNumber.Size = new System.Drawing.Size(248, 20);
            this.tbChannelNumber.TabIndex = 23;
            this.tbChannelNumber.TextChanged += new System.EventHandler(this.tbChannelNumber_TextChanged);
            this.tbChannelNumber.MouseLeave += new System.EventHandler(this.tbChannelNumber_MouseLeave);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 278);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(63, 13);
            this.label4.TabIndex = 22;
            this.label4.Text = "TV EPG ID:";
            // 
            // tbtvgEPG
            // 
            this.tbtvgEPG.Location = new System.Drawing.Point(15, 294);
            this.tbtvgEPG.Name = "tbtvgEPG";
            this.tbtvgEPG.Size = new System.Drawing.Size(248, 20);
            this.tbtvgEPG.TabIndex = 21;
            this.tbtvgEPG.TextChanged += new System.EventHandler(this.textBox2_TextChanged);
            this.tbtvgEPG.MouseLeave += new System.EventHandler(this.textBox2_MouseLeave);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 225);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(34, 13);
            this.label1.TabIndex = 20;
            this.label1.Text = "Logo:";
            // 
            // tbtvgLogo
            // 
            this.tbtvgLogo.Location = new System.Drawing.Point(15, 241);
            this.tbtvgLogo.Name = "tbtvgLogo";
            this.tbtvgLogo.Size = new System.Drawing.Size(248, 20);
            this.tbtvgLogo.TabIndex = 19;
            this.tbtvgLogo.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            this.tbtvgLogo.MouseLeave += new System.EventHandler(this.textBox1_MouseLeave);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 173);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(68, 13);
            this.label6.TabIndex = 11;
            this.label6.Text = "Stream URL:";
            // 
            // tbStream
            // 
            this.tbStream.Location = new System.Drawing.Point(15, 189);
            this.tbStream.Name = "tbStream";
            this.tbStream.Size = new System.Drawing.Size(248, 20);
            this.tbStream.TabIndex = 10;
            this.tbStream.TextChanged += new System.EventHandler(this.stream_TextChanged);
            this.tbStream.MouseLeave += new System.EventHandler(this.stream_MouseLeave_1);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 122);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(39, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Group:";
            // 
            // tbChannelTags
            // 
            this.tbChannelTags.Location = new System.Drawing.Point(15, 138);
            this.tbChannelTags.Name = "tbChannelTags";
            this.tbChannelTags.Size = new System.Drawing.Size(248, 20);
            this.tbChannelTags.TabIndex = 4;
            this.tbChannelTags.TextChanged += new System.EventHandler(this.channelTags_TextChanged);
            this.tbChannelTags.MouseLeave += new System.EventHandler(this.channelTags_MouseLeave);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 15);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Name:";
            // 
            // tbChannelName
            // 
            this.tbChannelName.Location = new System.Drawing.Point(15, 31);
            this.tbChannelName.Name = "tbChannelName";
            this.tbChannelName.Size = new System.Drawing.Size(248, 20);
            this.tbChannelName.TabIndex = 2;
            this.tbChannelName.TextChanged += new System.EventHandler(this.channelName_TextChanged_1);
            this.tbChannelName.MouseLeave += new System.EventHandler(this.channelName_MouseLeave);
            // 
            // openFile
            // 
            this.openFile.Filter = "Playlist Files (*.m3u)|*.m3u|CSV files (*.csv)|*.csv";
            this.openFile.Title = "Open Playlist";
            this.openFile.FileOk += new System.ComponentModel.CancelEventHandler(this.openFile_FileOk);
            // 
            // saveFile
            // 
            this.saveFile.Filter = "Playlist Files (*.m3u)|*.m3u|CSV files (*.csv)|*.csv";
            this.saveFile.Title = "Save Playlist";
            this.saveFile.FileOk += new System.ComponentModel.CancelEventHandler(this.saveFile_FileOk);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.Filter = "Playlist Files (*.m3u)|*.m3u";
            this.openFileDialog1.Title = "Open Playlist";
            this.openFileDialog1.FileOk += new System.ComponentModel.CancelEventHandler(this.openFileDialog1_FileOk);
            // 
            // importFileDialog
            // 
            this.importFileDialog.Filter = "Playlist Files (*.m3u)|*.m3u";
            this.importFileDialog.Title = "Open Playlist";
            this.importFileDialog.FileOk += new System.ComponentModel.CancelEventHandler(this.importFileDialog_FileOk);
            // 
            // saveHostsFile
            // 
            this.saveHostsFile.Filter = "Playlist Files (*.m3u)|*.m3u";
            this.saveHostsFile.Title = "Save Hosts File";
            this.saveHostsFile.FileOk += new System.ComponentModel.CancelEventHandler(this.saveHostsFile_FileOk);
            // 
            // importSimpleFileDialog
            // 
            this.importSimpleFileDialog.Filter = "Playlist Files (*.m3u)|*.m3u";
            this.importSimpleFileDialog.Title = "Import Simple List";
            this.importSimpleFileDialog.FileOk += new System.ComponentModel.CancelEventHandler(this.importSimpleFileDialog_FileOk);
            // 
            // saveSimpleFile
            // 
            this.saveSimpleFile.Filter = "Playlist Files (*.m3u)|*.m3u";
            this.saveSimpleFile.Title = "Save Simple IPTV List";
            this.saveSimpleFile.FileOk += new System.ComponentModel.CancelEventHandler(this.saveSimpleFile_FileOk);
            // 
            // Editor
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(920, 567);
            this.Controls.Add(this.splitContainer1);
            this.Controls.Add(this.toolStrip);
            this.Controls.Add(this.menuStrip);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip;
            this.MinimumSize = new System.Drawing.Size(870, 490);
            this.Name = "Editor";
            this.Text = "Tantrum IPTV Editor";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Editor_FormClosing);
            this.Load += new System.EventHandler(this.Editor_Load);
            this.menuStrip.ResumeLayout(false);
            this.menuStrip.PerformLayout();
            this.toolStrip.ResumeLayout(false);
            this.toolStrip.PerformLayout();
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            this.splitContainer1.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.channelsGrid)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openFileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openURLToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem helpToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStrip toolStrip;
        private System.Windows.Forms.ToolStripButton toolStripOpenFile;
        private System.Windows.Forms.ToolStripButton toolStripOpenURL;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
        private System.Windows.Forms.ToolStripButton toolStripSave;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.DataGridView channelsGrid;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbChannelTags;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox tbChannelName;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.OpenFileDialog openFile;
        private System.Windows.Forms.ToolStripButton toolStripNew;
        private System.Windows.Forms.ToolStripButton toolStripDuplicate;
        private System.Windows.Forms.ToolStripButton toolStripRemove;
        private System.Windows.Forms.SaveFileDialog saveFile;
        private System.Windows.Forms.ToolStripMenuItem newListToolStripMenuItem;
        private System.DirectoryServices.DirectoryEntry directoryEntry1;
        public System.Windows.Forms.TextBox tbStream;
        private System.Windows.Forms.ToolStripButton toolStripButton1;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tbtvgLogo;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox tbtvgEPG;
        private System.Windows.Forms.ToolStripMenuItem documentationHowToToolStripMenuItem;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox tbChannelNumber;
        private System.Windows.Forms.ToolStripButton toolStripBtnClearDuplicates;
        private System.Windows.Forms.ToolStripMenuItem optionsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reporrtDuplicatesToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator5;
        private System.Windows.Forms.OpenFileDialog importFileDialog;
        private System.Windows.Forms.ToolStripButton toolStripBtnExportHosts;
        private System.Windows.Forms.SaveFileDialog saveHostsFile;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator6;
        private System.Windows.Forms.ToolStripButton toolStripBtnVerifyLinks;
        private System.Windows.Forms.ToolStripButton toolStripBtnRemoveDeadLinks;
        private System.Windows.Forms.OpenFileDialog importSimpleFileDialog;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator7;
        private System.Windows.Forms.ToolStripButton toolStripBtnCopyName;
        private System.Windows.Forms.ToolStripMenuItem importToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem importKodiIPTVListToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem importSimpleIPTVListToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exportToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exportKodiIPTVListToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exportSimpleIPTVListToolStripMenuItem;
        private System.Windows.Forms.SaveFileDialog saveSimpleFile;
    }
}

