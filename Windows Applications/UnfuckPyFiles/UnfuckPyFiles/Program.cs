using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnfuckPyFiles
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0 || args[0].Contains("?"))
            {
                Console.WriteLine("Please use the following commands:");
                Console.WriteLine("UnFuckPyFiles <input file> <output file> <lines>");
                Console.WriteLine(" ");
                Console.WriteLine("input file: Python .py file to process");
                Console.WriteLine("output file: Python .py file to write modifications to");
                Console.WriteLine("lines: number of lines from input file to copy into output before writing unfuck code");
                Console.WriteLine(" ");
                Console.WriteLine("Encoded files using magic, joy, etc typically can have <lines> set to 7");
                return;
            }

            string input_file = args[0];
            string output_file = args[1];

            int line_count = Convert.ToInt32(args[2]);
            bool chk = true;
            File.Copy(input_file, output_file);
            Console.WriteLine("MuadDib is now bending The Joker over....");
            while (chk)
            {
                chk = ProcessFile(output_file, line_count);
                if (File.Exists("temp_" + output_file))
                {
                    if (File.Exists(output_file))
                        File.Delete(output_file);
                    File.Move("temp_" + output_file, output_file);
                }
            }
            if (File.Exists("iambatman.py"))
                File.Delete("iambatman.py");
            Console.WriteLine("The Joker is now his bitch. Your file has been unfucked.");
        }

        private static bool ProcessFile(string output_file, int line_count)
        {
            string temp_file = "temp_" + output_file;

            string[] strArray = File.ReadAllLines(output_file);
            int num = 0;
            bool magic_check = false;
            if (File.Exists("iambatman.py"))
                File.Delete("iambatman.py");
            using (StreamWriter streamWriter = new StreamWriter("iambatman.py"))
            {
                foreach (string str in strArray)
                {
                    if (num < line_count)
                    {
                        if (str.IndexOf("magic") == 0)
                            magic_check = true;
                        streamWriter.WriteLine(str);
                        ++num;
                    }
                }
                streamWriter.WriteLine("print(base64.b64decode(trust))");
            }
            if (magic_check)
            {
                Process p = new Process();
                p.StartInfo.FileName = "python";
                p.StartInfo.Arguments = "iambatman.py";
                p.StartInfo.UseShellExecute = false;
                p.StartInfo.RedirectStandardOutput = true;
                p.StartInfo.CreateNoWindow = true;
                p.Start();
                string output = p.StandardOutput.ReadToEnd();
                p.WaitForExit(1000 * 10);
                File.WriteAllText(temp_file, output.Replace("\r", ""));
            }
            return magic_check;
        }
    }
}
