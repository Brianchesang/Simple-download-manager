Download-manager
This code is a Python script that organizes files in the user's Downloads folder on a Windows operating system. The script categorizes files based on their file extensions and moves them to their respective folders in the Downloads directory.

The script starts by importing the os and shutil modules. The os module is used for interacting with the operating system, while the shutil module is used for file operations. The path to the Downloads directory is specified using the downloads_path variable, and the list of files in the directory is obtained using the os.listdir() method and stored in the file_names variable.

The code then defines several functions that group files based on their extensions:

images(): groups image files with extensions such as .ai, .bmp, .gif, etc.
videos(): groups video files with extensions such as .avi, .flv, .mp4, etc.
text_files(): groups text files with extensions such as .doc, .txt, .pdf, etc.
spreadsheets_files(): groups spreadsheet files with extensions such as .xls, .xlsx, .ods, etc.
presentation_files(): groups presentation files with extensions such as .ppt, .pptx, .odp, etc.
executable_files(): groups executable files with extensions such as .exe, .bat, .py, etc.
compressed_files(): groups compressed files with extensions such as .zip, .tar, .rar, etc.
The directory_maker() function creates new directories to organize files into. It creates a new directory for each file type and checks if the directory already exists. If the directory does not exist, it creates a new directory with the name of the file type.

The move_files() function uses the shutil.move() method to move the executable files from the Downloads directory to the "Download_Programs" directory created by directory_maker().

Finally, the script calls the move_files() function to move executable files to the appropriate folder and prints the list of files in the Downloads folder.

To use this script, the user should copy and paste it into a Python editor, save it with a .py extension, and run it on their Windows operating system. The script will then organize the files in the Downloads directory into different folders according to their file type.
