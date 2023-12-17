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
8. Now go on Oauth2/URL Generator. On scopes select "bot" and on Bot Permissions select "Administrator"
9. Now back on replit, on line 67 on main.py where it says "client.run('YOUR_BOT_TOKEN')" replace YOUR_BOT_TOKEN with the token you copied. If it says "The value you pasted looks like a secret.
Store it securely using our Secrets feature." then press the Enter Key
10. On line 6, replace YOUR_USER_ID with your user id
11. On line 7, replace YOUR_USER_ID with your user id and replace YOUR_BOT_USER_ID with your bot user id. To get a bot user id, go on your bot and copy the number on the search bar (https://discord.com/developers/applications/YOUR_BOT_USER_ID/bot). You can also add more user ids to the allowed_users to make someone allowed to use your bot
12. Now go on back on your Bot and go on Oauth2/URL Generator. On scopes select "bot" and on Bot Permissions select "Administrator". Open the link on Generated URL and add the bot to your server
13. Upon adding your bot, go back to your repl and click run. Your Bot should go online and your done
# Commands
!bot deletechn': 'Deletes all channels in the server',
'!bot deletesrv': 'Deletes the entire server',
'!bot adduser [user_id]': 'Adds a user to the allowed users list',
!bot removeuser [user_id]': 'Removes a user from the allowed users list',
'!bot spam [message]': 'Spams the provided message',
'!bot ban all': 'Bans all members from the server except allowed users',
'!bot kick all': 'Kicks all members from the server except allowed users'
