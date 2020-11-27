import click
import os
import fnmatch
import shutil
from pathlib import Path

# File Sorting and Organization


def organize_files_by_keyword(keyword, current_dir_path):
    for file in os.listdir(current_dir_path):
        if fnmatch.fnmatch(file, '*' + keyword + '*'):
            # print("Found:", file, os.path.isfile(file))
            if not os.path.isdir(current_dir_path + keyword):
                os.makedirs(current_dir_path + keyword)
            print("Moving File:", file)
            shutil.move(current_dir_path + file, current_dir_path + keyword + "/")


@click.group()
@click.version_option(version='1.00', prog_name='file_organizer')
def main():
    pass
@main.command()
@click.argument('current_path', default='./')
@click.option(
    '--keyword',
    '-k',
    help="Specify Keyword to Search Default is Date",
    default='Size')
def organize(current_path, keyword):    
    if (keyword == "Size"):
        for file in os.listdir(current_path):
            # print(current_path+file)
            statInfo = os.stat(current_path + file)

            if (statInfo.st_size >= 0 and statInfo.st_size <= 10):
                # print(statInfo.st_size)
                if (not os.path.isdir(current_path + "SMALL")):
                    os.makedirs(current_path + "SMALL")
                # print("Moving File", file)
                shutil.move(current_path + file, current_path + "/SMALL")

            elif (statInfo.st_size >= 10 and statInfo.st_size <= 100):
                if (not os.path.isdir(current_path + "MEDIUM")):
                    os.makedirs(current_path + "MEDIUM")
                # print("Moving File", file)
                shutil.move(current_path + file, current_path + "/MEDIUM")

            elif (statInfo.st_size >= 100 and statInfo.st_size <= 1000):
                if (not os.path.isdir(current_path + "LARGE")):
                    os.makedirs(current_path + "LARGE")
                # print("Moving File", file)
                shutil.move(current_path + file, current_path + "/LARGE")

            elif (statInfo.st_size >= 1001 and statInfo.st_size <= 16000):
                if (not os.path.isdir(current_path + "HUGE")):
                    os.makedirs(current_path + "HUGE")
                # print("Moving File", file)
                shutil.move(current_path + file, current_path + "/HUGE")

            elif (statInfo.st_size >= 16000):
                if (not os.path.isdir(current_path + "GIGANTIC")):
                    os.makedirs(current_path + "GIGANTIC")
                # print("Moving File", file)
                shutil.move(current_path + file, current_path + "/GIGANTIC")
        click.secho(
            ('Finished Organizing by date:{}'.format(keyword)), fg='green')
    else:
        organize_files_by_keyword(keyword, current_path)


if __name__ == '__main__':
    main()
