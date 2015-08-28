'''
 - To get the .webp images to display I needed to install the 'pillow' package.
 - I also wasn't able to get easygui working from cygwin. I needed to use cmd.exe
'''
from easygui import buttonbox
import json
import os.path

def main():
    with open('users_data.json', 'r') as f:
         users_data = json.load(f)
    usernames = users_data.keys()

    for username in usernames:
        current_user_data = users_data[username]
        image_number = 0
        while True:
            image = "profiles/" + username + "/" + str(image_number) + ".webp"
            if not os.path.isfile(image):
                break
            msg   = "Should this person be sent messages?"
            choices = ["Previous image","Next image","Yes","No"]
            reply=buttonbox(msg,image=image,choices=choices)
            if reply == "Yes":
                current_user_data['should_be_messaged'] = True
                break
            elif reply == "No":
                current_user_data['should_be_messaged'] = False
                break
            elif reply == "Previous image":
                image_number = max(image_number - 1, 0)
                continue
            elif reply == "Next image":
                image_number = min(image_number + 1, 2)
                continue
'''
        users_data[username] = current_user_data
        with open('users_data.json', 'w') as outfile:
            json.dump(users_data, outfile)
'''

if __name__ == '__main__':
    main()