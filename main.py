import os
import collections

VIDEOS_FOLDER = 'Videos'
PICTURES_FOLDER = 'Pictures'
DOCUMENTS_FOLDER = 'Documents'
HOME_FOLDER = 'Home'
MUSIC_FOLDER = 'Music'
OTHER_FOLDER = 'Other'

file_categories = {
    'Video': ['mp4'],
    'Music': ['mp3'],
    'Images': ['jpg', 'png', 'jpeg'],
    'Documents': ['txt', 'pdf', 'csv', 'xls', 'xlsx'],
    'Compressed': ['zip', 'tar'],
    'Install': ['dmg', 'exe', 'iso']
}

path = os.path.expanduser('~')
downDir = os.path.join(path, 'Downloads')
mapping = collections.defaultdict(list)
filesList = os.listdir(downDir)

for file in filesList:
    if file[0] != '.':
        _, file_ext = os.path.splitext(file)
        mapping[file_ext].append(file)

for file_ext, filesList in mapping.items():
    destination_folder = OTHER_FOLDER

    if file_ext in (file_ext_list for file_category, file_ext_list in file_categories.items() if file_category != 'Other'):
        destination_folder = next(folder for folder, ext_list in file_categories.items() if file_ext in ext_list)

    destination_path = os.path.join(path, destination_folder)

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    for file in filesList:
        src_path = os.path.join(downDir, file)
        dest_path = os.path.join(path, destination_folder, file)
        os.rename(src_path, dest_path)
