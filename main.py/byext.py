import os
from pathlib import Path

class f_formats:
    def __init__(self):
        self.DIRECTORIES = {
            "HTML": [".html5", ".html", ".htm", ".xhtml"],
            "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                       ".heif", ".psd"],
            "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                       ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
            "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                          ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                          ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                          "pptx"],
            "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                         ".dmg", ".rar", ".xar", ".zip"],
            "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                      ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
            "PLAINTEXT": [".txt", ".in", ".out"],
            "PDF": [".pdf"],
            "PYTHON": [".py"],
            "XML": [".xml"],
            "EXE": [".exe"],
            "SHELL": [".sh"]
            }
        
        
    def get_file_formats(self,dirr):
        
        self.FILE_FORMATS = {f_format: directory
                for directory, f_formats in dirr.items()
                for f_format in f_formats}
        return self.FILE_FORMATS

class jfile_organizer(f_formats):
    
    def __init__(self,pathh):
        self.paath=pathh
        super().__init__()
        self.FILE_FORMATS=super().get_file_formats(self.DIRECTORIES)


    def organize_files(self):
        direct=self.paath
        os.chdir(direct)
        for entry in os.scandir():
            if entry.is_dir():continue
            file_path = Path(entry.name)
            file_format = file_path.suffix.lower()
            if file_format in self.FILE_FORMATS:
                directory_path = Path(self.FILE_FORMATS[file_format])
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path))
        #if extension not present in the dctionary than create a folder name "OTHER"
        try:
            os.mkdir("OTHER")
        except:
            pass
        for path in os.scandir():
            try:
                if path.is_dir():
                    os.rmdir(path)
                else:
                    os.rename(os.getcwd() + '/' + str(Path(path)), os.getcwd() + '/OTHER/' + str(Path(path)))
            except:
                pass
jf=jfile_organizer("D:\\")
jf.organize_files()