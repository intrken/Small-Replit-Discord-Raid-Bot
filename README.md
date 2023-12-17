# Small-Replit-Discord-Raid-Bot
How to use:
1. Go on [replit](https://replit.com/) and make an account if you don't have one
2. Make a replit by pressing **Create Repl** and choose search the template "python discord bot" and a template with that name should come up
3. Click "python discord bot" on the search bar and hit  "+ Create Repl"
4. If it says "Configure missing Secret values" click Dismiss
5. Delete everything in the script "main.py"
6. Paste the [source code](https://github.com/intrken/Small-Replit-Discord-Raid-Bot/blob/main/source_code.py) into main.py
7. Add a tab called "Shell" if its not there, and on the shell tab, paste "pip install discord" or "pip install discord.py"
# Creating a Discord Bot
Now you have to create your discord bot
If you already know how to make a bot and get its token, you can skip this part
1. [Click here](https://discord.com/developers/applications) and it it wll teleport you to to the Discord Developer Hub
2. Sign into your account if you havent signed in yet
3. Upon signing in, a button on the top right of your screen should say "New Application", click it
4. Something should pop up called create an application. Choose your Bot's name and agree to the discord developer TOS and press Create
5. Customise your bot in general information
6. Go on Bot , change the username to what you want and press "Reset Token" and copy your token
7. Now scroll down till you see **Privileged Gateway Intents** and put PRESENCE INTENT, SERVER MEMBERS INTENT and MESSAGE CONTENT INTENT to yes
8. Now back on replit, on line 67 on main.py where it says "client.run('YOUR_BOT_TOKEN')" replace YOUR_BOT_TOKEN with the token you copied
9. On line 7, replace YOUR_USER_ID with your user id
10. On line 9, replace YOUR_USER_ID with your user id, you cant also replace the other user id's with people you allow to use the bot or remove them
11. And your done! Now press run and click the authorization link on the "console" tab
12. Add the bot to the server you want and your done
# Commands
!bot deletechn': 'Deletes all channels in the server',
'!bot deletesrv': 'Deletes the entire server',
'!bot adduser [user_id]': 'Adds a user to the allowed users list',
!bot removeuser [user_id]': 'Removes a user from the allowed users list',
'!bot spam [message]': 'Spams the provided message',
'!bot ban all': 'Bans all members from the server except allowed users',
'!bot kick all': 'Kicks all members from the server except allowed users'
