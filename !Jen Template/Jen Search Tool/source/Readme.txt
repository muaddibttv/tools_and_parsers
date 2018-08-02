How to Make a Search DB for Jen

Make sure you have python 2.7.x installed and that you pip install requests.
If you wish to help update this file to work under both 2.7 and 3.x, please let someone know.
    - Currently, the ConfigParser code needs to be updated to work under both 2.7 and 3.x

==== Configuration of the Script ====
- Open the Config.ini file
- Set the two lines in the [addon] section to the Name and ID of your Jen.
    - This is just for saving multiple copies of search db generators. So they are easy for you to keep track of.
- Set the output_path relative to where you want the files saved to.
    - Recommend a subfolder of where you keep this script. If a subfolder as such, prepend the path with ./ like the example
- Set the sections_xml to the name of the file you have set up containing all the sections you want to index for search
    - Make sure the xml is in the same folder as the script.

==== Creating your Search DB File and using it ====
- Run the script under Python 2.7.15 (recommended). Not 3.x
- Files will be saved to the output_path
- Save the db file inside your addon, or on your server where the xmls are locations if remote hosting them
- Open settings.xml and ensure that the search_db_location is set to your search.db file accordingly


