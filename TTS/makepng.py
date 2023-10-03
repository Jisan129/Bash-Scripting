import sys
import base64
import getpass


base64_encoded="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"


binary_data = base64.b64decode(base64_encoded)
username=getpass.getuser();

with open(f'/home/{username}/Documents/decoded_image.png', 'wb') as image_file:
     image_file.write(binary_data)

