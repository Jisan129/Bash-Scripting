import  os
list_of_files = []
current_dir="/media/reve/New Volume/Bash/Bash"
for file in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, file)):
        file_path = os.path.join(current_dir, file)
        list_of_files.append(file_path)

for file_path in list_of_files:
    print(file_path)



cd Notion-linux-x64
./Notion