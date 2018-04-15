using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace YTThumbCollector
{
    public partial class TheForm : Form
    {
        private string fileSaveLoc = null;
        private string[] videoIDList;
        private Dictionary<string, string> imageList = new Dictionary<string, string>();
        private bool useID = false;

        public TheForm()
        {
            InitializeComponent();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            tbVideoIDList.Text = "";
            return;
        }

        private void btnRun_Click(object sender, EventArgs e)
        {
            if (!rbVideoID.Checked && !rbVideoName.Checked && !rbInOrder.Checked)
            {
                MessageBox.Show("You need to select a naming convention for the images first!");
                return;
            }
            else
                useID = rbVideoID.Checked;

            if (fileSaveLoc == null)
            {
                MessageBox.Show("You need to select a save location first!");
                return;
            }

            lblWorking.Text = "Preparing List";
            panelWorking.Visible = true;

            processList();
        }

        private void processList()
        {
            videoIDList = tbVideoIDList.Text.Split(new string[] { Environment.NewLine }, StringSplitOptions.None);
            imageList.Clear();

            lblWorking.Text = "Gathering Links";
            MessageBox.Show("Ready to do this!");
            try
            {
                int i = 1;
                foreach (string theID in videoIDList)
                {
                    if (theID.Trim().Length < 1)
                        continue;

                    ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
                    WebClient webClient = new WebClient();
                    string htmlString = webClient.DownloadString("https://www.youtube.com/watch?v=" + theID.Trim());

                    string fileName;
                    if (useID)
                        fileName = theID.Trim() + ".jpg";
                    else if (rbVideoName.Checked)
                    {
                        string theTitle = htmlString.Substring(htmlString.IndexOf("og:title") + 19, 200);
                        theTitle = theTitle.Remove(theTitle.IndexOf("\""));
                        foreach (var c in Path.GetInvalidFileNameChars()) { theTitle = theTitle.Replace(c, '-'); }
                        fileName = theTitle + ".jpg";
                    }
                    else
                    {
                        fileName = i + ".jpg";
                        i++;
                    }

                    string theLink = htmlString.Substring(htmlString.IndexOf("og:image") + 19, 200);
                    theLink = theLink.Remove(theLink.IndexOf("\""));

                    imageList.Add(fileName, theLink);
                }
            }
            catch
            {
                MessageBox.Show("Something went wrong gathering links. Try again.");
                panelWorking.Visible = false;
                return;
            }

            lblWorking.Text = "Downloading Images";

            try
            {
                foreach (KeyValuePair<string, string> pair in imageList)
                {
                    string theFilename = pair.Key;
                    string thisLink = pair.Value;

                    using (WebClient client = new WebClient())
                    {
                        client.DownloadFile(new Uri(thisLink), fileSaveLoc + @"\" + theFilename);
                    }
                }
            }
            catch
            {
                MessageBox.Show("Something went wrong while download. Try again");
                panelWorking.Visible = false;
                return;
            }
            MessageBox.Show("All Thumbnails have been downloaded.");
            System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo()
            {
                FileName = fileSaveLoc,
                UseShellExecute = true,
                Verb = "open"
            });
            panelWorking.Visible = false;
        }

        private void btnSaveLocation_Click(object sender, EventArgs e)
        {
            // Show the FolderBrowserDialog.
            DialogResult result = folderBrowserDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                fileSaveLoc = folderBrowserDialog1.SelectedPath;
                tbFolder.Text = fileSaveLoc;
            }
        }
    }
}
