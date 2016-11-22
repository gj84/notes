using System;
using System.IO;

namespace Application
{
    public class MasiveNameChanger
    {

        public static void changeName(string oldname, string newname)
        {
            if (File.Exists (oldname)) {
                System.IO.File.Move(oldname, newname);
            }
         }

        public static string getNewName(string oldname)
        {
            string content = oldname.Split ('(') [0];
            string number = oldname.Split ('(') [1].Split('-')[0];
            number = number.PadLeft (2, '0');
            string extension = ".mp4";
            string newname = number + '-' + content + extension;
            return newname;
        }

        public static void procesDir(string dirname){
            if (Directory.Exists (dirname)) {
                string[] listDir = Directory.GetFiles (dirname);
                foreach (string absfilename in listDir) {
                    string filename = Path.GetFileName (absfilename); 
                   
                    string newname = getNewName (filename);
                    string absnewname = dirname + '/' + newname;
                    changeName (absfilename, absnewname);
                    Console.WriteLine ("Filename '{0}' changed to '{1}'", absfilename, absnewname);
                }
            }
        }

        static void Main(String[] args)
        {
            if (args.Length > 0) {
                if (Directory.Exists (args [0])) {
                    procesDir (args [0]);
                }
            }
        }
    }
}

