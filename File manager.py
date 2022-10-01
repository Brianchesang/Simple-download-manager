import os 
import shutil

downloads_path = ('C:/Users/user/Downloads')
file_names = os.listdir(downloads_path)


def images(list):
    image_extensions=(".ai" , ".bmp" , ".gif" , ".ico" , ".Jpeg" , ".jpg" , ".max" , 
        ".obj" , ".png" , ".ps" , ".psd" , ".svg" , ".tif" , ".tiff" , ".3ds" , ".3dm")
    for file in file_names:
        if file.endswith (image_extensions):
           print(os.path.join(downloads_path, file))


def videos(list):
    video_extensions=(".avi",".flv",".h264",".m4v",".mkv",".mov",	
    ".mp4",".mpg ",".mpeg",".rm",".swf",".vob",".wmv",".3g2",".gp"	)
    for file in file_names:
        if file.endswith(video_extensions):
            print(file)

def text_files(list):
    documents_extensions = (".doc",".docx",".odt",".msg",".pdf",".rtf",".tex",".txt",".wks",".wps",".wpd"	)
    for file in file_names:
        if file.endswith (documents_extensions):
           print(os.path.join(downloads_path, file))

def spreadsheets_files(list):
    spreadsheet_extensions = (".ods",".xlr" ,".xls"	,".xlsx"	)
    for file in file_names:
        if file.endswith (spreadsheet_extensions):
           print(os.path.join(downloads_path, file))


def presentation_files(list):
    presentation_extensions = (".ods",".xlr",".xls",".xlsx"	)
    for file in file_names:
        if file.endswith (presentation_extensions):
           print(os.path.join(downloads_path, file))

def Executable_files(list):
    executables = []
    
    executable_extensions = (".apk",".bat",".bin",".cgi",".com",".exe",".jar",".py",".wsf")
    for file in file_names:
        if file.endswith (executable_extensions):
            temp_e = (os.path.join(downloads_path, file))
            executables.append(temp_e) 
    
    return executables

def compressed_files(list):
    compressedfiles_extension = (".7z",".arj",".deb",".pkg",".rar",".rpm",".tar",".gz",".z",".zip")
    for file in file_names:
        if file.endswith (compressedfiles_extension):
           print(os.path.join(downloads_path, file))


def directory_maker(list):
    Videos = os.path.join(downloads_path, "Download_Videos")
    Audeos = (os.path.join(downloads_path, "Download_Audios"))
    Programs = (os.path.join(downloads_path, "Download_Programs"))
    Compressed = (os.path.join(downloads_path, "Download_Compressed Files"))
    Text = (os.path.join(downloads_path, "Download_Text Files"))
    spreadsheets = (os.path.join(downloads_path, "Download_Spreadsheets"))
    presentations = (os.path.join(downloads_path, "Download_Presentations"))
    Images = (os.path.join(downloads_path, "Download_Images"))
    if "Download_Videos" not in file_names:
        os.mkdir(Videos)
    if "Download_Audios" not in file_names:
        os.mkdir(Audios)
    if "Download_Programs" not in file_names:
        os.mkdir(Programs)
    if "Download_compressed Files" not in file_names:
        os.mkdir(Compressed)
    if "Download_Text Files" not in file_names:
        os.mkdir(Text)
    if "Download_Spreadsheets" not in file_names:
        os.mkdir(spreadsheets)
    if "Download_Presentations" not in file_names:
        os.mkdir(presentations)
    if "Download_Images" not in file_names:
        os.mkdir(Images)
    return Videos , Audios , Programs , Compressed , Spreadsheets , Presentations , Images; 

def move_files():
    shutil.move(Executable_files(downloads_path), os.path.join(downloads_path, "Download_Programs"))
     

#directory_maker(file_names)
move_files()
#print(file_names)

#prog_checker(file_names)
#compressed_files(file_names)
#directory_maker(file_names)