using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace Kodi_Favorites_Parser
{
    public partial class MainForm : Form
    {
        DataTable favTable = null;

        public MainForm()
        {
            InitializeComponent();

            if (Directory.Exists(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData)+@"/Kodi/userdata"))
            {
                selectFavFileDialog.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData) + @"/Kodi/userdata";
            }
            else
            {
                selectFavFileDialog.InitialDirectory = Application.StartupPath;
            }
            
        }

        private void btnSelectFile_Click(object sender, EventArgs e)
        {
            DialogResult result = selectFavFileDialog.ShowDialog();
            if (result == DialogResult.OK) // Test result.
            {
                try
                { 
                    lblFavFile.Text = selectFavFileDialog.FileName;
                }
                catch
                {
                    MessageBox.Show("Issue accessing file. Make sure file is not locked or in use and try again.");
                }
            }
        }

        private void lblFavFile_TextChanged(object sender, EventArgs e)
        {
            Label thisLabel = sender as Label;
            if (thisLabel.Text.Contains("No File Selected"))
            {
                lblFavCount.Text = "";
                btnParseFile.Enabled = false;
                btnCleanChannels.Enabled = false;
                btnCleanPlaylists.Enabled = false;
                btnCleanVideos.Enabled = false;
            }
            else
            {
                btnParseFile.Enabled = true;
                btnCleanChannels.Enabled = true;
                btnCleanPlaylists.Enabled = true;
                btnCleanVideos.Enabled = true;
            }
        }

        private void btnParseFile_Click(object sender, EventArgs e)
        {
            favTable = new DataTable("Favourites");
            favTable.Columns.Add("title");
            favTable.Columns.Add("thumb");
            favTable.Columns.Add("shortcut");

            XmlDocument doc = new XmlDocument();
            doc.Load(lblFavFile.Text);

            XmlNode favsRoot = doc.DocumentElement.SelectSingleNode("/favourites");
            foreach (XmlNode favItem in doc.DocumentElement.ChildNodes)
            {
                string favTitle = favItem.Attributes["name"].InnerText;
                favTitle = Regex.Replace(favTitle, @"\[/?COLOR\b[^][]*]", string.Empty);

                string favThumb = favItem.Attributes["thumb"].InnerText;

                string favShortcut = favItem.InnerText;

                favTable.Rows.Add(favTitle, favThumb, favShortcut);
            }

            dgvFavs.DataSource = null;
            dgvFavs.DataSource = favTable;
            dgvFavs.Update();

            lblFavCount.Text = favTable.Rows.Count.ToString();
        }

        #region Favourites Editor related code

        private void btnSaveEdit_Click(object sender, EventArgs e)
        {
            if (dgvFavs.SelectedCells.Count > 0)
            {
                dgvFavs.SelectedCells[0].OwningRow.Cells[0].Value = tbTitle.Text;
                dgvFavs.SelectedCells[0].OwningRow.Cells[1].Value = tbThumb.Text;
                dgvFavs.SelectedCells[0].OwningRow.Cells[2].Value = tbShorcut.Text;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (dgvFavs.SelectedCells.Count > 0)
            {
                tbTitle.Text = dgvFavs.SelectedCells[0].OwningRow.Cells[0].Value.ToString();
                tbThumb.Text = dgvFavs.SelectedCells[0].OwningRow.Cells[1].Value.ToString();
                string tempShortcut = WebUtility.UrlDecode(dgvFavs.SelectedCells[0].OwningRow.Cells[2].Value.ToString());
                tempShortcut = Regex.Replace(tempShortcut, @"\[/?COLOR\b[^][]*]", string.Empty);
                tbShorcut.Text = tempShortcut;
            }
        }

        private void dgvFavs_RowEnter(object sender, DataGridViewCellEventArgs e)
        {
            if (dgvFavs.SelectedCells.Count > 0)
            { 
                tbTitle.Text = dgvFavs.SelectedCells[0].OwningRow.Cells[0].Value.ToString();
                tbThumb.Text = dgvFavs.SelectedCells[0].OwningRow.Cells[1].Value.ToString();
                string tempShortcut = WebUtility.UrlDecode(dgvFavs.SelectedCells[0].OwningRow.Cells[2].Value.ToString());
                tempShortcut = Regex.Replace(tempShortcut, @"\[/?COLOR\b[^][]*]", string.Empty);
                tbShorcut.Text = tempShortcut;
            }
        }

        #endregion Favourites Editor related code

        #region Menu Generator related code

        private void btnMakeMenu_Click(object sender, EventArgs e)
        {
            tbMenuFile.Text = string.Empty;
            if (rbPlain.Checked)
                GeneratePlainData();
            else
                GenerateYTData();
        }

        private void GeneratePlainData()
        {
            StringBuilder menuItem = new StringBuilder();

            menuItem.AppendLine();
            if (cbTitle.Checked)
                menuItem.AppendLine(tbTitle.Text);
            if (cbThumb.Checked)
                menuItem.AppendLine(tbThumb.Text);
            if (cbShortcut.Checked)
                menuItem.AppendLine(tbShorcut.Text);
            menuItem.AppendLine();

            tbMenuFile.Text = menuItem.ToString();
        }

        private void GenerateYTData()
        {
            if (cbGenForAll.Checked)
            {
                GenerateYTDataForAll();
                return;
            }
            StringBuilder menuItem = new StringBuilder();

            if (cbTitle.Checked)
            {
                menuItem.AppendLine("name=\"" + tbTitle.Text + "\"");
            }
            else
            {
                menuItem.AppendLine("name=\" \"");
            }

            menuItem.AppendLine("section=\"false\"");
            menuItem.AppendLine("subid=\"false\"");

            if (rbPlaylist.Checked)
            {
                menuItem.AppendLine("playlistid=\"" + tbShorcut.Text + "\"");
            }
            else
            {
                menuItem.AppendLine("playlistid=\"false\"");
            }
            if (rbChannel.Checked)
            {
                menuItem.AppendLine("channelid=\"" + tbShorcut.Text + "\"");
            }
            else
            {
                menuItem.AppendLine("channelid=\"false\"");
            }
            if (rbYTVideo.Checked)
            {
                menuItem.AppendLine("videoid=\"" + tbShorcut.Text + "\"");
            }
            else
            {
                menuItem.AppendLine("videoid=\"false\"");
            }

            if (cbThumb.Checked)
            {
                menuItem.AppendLine("icon=\"" + tbThumb.Text + "\"");
            }
            else
            {
                menuItem.AppendLine("icon=\"http://\"");
            }
            menuItem.AppendLine("fanart=\"http://\"");
            if (cbTitle.Checked)
            {
                menuItem.AppendLine("description=\"" + tbTitle.Text + "\"");
            }
            else
            {
                menuItem.AppendLine("description=\" \"");
            }
            menuItem.AppendLine();

            tbMenuFile.Text = menuItem.ToString();
        }

        private void GenerateYTDataForAll()
        {
            if (dgvFavs.Rows.Count > 0)
            {
                StringBuilder menuItem = new StringBuilder();
                foreach (DataGridViewRow theRow in dgvFavs.Rows)
                {
                    string theShortcut = theRow.Cells[2].Value.ToString();
                    if (cbTitle.Checked)
                    {
                        menuItem.AppendLine("name=\"" + theRow.Cells[0].Value.ToString() + "\"");
                    }
                    else
                    {
                        menuItem.AppendLine("name=\" \"");
                    }
                    menuItem.AppendLine("section=\"false\"");
                    menuItem.AppendLine("subid=\"false\"");
                    if (rbPlaylist.Checked)
                    {
                        menuItem.AppendLine("playlistid=\"" + theRow.Cells[2].Value.ToString() + "\"");
                    }
                    else
                    {
                        menuItem.AppendLine("playlistid=\"false\"");
                    }
                    if (rbChannel.Checked)
                    {
                        menuItem.AppendLine("channelid=\"" + theRow.Cells[2].Value.ToString() + "\"");
                    }
                    else
                    {
                        menuItem.AppendLine("channelid=\"false\"");
                    }
                    if (rbYTVideo.Checked)
                    {
                        menuItem.AppendLine("videoid=\"" + theRow.Cells[2].Value.ToString() + "\"");
                    }
                    else
                    {
                        menuItem.AppendLine("videoid=\"false\"");
                    }
                    if (cbThumb.Checked)
                    {
                        menuItem.AppendLine("icon=\"" + theRow.Cells[1].Value.ToString() + "\"");
                    }
                    else
                    {
                        menuItem.AppendLine("icon=\"http://\"");
                    }
                    menuItem.AppendLine("fanart=\"http://\"");
                    if (cbTitle.Checked)
                    {
                        menuItem.AppendLine("description=\"" + theRow.Cells[0].Value.ToString() + "\"");
                    }
                    else
                    {
                        menuItem.AppendLine("description=\" \"");
                    }
                    menuItem.AppendLine();
                }
                tbMenuFile.Text = menuItem.ToString();
            }
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            tbMenuFile.Text = string.Empty;

            cbShortcut.Checked = false;
            cbThumb.Checked = false;
            cbTitle.Checked = false;
            cbGenForAll.Checked = false;

            rbChannel.Checked = false;
            rbPlain.Checked = false;
            rbPlaylist.Checked = false;
            rbURL.Checked = false;
            rbVideo.Checked = false;
            rbYTMenuFile.Checked = false;
            rbYTVideo.Checked = false;
        }

        #endregion Menu Generator related code

        private void btnCleanChannels_Click(object sender, EventArgs e)
        {
            if (dgvFavs.Rows.Count > 0)
            {
                int rowIndex = 0;
                foreach (DataGridViewRow theRow in dgvFavs.Rows)
                {
                    string theShortcut = theRow.Cells[2].Value.ToString();
                    if (theShortcut.Contains("%2Fchannel%2F"))
                    {
                        int theLength = theShortcut.IndexOf("%2Fchannel%2F") + 13;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("%2F"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("%2F"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    else if (theShortcut.Contains("/channel/"))
                    {
                        int theLength = theShortcut.IndexOf("/channel/") + 9;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("/"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("/"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    rowIndex++;
                }
            }
        }

        private void btnCleanVideos_Click(object sender, EventArgs e)
        {
            if (dgvFavs.Rows.Count > 0)
            {
                int rowIndex = 0;
                foreach (DataGridViewRow theRow in dgvFavs.Rows)
                {
                    string theShortcut = theRow.Cells[2].Value.ToString();
                    if (theShortcut.Contains("%2Fwatch%3Fv%3D%2F"))
                    {
                        int theLength = theShortcut.IndexOf("%2Fwatch%3Fv%3D%2F") + 18;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("%"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("%"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    else if (theShortcut.Contains("play/?video_id="))
                    {
                        int theLength = theShortcut.IndexOf("play/?video_id=") + 15;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("\""));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("\""), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    else if (theShortcut.Contains("play%2F%3Fvideo_id%3D"))
                    {
                        int theLength = theShortcut.IndexOf("play%2F%3Fvideo_id%3D") + 21;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("%"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("%"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    else if (theShortcut.Contains("%2Fwatch%3Fv%3D"))
                    {
                        int theLength = theShortcut.IndexOf("%2Fwatch%3Fv%3D") + 15;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("%"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("%"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    rowIndex++;
                }
            }
        }

        private void btnCleanPlaylists_Click(object sender, EventArgs e)
        {
            if (dgvFavs.Rows.Count > 0)
            {
                int rowIndex = 0;
                foreach (DataGridViewRow theRow in dgvFavs.Rows)
                {
                    string theShortcut = theRow.Cells[2].Value.ToString();
                    if (theShortcut.Contains("/playlist/"))
                    {
                        int theLength = theShortcut.IndexOf("/playlist/") + 10;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("/"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("/"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    else if (theShortcut.Contains("%2Fplaylist%2F"))
                    {
                        int theLength = theShortcut.IndexOf("%2Fplaylist%2F") + 15;
                        theShortcut = theShortcut.Remove(0, theLength);
                        theLength = theShortcut.Length - (theShortcut.IndexOf("%"));
                        theShortcut = theShortcut.Remove(theShortcut.IndexOf("%"), theLength);
                        dgvFavs.Rows[rowIndex].Cells[2].Value = theShortcut;
                    }
                    rowIndex++;
                }
            }
        }
    }
}
