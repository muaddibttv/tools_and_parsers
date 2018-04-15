using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Tantrum_IPTV_Editor
{
    class textoperations
    {
        public static string Between(string strSource, string strStart, string strEnd)
        {
            int Start, End;
            string strSourceCompare = strSource.ToLower();
            if (strSourceCompare.Contains(strStart) && strSourceCompare.Contains(strEnd))
            {
                Start = strSourceCompare.IndexOf(strStart, 0) + strStart.Length;
                End = strSourceCompare.IndexOf(strEnd, Start);
                return strSource.Substring(Start, End - Start);
            }
            else
            {
                return "";
            }
        }
    }
}
