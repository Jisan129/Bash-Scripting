echo "hello from bash script"
sudo apt update 
sudo apt upgrade
y
#!/bin/bash

# Read the password from the user (you can also provide it as an argument or from a file)
echo -n "Enter your password: "
read -s password

# Run the sudo command with the -S option to read the password from standard input
echo "$password" | sudo -S your_command_here
chmod u+x refresh.sh