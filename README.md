# Amridell's Easy to Use CYOA creator (AKA how I make CYOAs)
I can't use photoshop, so I did a few CYOAs in HTML. Eventually I thought to myself "Hey, I should automate this". I felt like an idiot for doing all that work over and over in a text editor.

# How to use this
YOU MUST HAVE PYTHON 3.5 AND DJANGO 1.9 FOR THIS TO WORK. I HAVE NOT TESTED WITH OTHER VERSIONS BUT THEY MIGHT WORK. IF YOU'RE NOT SURE, USE THOSE.
Installing Python (Thank you Derek Banas): https://www.youtube.com/watch?v=EU8L9SMH8K0
Installing Django (Thank CodingEntrepreneurs for this because I don't remember how to explain this one): https://www.youtube.com/watch?v=QhevHKBy7Hc
First you'll need to bring up the server. Download the repo, copy it so you don't have to come back and redownload, then navigate into your copied directory.
Next, shift-right-click in the directory. Click "Open command prompt here".
Type "python manage.py runserver"
Go to 127.0.0.1 in a web browser. You should see the demo CYOA pop up.
Log in using the username "admin" and the password "AveryTGpassword" at 127.0.0.1/admin, this will allow you to edit the CYOA.
You only need one introduction.
Sections are the large bits, contents are the small ones. A content must be mapped to a section.
Images should be stored under static/options/images/. This will help you organize and make everything easier.
Enter in your stuff. This is the actually making the CYOA part.
You can then take a screenshot using full page screen capture for chrome/firefox. Crop and compress to taste. Upload where you please.
You can edit options/templates/options/index.html and static/options/layout.css to change the look and feel.

# Examples
https://i.imgur.com/DvHT6is.jpg
https://i.imgur.com/yqjOKWb.png
