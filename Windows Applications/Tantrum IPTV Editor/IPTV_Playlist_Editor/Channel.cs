using System;
using System.Collections.Generic;
using System.Text;
using System.ComponentModel;

namespace Tantrum_IPTV_Editor
{
    public class Channel : INotifyPropertyChanged
    {

        private string _Name, _channel, _tvid, _Group, _ip, _logo; //_epg, _image
        public event PropertyChangedEventHandler PropertyChanged;

        public Channel(int id, string Name, string ip, string Group = "", string logo = "", string tvid = "", string channel = "")
        {
            _Name = Name;
            _channel = channel;
            _tvid = tvid;
            _Group = Group;
            _logo = logo;
            _ip = ip;
        }

        public string Name
        {
            get { return _Name; }
            set
            {
                _Name = value;
                this.NotifyPropertyChanged("Name");
            }
        }

        public string ChannelID
        {
            get { return _channel; }
            set
            {
                _channel = value;
                this.NotifyPropertyChanged("Channel");
            }
        }

        public string EPG
        {
            get { return _tvid; }
            set
            {
                _tvid = value;
                this.NotifyPropertyChanged("EPG");
            }
        }

        public string Group
        {
            get { return _Group; }
            set
            {
                _Group = value;
                this.NotifyPropertyChanged("Group");
            }
        }

        public string IP
        {
            get { return _ip; }
            set
            {
                _ip = value;
                this.NotifyPropertyChanged("URL");
            }
        }

        public string Image
        {
            get { return _logo; }
            set
            {
                _logo = value;
                this.NotifyPropertyChanged("Logo");
            }
        }

        private void NotifyPropertyChanged(string value)
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(value));
        }
    }
}
