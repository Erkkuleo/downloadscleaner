# Downloadscleaner

## Overview

This Python script organizes files in the user's "Downloads" directory based on their file extensions into specific folders for Videos, Images, Documents, Compressed files, Installers, Music, and Other.

## Usage
1. Ensure that Python is installed on your system.
2. Copy and paste the code into a Python file (e.g., organize\_downloads.py).
3. Run the script in a terminal or command prompt.

## Constraints and Dictionary
1. Folder Constants

    VIDEOS_FOLDER: Destination for Video files.
    PICTURES_FOLDER: Destination for Image files.
    DOCUMENTS_FOLDER: Destination for Document and Compressed files.
    HOME_FOLDER: Destination for Installer files.
    MUSIC_FOLDER: Destination for Music files.
    OTHER_FOLDER: Destination for files not matching any predefined category.

2. File Categories Dictionary

    'Video': Files with extensions 'mp4'.
    'Music': Files with extensions 'mp3'.
    'Images': Files with extensions 'jpg', 'png', 'jpeg'.
    'Documents': Files with extensions 'txt', 'pdf', 'csv', 'xls', 'xlsx'.
    'Compressed': Files with extensions 'zip', 'tar'.
    'Install': Files with extensions 'dmg', 'exe', 'iso'.

## Implementatiom
1. File Listing
    Retrieves the list of files in the user's "Downloads" directory, excluding hidden files.

2. Categorization
    ```
    mapping = collections.defaultdict(list)

    for file in filesList:
        if file[0] != '.':
            _, file_ext = os.path.splitext(file)
            mapping[file_ext].append(file)

    ```

3. Organizing Files
    Moves files to their  respective folders based on their categories.
    ```
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
    ```
## Note
    Ensure that the necessary folders exist ('Videos', 'Pictures', 'Documents', 'Home', 'Music', 'Other') in the specified destination path.
    The script may overwrite files if there are name conflicts in the destination folders.

## Disclaimer
    Use this script at your own risk. It's recommended to back up your files before running any script that modifies file locations.
