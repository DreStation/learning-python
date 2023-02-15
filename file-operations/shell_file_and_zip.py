import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def create_file(file_name):
    file = open(file_name, "w+")
    file.write("🐍 Sss!")

def backup_file(file_name):
    if (path.exists(file_name)):
        src = path.realpath(file_name)

        # Make a backup (append .bak)
        dst = src + ".bak"
        shutil.copy(src, dst)
    else:
        print("Error: cannot find file \"%s\""% file_name)

def rename_file(original, new):
    if (path.exists(original)):
        os.rename(original, new)
    else:
        print("Error: cannot find file \"%s\""% original)

def zip_file(file_name):
    if (path.exists(file_name)):
        # Include everything in this repo
        #src = path.realpath(file_name)
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

        # Include just this specified file
        with ZipFile("archive.zip", "w") as zip:
            zip.write(file_name)
    else:
        print("Error: cannot find file \"%s\""% file_name)

def main():
    create_file("snake.txt")
    backup_file("snake.txt")
    rename_file("snake.txt", "new_snake.txt")
    zip_file("new_snake.txt")

if __name__ == "__main__":
    main()