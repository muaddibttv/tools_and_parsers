using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Kodi_M3U_IPTV_Editor
{
   
    public partial class tester : Form
    
    {
        //Editor edit = new Editor();
        
        public tester()
        {
            InitializeComponent();
        }

        public void tester_Load(object sender, EventArgs e)
        {
            
        }

        private void axVLCPlugin1_Enter(object sender, EventArgs e)
        {
           
            
            //axVLCPlugin1.addTarget(edit.stream.Text, null, AXVLC.VLCPlaylistMode.VLCPlayListInsert, 0);
            axVLCPlugin1.play();

        }
    }
}
