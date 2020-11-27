""" Junk file organizer"""
import os
import shutil
import os.path
import time

from datetime import datetime

"""this function is used to sort by date"""

def bydate():

    path = input("enter path directory :-")
    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    os.chdir(path)

    for x in files:

        """ Get the last modified time and the creation time"""

        modified_time_string = time.ctime(
            os.path.getmtime(os.path.join(path, x)))

        modified_datetime_obj = datetime.strptime(
         modified_time_string, '%a %b %d %H:%M:%S %Y')

        organized_date = str(modified_datetime_obj.day) + '-' + str(
         modified_datetime_obj.month) + '-' + str(modified_datetime_obj.year)

        if(os.path.isdir(organized_date)):
            shutil.move(os.path.join(path, x), organized_date)
        else:
            os.makedirs(organized_date)
            shutil.move(os.path.join(path, x), organized_date)

if __name__ == "__main__":
    bydate()