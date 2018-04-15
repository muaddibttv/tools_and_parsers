using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Tantrum_IPTV_Editor
{
    class Xmltv
    {
        private string _id, _name, _channels;
        public Xmltv(string id, string name, string channels)
        {
            _id = id;
            _name = name;
            _channels = channels;
        }

        public string ID {
            get { return _id; }
            set { _id = value; }
        }

        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public string Channels
        {
            get { return _channels; }
            set { _channels = value; }
        }
    }
}
