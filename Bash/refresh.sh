
# Save the password in a variable (not recommended, just for example purposes)
PASSWORD="reve"

# Run sudo to extend the timeout and cache the password
echo "$PASSWORD" | sudo -Sv

# Run other commands using sudo without entering the password
sudo apt update
sudo apt upgrade -y


chromium-browser

