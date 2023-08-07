# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import re


def checkMime(file):
    photosMime = r'\.(jpg|jpeg|png|hexc)'
    documentsMime = r'\.(pdf|xdl|odt|xml)'
    audioMime = r'\.(wav|mp3|mp4)'
    root = os.getcwd()
    if re.search(photosMime, file):
        command = f"mv {file} {photos}"
        os.system(command)
        print(os.system(command))



    elif re.search(documentsMime, file):
        command = f"mv {file} {documents}"
        print(os.system(command))

    elif re.search(audioMime, file):
        command = f"mv {file} {audio}"
        os.system(command)

        print(file)


    else:
        print("nothing")


def checkFileTypes(list):
    i = 0

    while i < len(list):
        print(list[i])
        mimeType = checkMime(list[i])
        i += 1;


def print_hi(name):
    list_of_files = [];
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    current_dir = os.getcwd()

    for root, dirs, files in os.walk(current_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_path = str(file_path)
            list_of_files.append(file_path)

    checkFileTypes(list_of_files);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_dir = os.getcwd()
    temp=str(current_dir)
    photos=str(temp+'/Photos')
    documents=str(temp+'/Documents')
    audio=str(temp+'/Audio')
    os.system(f'mkdir {photos}')
    os.system(f'mkdir {documents}')
    os.system(f'mkdir {audio}')

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# get  directory
# create directorry
# move
