# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    current_dir=os.getcwd()

    '''os.system(f'mkdir {current_dir}/Photos')
    os.system(f'mkdir {current_dir}/Deb')
    os.system(f'mkdir {current_dir}/pdf')'''
    for root,files,dirs in os.walk(current_dir):
        for file in files:
            temp=os.path.join(root,file)
            print(temp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#get  directory
#create directorry
#move
