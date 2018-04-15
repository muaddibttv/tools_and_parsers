using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Net;

namespace Tantrum_IPTV_Editor
{
    public partial class OpenURL : Form
    {
        public string fileContent { get; set; }
        public string filePath = "playlist.txt";

        public OpenURL()
        {
            InitializeComponent();
            statusStrip.Padding = new Padding(statusStrip.Padding.Left, statusStrip.Padding.Top, statusStrip.Padding.Left, statusStrip.Padding.Bottom);
        }

        private void buttonOpen_Click(object sender, EventArgs e)
        {
            if (tbURL.Text.Trim().Length == 0)
                return;

            try
            {
                toolStripStatusLabel.Text = "Checking if URL exists...";
                tbURL.Enabled = false;
                buttonOpen.Enabled = false;
                HttpWebRequest request = WebRequest.Create(tbURL.Text) as HttpWebRequest;
                request.Method = "HEAD";
                HttpWebResponse response = request.GetResponse() as HttpWebResponse;
                if (response.StatusCode == HttpStatusCode.OK)
                {
                    toolStripStatusLabel.Text = "URL exists, starting with download...";
                    using (var webClient = new WebClient())
                    {
                        try
                        {
                            webClient.DownloadFileCompleted += webClient_DownloadFileCompleted;
                            webClient.DownloadProgressChanged += webClient_DownloadProgressChanged;
                            webClient.DownloadFileAsync(new Uri(tbURL.Text.Trim()), filePath);
                        }
                        catch (Exception ex)
                        {
                            toolStripStatusLabel.Text = "Download Error...";
                            MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                            tbURL.Enabled = true;
                            buttonOpen.Enabled = true;
                            toolStripStatusLabel.Text = "Enter URL and press Open...";
                        }
                    }
                }
                else
                {
                    throw new WebException();
                }
            }
            catch
            {
                toolStripStatusLabel.Text = "URL Error...";
                MessageBox.Show("Cannot open URL!", "URL Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                tbURL.Enabled = true;
                buttonOpen.Enabled = true;
                toolStripStatusLabel.Text = "Enter URL and press Open...";
            }
        }

        void webClient_DownloadProgressChanged(object sender, DownloadProgressChangedEventArgs e)
        {
            toolStripStatusLabel.Text = "Downloading ...";
            toolStripProgressBar.Value = e.ProgressPercentage;
        }

        void webClient_DownloadFileCompleted(object sender, AsyncCompletedEventArgs e)
        {
            if (e.Error != null)
            {
                toolStripStatusLabel.Text = "URL Error...";
                MessageBox.Show(e.Error.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                tbURL.Enabled = true;
                buttonOpen.Enabled = true;
                toolStripStatusLabel.Text = "Enter URL and press Open...";
            }
            else
            {
                toolStripStatusLabel.Text = "Successfully Downloaded!";
                MessageBox.Show("File was successfuly downloaded and saved.", "File saved", MessageBoxButtons.OK, MessageBoxIcon.Information);
                DialogResult = DialogResult.OK;
                Close();
            }
        }

        private void buttonCancel_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.Cancel;
            Close();
            Dispose();
        }

        private void toolStripProgressBar_Click(object sender, EventArgs e)
        {

        }
    }
}
