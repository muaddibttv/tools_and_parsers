using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Net;

namespace Tantrum_IPTV_Editor
{
    public partial class Editor : Form
    {

        public List<string> data = new List<string>();

        public string fileName = "", line;
        private int channelNum = 0;
        public StreamReader playlistFile;
        public SortableBindingList<Channel> channels = new SortableBindingList<Channel>();
        bool newlist;
        bool updateboolean;

        private void ToggleToolbarButtons(bool mode)
        {
            importKodiIPTVListToolStripMenuItem.Enabled = mode;
            toolStripBtnExportHosts.Enabled = mode;
            toolStripBtnVerifyLinks.Enabled = mode;
            toolStripBtnRemoveDeadLinks.Enabled = mode;
            importSimpleIPTVListToolStripMenuItem.Enabled = mode;
            toolStripBtnCopyName.Enabled = mode;
            exportKodiIPTVListToolStripMenuItem.Enabled = mode;
            exportSimpleIPTVListToolStripMenuItem.Enabled = mode;
        }

        public Editor()
        {
            newlist = true;
            InitializeComponent();
            ToggleToolbarButtons(false);
        }

        public SortableBindingList<Channel> GetList()
        {
            return channels;
        }

        private void openPlaylist(object sender, EventArgs e)
        {
            alertSave();
            openFile.ShowDialog();
        }

        public void updatechannels()
        {
            if (updateboolean == true)
            {
                if (channelsGrid.SelectedRows.Count == 0)
                    return;

                if (tbChannelName.Text.Trim().Length > 0 && tbStream.Text.Trim().Length > 0)
                {
                    int selectedRow = channelsGrid.SelectedRows[0].Index;

                    channels[selectedRow].Name = tbChannelName.Text;
                    channels[selectedRow].ChannelID = tbChannelNumber.Text;
                    channels[selectedRow].Group = tbChannelTags.Text;

                    channels[selectedRow].IP = tbStream.Text;
                    string uri = tbStream.Text;
                    channels[selectedRow].EPG = tbtvgEPG.Text;
                    channels[selectedRow].Image = tbtvgLogo.Text;
                }
            }
        }

        public void importM3U()
        {
            //  bool image = false;
            updateboolean = false;

            while ((line = playlistFile.ReadLine()) != null)
            {
                if (line.StartsWith("#EXTINF"))
                {
                    data.Add("EPG N/A");
                    data.Add("Logo N/A");
                    data.Add("Unsorted");
                    data.Add("EPG N/A");
                    data.Add("Logo N/A");
                    data.Add("Unsorted");
                    data.Add("Title N/A");

                    //tvg-id used for epg data[0]

                    string between2 = textoperations.Between(line, "tvg-id=\"", "\"");
                    data[0] = between2;
                    if (data[0] == "")
                    {
                        data[0] = "EPG N/A";
                    }

                    //tvg-logo used for logo data[1]

                    string between3 = textoperations.Between(line, "tvg-logo=\"", "\"");
                    data[1] = between3;
                    if (data[1] == "")
                    {
                        data[1] = "Logo N/A";
                    }

                    //this one is for getting group-title data[2]

                    string between = textoperations.Between(line, "group-title=\"", "\"");
                    data[2] = between;
                    if (data[2] == "")
                    {
                        data[2] = "Unsorted";
                    }

                    //this is the name of the channel... data[3 && 4]= rubbish data[5]=channel name 

                    string lastPart = line.Split(',').Last();
                    data[6] = lastPart;
                    if (data[6] == "")
                    {
                        data[6] = "Title N/A";
                    }
                    continue;
                }
                else if (line.Contains("//"))
                {
                    //this is the url ...data[6]
                    data[5] = line;
                }

                // here comes the bit that adds the channels, and defines what goes where

                if (data.Count > 0)
                {
                    try
                    {
                        //data count should be 7
                        channels.Add(new Channel(id: channelNum, Name: data[6].Trim(), ip: data[5].Trim(), Group: data[2].Trim(), logo: data[1].Trim(), tvid: data[0].Trim()));//, data[4].Trim(),data[6].Trim(), data[5].Trim()* 
                    }
                    catch (System.ArgumentOutOfRangeException)
                    {
                        MessageBox.Show("A channel has been omitted due to its incorrect format");
                        continue;
                    }
                }
                data.Clear();
            }
            playlistFile.Close();

            if (channels.Count == 0)
            {
                MessageBox.Show("Selected file has incorrect structure! Please open an appropriate file.", "File Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                splitContainer1.Panel2Collapsed = false; enableEditing();

            }
        }

        public void importSimpleM3U()
        {
            //  bool image = false;
            updateboolean = false;

            while ((line = playlistFile.ReadLine()) != null)
            {
                if (line.StartsWith("#EXTINF"))
                {
                    data.Add("EPG N/A");
                    data.Add("Logo N/A");
                    data.Add("Unsorted");
                    data.Add("EPG N/A");
                    data.Add("Logo N/A");
                    data.Add("Unsorted");
                    data.Add("Title N/A");

                    string lastPart = line.Substring(line.IndexOf(",") + 1);
                    data[6] = lastPart;
                    if (data[6] == "")
                    {
                        data[6] = "Title N/A";
                    }
                    continue;
                }
                else if (line.Contains("//"))
                {
                    //this is the url ...data[6]
                    data[5] = line;
                }

                // here comes the bit that adds the channels, and defines what goes where

                if (data.Count > 0)
                {
                    try
                    {
                        //data count should be 7
                        channels.Add(new Channel(id: channelNum, Name: data[6].Trim(), ip: data[5].Trim(), Group: data[2].Trim(), logo: data[1].Trim(), tvid: data[0].Trim()));//, data[4].Trim(),data[6].Trim(), data[5].Trim()* 
                    }
                    catch (System.ArgumentOutOfRangeException)
                    {
                        MessageBox.Show("A channel has been omitted due to its incorrect format");
                        continue;
                    }
                }
                data.Clear();
            }
            playlistFile.Close();

            if (channels.Count == 0)
            {
                MessageBox.Show("Selected file has incorrect structure! Please open an appropriate file.", "File Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                splitContainer1.Panel2Collapsed = false; enableEditing();

            }
        }

        private void importCSV()
        {
            while ((line = playlistFile.ReadLine()) != null)
            {
                data.Add("one N/A"); // 0
                data.Add("two N/A"); // 1
                data.Add("three N/A"); // 2
                data.Add("four N/A");//3
                data.Add("five N/A");//4
                data.Add("six N/A");//5
                data.Add("seven N/A");//6

                data.AddRange(line.Split(','));

                // if (!int.TryParse(data[0].Trim(), out channelNum)) { data.Clear(); continue; }

                if (data.Count > 0)
                {
                    try
                    {
                        //data count should be 7 */
                        channels.Add(new Channel(id: channelNum, Name: data[7].Trim(), ip: data[9].Trim(), Group: data[8].Trim(), logo: data[10].Trim(), tvid: data[11].Trim()));//, data[4].Trim(),data[6].Trim(), data[5].Trim()* 
                    }
                    catch (System.ArgumentOutOfRangeException)
                    {
                        MessageBox.Show("A channel has been omitted due to its incorrect format");
                        continue;
                    }
                    data.Clear();
                }
                // playlistFile.Close();
                if (channels.Count == 0)
                {
                    MessageBox.Show("Selected file has incorrect structure! Please open appropriate file.", "File Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            channels.RemoveAt(0);
        }

        private void enableEditing()
        {
            saveToolStripMenuItem.Enabled = true;
            // exportToolStripMenuItem.Enabled = true;
            toolStripSave.Enabled = true;

            toolStripNew.Enabled = true;
            toolStripRemove.Enabled = true;
            // this.channelsGrid.Columns[1].SortMode = DataGridViewColumnSortMode.Automatic;
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void textBoxNumericInput(object sender, KeyPressEventArgs e)
        {
            e.Handled = !char.IsDigit(e.KeyChar) && !char.IsControl(e.KeyChar);
        }

        private void toolStripNew_Click(object sender, EventArgs e)
        {
            channels.Add(new Channel(id: channelNum, Name: "New Channel", ip: "http://123.456.789", Group: "New Group", logo: "New Logo", tvid: "New EPG"));
            channelsGrid.Rows[channels.Count - 1].Selected = true;
            channelsGrid.FirstDisplayedScrollingRowIndex = channels.Count - 1;
        }

        public void channelsGrid_SelectionChanged(object sender, EventArgs e)
        {
            if (channelsGrid.SelectedRows.Count == 0)
                return;

            int selectedRow = channelsGrid.SelectedRows[0].Index;
            /* if (selectedRow != 0)
                 toolStripMoveUp.Enabled = true;
             else
                 toolStripMoveUp.Enabled = false;
             if (channelsGrid.RowCount > 1 && selectedRow == channelsGrid.RowCount - 1)
                 toolStripMoveDown.Enabled = false;
             else
                 toolStripMoveDown.Enabled = true;
             */
            toolStripDuplicate.Enabled = true;
            toolStripBtnClearDuplicates.Enabled = true;

            updateboolean = false;
            tbChannelName.Text = channels[selectedRow].Name;
            tbChannelNumber.Text = channels[selectedRow].ChannelID;
            tbChannelTags.Text = channels[selectedRow].Group;

            tbStream.Text = channels[selectedRow].IP;
            tbtvgLogo.Text = channels[selectedRow].Image;
            tbtvgEPG.Text = channels[selectedRow].EPG;
            updateboolean = true;

            string uri = tbStream.Text;
        }

        private void toolStripMoveUp_Click(object sender, EventArgs e)
        {
            if (channelsGrid.SelectedRows.Count == 0)
                return;

            int selectedRow = channelsGrid.SelectedRows[0].Index;
            Channel current = channels[selectedRow];
            Channel previous = channels[selectedRow - 1];
            channels.RemoveAt(selectedRow);

            channels.Insert(selectedRow -= 1, current);
            channelsGrid.Rows[selectedRow].Selected = true;
        }

        private void toolStripMoveDown_Click(object sender, EventArgs e)
        {
            if (channelsGrid.SelectedRows.Count == 0)
                return;

            int selectedRow = channelsGrid.SelectedRows[0].Index;
            Channel current = channels[selectedRow];
            Channel next = channels[selectedRow + 1];
            channels.RemoveAt(selectedRow);

            channels.Insert(selectedRow += 1, current);
            channelsGrid.Rows[selectedRow].Selected = true;
        }

        private void toolStripDuplicate_Click(object sender, EventArgs e)
        {
            if (channelsGrid.SelectedRows.Count == 0)
                return;

            this.Cursor = Cursors.WaitCursor;
            int selectedRow = channelsGrid.SelectedRows[0].Index;
            Channel current = channels[selectedRow++];
            channels.Insert(selectedRow, current);
            channelsGrid.Rows[selectedRow].Selected = true;
            this.Cursor = Cursors.Arrow;
        }

        private void toolStripRemove_Click(object sender, EventArgs e)
        {
            if (channelsGrid.SelectedRows.Count == 0)
                return;

            int selectedRow = channelsGrid.SelectedRows[0].Index;

            if (channels.Count > 1 && selectedRow - 1 > 0)
                channelsGrid.Rows[selectedRow - 1].Selected = true;
            else if (channels.Count > 1 && selectedRow + 1 <= channels.Count - 1)
                channelsGrid.Rows[selectedRow + 1].Selected = true;

            channels.RemoveAt(selectedRow);


        }

        private void buttonSubmit_Click(object sender, EventArgs e)
        {
            if (channelsGrid.SelectedRows.Count == 0)
                return;

            //int id;
            if (/*channelID.Text.Trim().Length > 0 && int.TryParse(channelID.Text.Trim(), out id) && */ tbChannelName.Text.Trim().Length > 0 && tbStream.Text.Trim().Length > 0)
            {
                int selectedRow = channelsGrid.SelectedRows[0].Index;

                channels[selectedRow].Name = tbChannelName.Text;
                channels[selectedRow].ChannelID = tbChannelNumber.Text;
                channels[selectedRow].Group = tbChannelTags.Text;
                tbtvgLogo.Text = channels[selectedRow].Image;
                tbtvgEPG.Text = channels[selectedRow].EPG;
                channels[selectedRow].IP = tbStream.Text;
                string uri = tbStream.Text;
                //  channels[selectedRow].EPG = channelEPG.Text;
                //channels[selectedRow].Image = channelImage.Text;
            }
            /*   else
               {
                   MessageBox.Show("A name and stream URL is required", "Update error", MessageBoxButtons.OK, MessageBoxIcon.Error);
               } */
        }

        private void savePlaylist(object sender, EventArgs e)
        {
            saveFile.ShowDialog();
        }

        private void saveSimplePlaylist(object sender, EventArgs e)
        {
            saveSimpleFile.ShowDialog();
        }

        private void openURL(object sender, EventArgs e)
        {
            alertSave();
            OpenURL url = new OpenURL();
            if (url.ShowDialog() != DialogResult.OK)
                return;

            fileName = Path.GetFileNameWithoutExtension(url.filePath);
            playlistFile = new StreamReader(url.filePath);
            channels.Clear();
            channelsGrid.AutoGenerateColumns = false;
            channelsGrid.DataSource = channels;
            if (playlistFile.ReadLine().StartsWith("#EXTM3U"))
                importM3U();
        }

        private void alertSave()
        {
            if (channelsGrid.Rows.Count == 0)
                return;
            updateboolean = true;
            DialogResult dialogSave = MessageBox.Show("Do you want to save your current playlist?", "Save Playlist", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (dialogSave == DialogResult.Yes)
                saveFile.ShowDialog();
        }



        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            about1 about = new about1();
            about.Show();
        }

        private void Editor_FormClosing(object sender, FormClosingEventArgs e)
        {
            alertSave();
        }

        public void openFile_FileOk(object sender, CancelEventArgs e)
        {
            fileName = Path.GetFileNameWithoutExtension(openFile.FileName);
            playlistFile = new StreamReader(openFile.FileName);
            channels.Clear();
            channelsGrid.DataSource = channels;
            switch (Path.GetExtension(openFile.FileName))
            {
                case ".m3u":
                    importM3U();
                    ToggleToolbarButtons(true);
                    updateboolean = true;
                    break;

                case ".csv":
                    importCSV();
                    ToggleToolbarButtons(false);
                    updateboolean = true;
                    break;

            }
        }

        private void importFileDialog_FileOk(object sender, CancelEventArgs e)
        {
            playlistFile.Close();
            fileName = Path.GetFileNameWithoutExtension(importFileDialog.FileName);
            playlistFile = new StreamReader(importFileDialog.FileName);
            channelsGrid.DataSource = channels;
            switch (Path.GetExtension(importFileDialog.FileName))
            {
                case ".m3u":
                    importM3U();
                    updateboolean = true;
                    break;
            }
        }

        private void importSimpleFileDialog_FileOk(object sender, CancelEventArgs e)
        {
            playlistFile.Close();
            fileName = Path.GetFileNameWithoutExtension(importSimpleFileDialog.FileName);
            playlistFile = new StreamReader(importSimpleFileDialog.FileName);
            channelsGrid.DataSource = channels;
            switch (Path.GetExtension(importSimpleFileDialog.FileName))
            {
                case ".m3u":
                    importSimpleM3U();
                    updateboolean = true;
                    break;
            }
        }

        private void saveFile_FileOk(object sender, CancelEventArgs e)
        {
            switch (Path.GetExtension(saveFile.FileName))
            {
                case ".m3u":
                    saveM3U();
                    break;
                case ".csv":
                    saveCSV();
                    break;

            }
        }

        private void saveM3U()
        {
            StreamWriter file = new StreamWriter(saveFile.FileName, false, Encoding.UTF8);
            file.WriteLine("#EXTM3U");
            file.WriteLine();

            for (int i = 0; i < channels.Count; i++)
            {
                string thischan = channels[i].ChannelID;
                if (thischan == null || thischan == "")
                    thischan = "-1";
                file.WriteLine("#EXTINF:" + thischan + ", tvg-id=\"" + channels[i].EPG + "\" " + "tvg-logo=\"" + channels[i].Image + "\" " + "tvg-name=\"" + channels[i].Name + "\" " + " group-title=\"" + channels[i].Group + "\"" + "," + channels[i].Name);
                file.WriteLine(channels[i].IP);
                file.WriteLine();
            }
            file.Close();
        }

        private void saveCSV()
        {
            StreamWriter file = new StreamWriter(saveFile.FileName, false, Encoding.UTF8);
            file.WriteLine("Name,Group,Stream URL,Logo,EPG");
            for (int i = 0; i < channels.Count; i++)
            {
                file.WriteLine(channels[i].Name + "," + channels[i].Group.Replace(",", "-") + "," + channels[i].IP + "," + channels[i].Image + "," + channels[i].EPG);
            }
            file.Close();
        }

        private void saveSimpleFile_FileOk(object sender, CancelEventArgs e)
        {
            switch (Path.GetExtension(saveSimpleFile.FileName))
            {
                case ".m3u":
                    saveSimpleM3U();
                    break;
            }
        }

        private void saveSimpleM3U()
        {
            StreamWriter file = new StreamWriter(saveSimpleFile.FileName, false, Encoding.UTF8);
            file.WriteLine("#EXTM3U");

            file.WriteLine();
            for (int i = 0; i < channels.Count; i++)
            {
                string thischan = channels[i].ChannelID;
                if (thischan == null || thischan == "")
                    thischan = "-1";

                file.WriteLine("#EXTINF:" + thischan + ", " + channels[i].Name);
                file.WriteLine(channels[i].IP);
                file.WriteLine();
            }
            file.Close();

            MessageBox.Show("Make sure to use this file to validate hosts via http://www.iptvtools.net/");
        }

        private void saveHostsFile_FileOk(object sender, CancelEventArgs e)
        {
            switch (Path.GetExtension(saveHostsFile.FileName))
            {
                case ".m3u":
                    saveHostsM3U();
                    break;
            }
        }

        private void saveHostsM3U()
        {
            StreamWriter file = new StreamWriter(saveHostsFile.FileName, false, Encoding.UTF8);
            file.WriteLine("#EXTM3U");

            file.WriteLine();
            for (int i = 0; i < channels.Count; i++)
            {
                string thischan = channels[i].ChannelID;
                if (thischan == null || thischan == "")
                    thischan = "-1";

                file.WriteLine("#EXTINF:" + thischan + ", " + channels[i].Name);
                file.WriteLine(channels[i].IP);
                file.WriteLine();
            }
            file.Close();

            MessageBox.Show("Make sure to use this file to validate hosts via http://www.iptvtools.net/");
        }

        private void channelsGrid_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void menuStrip_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void Editor_Load(object sender, EventArgs e)
        {

        }

        private void channelName_TextChanged(object sender, EventArgs e)
        {

        }

        private void toolStrip_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void splitContainer1_SplitterMoved(object sender, SplitterEventArgs e)
        {

        }

        public void newListToolStripMenuItem_Click(object sender, EventArgs e)
        {
            alertSave();

            enableEditing();
            channelsGrid.DataSource = channels;
            data.Clear();
            channels.Clear();
            channels.Add(new Channel(id: channelNum, Name: "New Channel", ip: "http://123.456.789", Group: "New Group", logo: "New Logo", tvid: "New EPG"));//, data[4].Trim(),data[6].Trim(), data[5].Trim()* 
            newlist = true;

            ToggleToolbarButtons(false);

            splitContainer1.Panel2Collapsed = false; enableEditing();
       }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            alertSave();

            enableEditing();
            channelsGrid.DataSource = channels;
            data.Clear();
            channels.Clear();

            channels.Add(new Channel(id: channelNum, Name: "New Channel", ip: "http://123.456.789", Group: "New Group", logo: "New Logo", tvid: "New EPG"));//, data[4].Trim(),data[6].Trim(), data[5].Trim()* 


        }

        private void addAListToolStripMenuItem_Click(object sender, EventArgs e)
        {
            openFileDialog1.ShowDialog();
        }

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            playlistFile.Close();
            fileName = Path.GetFileNameWithoutExtension(openFileDialog1.FileName);
            playlistFile = new StreamReader(openFileDialog1.FileName);

            channelsGrid.DataSource = channels;
            switch (Path.GetExtension(openFileDialog1.FileName))
            {
                case ".m3u":
                    importM3U();
                    updateboolean = true;
                    break;
            }
        }

        private void channelName_MouseLeave(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void stream_MouseLeave_1(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void channelTags_MouseLeave(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void textBox1_MouseLeave(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void textBox2_MouseLeave(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void documentationHowToToolStripMenuItem_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("https://iptvm3ueditor.codeplex.com/documentation");
        }

        private void channelName_TextChanged_1(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void channelTags_TextChanged(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void stream_TextChanged(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void toolStripBtnClearDuplicates_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            int removecnt = 0;
            string removelist = "";
            try
            {
                if (channelsGrid.Rows.Count > 2)
                {
                    for (int currentRow = 0; currentRow < channelsGrid.Rows.Count; currentRow++)
                    {
                        var rowToCompare = channelsGrid.Rows[currentRow];

                        foreach (DataGridViewRow row in channelsGrid.Rows)
                        {
                            if (rowToCompare.Equals(row))
                            {
                                continue;
                            }
                            // If row is the same row being compared, skip.

                            bool duplicateRow = true;

                            if (rowToCompare.Cells["IP"].Value != null && rowToCompare.Cells["IP"].Value.ToString() != row.Cells["IP"].Value.ToString())
                            {
                                duplicateRow = false;
                            }
                            if (duplicateRow)
                            {
                                channelsGrid.Rows.RemoveAt(row.Index);
                                if (reporrtDuplicatesToolStripMenuItem.Checked)
                                {
                                    removecnt++;
                                    removelist += rowToCompare.Cells["Name"].Value + Environment.NewLine;
                                }
                                break;
                            }
                        }
                    }
                }
            }
            catch
            {
            }
            if (reporrtDuplicatesToolStripMenuItem.Checked)
            {
                MessageBox.Show("Total Duplicates Removed: " + removecnt.ToString());
                MessageBox.Show("Names where Duplicates were found: " + Environment.NewLine + removelist);
            }
            this.Cursor = Cursors.Arrow;
        }

        private void reporrtDuplicatesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (reporrtDuplicatesToolStripMenuItem.Checked)
                reporrtDuplicatesToolStripMenuItem.Checked = false;
            else
                reporrtDuplicatesToolStripMenuItem.Checked = true;
        }

        private void tbChannelNumber_TextChanged(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void tbChannelNumber_MouseLeave(object sender, EventArgs e)
        {
            updatechannels();
        }

        private void toolStripBtnExportHosts_Click(object sender, EventArgs e)
        {
            saveHostsFile.ShowDialog();
        }

        private void toolStripBtnVerifyLinks_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            try
            {
                if (channelsGrid.Rows.Count > 0)
                {
                    for (int currentRow = 0; currentRow < channelsGrid.Rows.Count; currentRow++)
                    {
                        var rowToCheck = channelsGrid.Rows[currentRow];
                        try
                        {
                            HttpWebRequest request = WebRequest.Create(rowToCheck.Cells["IP"].Value.ToString()) as HttpWebRequest;
                            request.Method = "HEAD";
                            request.Timeout = 15000;

                            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
                            response.Close();

                            bool connected = false;
                            switch (response.StatusCode)
                            {
                                case HttpStatusCode.Accepted: connected = true; break;
                                case HttpStatusCode.Ambiguous: connected = true; break;
                                case HttpStatusCode.Continue: connected = true; break;
                                case HttpStatusCode.Created: connected = true; break;
                                case HttpStatusCode.Found: connected = true; break;
                                case HttpStatusCode.OK: connected = true; break;
                            }
                            if (!connected)
                            {
                                rowToCheck.DefaultCellStyle.BackColor = Color.Red;
                            }
                        }
                        catch (WebException webexecpt)
                        {
                            if (webexecpt.Status == WebExceptionStatus.Timeout)
                            {
                                rowToCheck.DefaultCellStyle.BackColor = Color.PaleVioletRed;
                            }
                            else 
                            {
                                rowToCheck.DefaultCellStyle.BackColor = Color.Red;
                            }
                        }
                        catch
                        {
                            // Couldn't connect?
                            rowToCheck.DefaultCellStyle.BackColor = Color.Red;
                            continue;
                        }
                    }
                }
            }
            catch
            {
                MessageBox.Show("What?!?!!?!");
            }
            this.Cursor = Cursors.Arrow;
        }

        private void toolStripBtnRemoveDeadLinks_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            List<int> toremove = new List<int>();
            try
            {
                if (channelsGrid.Rows.Count > 0)
                {
                    for (int currentRow = 0; currentRow < channelsGrid.Rows.Count; currentRow++)
                    {
                        var rowToCheck = channelsGrid.Rows[currentRow];
                        try
                        {
                            if(rowToCheck.DefaultCellStyle.BackColor == Color.Red)
                            {
                                toremove.Add(currentRow);
                            }
                        }
                        catch
                        {
                            MessageBox.Show("Row Check Crash");
                        }
                    }

                    if (toremove != null && toremove.Count > 0)
                    {
                        toremove.Reverse();
                        for (int rowid = 0; rowid < toremove.Count; rowid++)
                        {
                            channelsGrid.Rows.RemoveAt(toremove[rowid]);
                        }
                    }
                }
            }
            catch
            {
                MessageBox.Show("What?!?!!?!");
            }
            this.Cursor = Cursors.Arrow;
        }

        private void toolStripBtnCopyName_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            try
            {
                if (channelsGrid.Rows.Count > 0)
                {
                    for (int currentRow = 0; currentRow < channelsGrid.Rows.Count; currentRow++)
                    {
                        var rowToCheck = channelsGrid.Rows[currentRow];
                        try
                        {
                            if (rowToCheck.Cells["EPG"].Value.ToString() == null || rowToCheck.Cells["EPG"].Value.ToString() == "EPG N/A" || rowToCheck.Cells["EPG"].Value.ToString().Length == 0)
                            {
                                rowToCheck.Cells["EPG"].Value = rowToCheck.Cells["Name"].Value;
                            }
                        }
                        catch
                        {
                        }
                    }
                }
            }
            catch
            {
                MessageBox.Show("What?!?!!?!");
            }
            this.Cursor = Cursors.Arrow;
        }

        #region Import Button Code

        private void importKodiIPTVListToolStripMenuItem_Click(object sender, EventArgs e)
        {
            importFileDialog.ShowDialog();
        }

        private void importSimpleIPTVListToolStripMenuItem_Click(object sender, EventArgs e)
        {
            importSimpleFileDialog.ShowDialog();
        }

        #endregion Import Button Code

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            updatechannels();
        }
    }
}
