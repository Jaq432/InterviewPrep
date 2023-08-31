# The goal of this program is to make a file organizer. 
# In the folder is a myriad of different files that all need organizing.
# It is our duty, if we choose to accept it, to put them where they belong.
# (Where they belong is in folders corresponding to their extension)
#
# Hits at the bottom of the file

import os

fileExtensions = {
    'pdf': "PDFs",
    'png': "Images",
    'jpg': "Images",
    'jpeg': "Images",
    'gif': 'Images',
    'doc': 'Documents',
    'docx': 'Documents',
    'txt': 'Documents',
    'csv': 'Data',
    'xlsx': 'Data',
    'zip': 'Archive',
    'rar': 'Archive',
    'exe': 'Executables',
    'mp3': 'Music',
    'wav': 'Music',
    'mp4': 'Videos',
    'avi': 'Videos',
    'flv': 'Videos',
    'wmv': 'Videos',
}


for extension in fileExtensions:
    fileName = f'ima{extension}.{extension}'
    file = open(fileName,'w')
    file.close()





# Hints

# Use the import os module to perform operating system functions
# ----------------------------------------------------------
# Use the os.getcwd() command to get the current file's location
# ----------------------------------------------------------
# 