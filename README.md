# Directory cleaning tools
 Multiple directory managment tools for python  


## File class- 
 A comfotable class containing usfull file data for files inside pointer directory.
 ### init:
        self.name - File name
        self.path - Directory path
        self.full_path - Full path including filename and extention
        self.is_dir - Is The file a directory? 
        self.extension - File extension.
        
 ### Usefull methods:
		-move_file_by_extention(self) moves file to a directory named as its extension (mp3,js, etc...)
		-move_file_to_path(self, path) moves file to an argument given path.
		-move_file_by_year(self) moves file to a directory named as its creation year

## DirPointer-
 A class object acting as a directory pointer. 
 
 ### init: 
        self.dir_path - current path of pinter
        self.file_list - A list of current directory's files
 ### Usefull methods:
		-Get_in_dir(dir_name), get_out_of_dir() are pretty much self explainitory.
		-get_dirs_only(self) returns a list of all directories in current pointer path.
		-get_files_only(self) returns a file list of all files in current pointer path.
		-get_all_branching_files(self) returns a file list of all the files found in branching directorie.
  
# Basic work-flow
Basically you can go to any messy folder, 
