'''
"...directory is actually no more than a file, but its contents are controlled by the system, and the contents are names of other files. (A directory is sometimes called a catalog in other systems.)" 
- Dennis Ritchie, 1972 
'''


import os
import datetime


class File():
    def __init__(self, path, name):
        self.name = name
        self.path = path+'\\'
        self.full_path = self.path+self.name
        # If True its a directory, else, it is a file
        self.is_dir = os.path.isdir(
            self.full_path)
        self.extension = os.path.splitext(self.full_path)[1]

    def __str__(self):
        return self.name

    # This method return the string represenation for list etc...
    def __repr__(self):
        return self.__str__()

    def get_file_creation_year(self):
        return str(datetime.datetime.fromtimestamp(os.path.getctime(self.full_path)).date()).split('-')[0]

    def change_name(self, new_name):
        os.rename(self.full_path, self.path+new_name)

    def move_to(self, path):
        pass

    def move_file_to_path(self, path): #move File to certain path
        os.replace(self.full_path,path+'\\'+self.name)

    def move_file_by_extention(self): #move file to a directory named as its format
        extension = self.extension
        if not self.is_dir:
            try:
                os.mkdir(self.path+self.extension)
            except FileExistsError:
                print(f'{self.extension} Directory exists!')
            os.replace(self.full_path, self.path +
                       self.extension+'\\'+self.name)
    
    def move_file_by_year(self):
        year= self.get_file_creation_year()
        if not self.is_dir:
            
            try:
                os.mkdir(self.path+year)
            except FileExistsError:
                print(f'{year} Directory exists!')
            os.replace(self.full_path, self.path +
                       year+'\\'+self.name)

    def move_by_year(self):
        pass


class DirPointer():
    def __init__(self, dir_path):
        self.dir_path = dir_path+'\\'
        # Get a list of file objects
        self.file_list = self.set_file_objects()
        # self.file_list = os.listdir(dir_path)
       

    def get_dirs_only(self):
        return list(filter(lambda file: file.is_dir, self.file_list))

    def get_files_only(self):
        return list(filter(lambda file: not file.is_dir, self.file_list))

    def set_file_objects(self):
        return[File(self.dir_path, filename) for filename in os.listdir(self.dir_path)]

    # Get in to a directory
    def get_in_dir(self, dirname):
        self.dir_path += dirname+'\\'
        # File path needs to be reassigned as it is only initialized opun instantiation
        self.file_list = self.set_file_objects()

    # Get out of a directory
    def get_out_of_dir(self):
        self.dir_path = '\\'.join(self.dir_path.split('\\')[0:-2])+'\\'
        self.file_list = self.set_file_objects()

    def __str__(self):
        return f'PATH: {self.dir_path} \nCONTENTS {self.file_list}'

    # move through all branching directories by reccurssion to get a list of all files

    

             
    def get_all_branching_files(self):
        files=[]
        def recurse_branching_dirs():

            if len(self.get_dirs_only()) == 0:
                return self.get_files_only()
            else:
                files.append(self.get_files_only())

            for dir in self.get_dirs_only():
                self.get_in_dir(dir.name)
                files.append(recurse_branching_dirs())
                self.get_out_of_dir()

        recurse_branching_dirs()

        return [item for sublist in files if sublist != None for item in sublist]
        

def main():
    cwd = os.getcwd()
    # pointer = DirPointer(cwd)


    # branching_files = pointer.file_list

    # print(branching_files)
    # for file in branching_files:
    #     file.move_file_by_extention()

if __name__ == '__main__':
    main()
